import pygame
import math

# --- Constantes da simulação ---
WIDTH, HEIGHT = 800, 600            # Tamanho da janela
FPS = 60                            # Frames por segundo
GRAVITY = 0.3                       # Aceleração da gravidade
ATRITO_AR = 0.999                   # Atrito do ar (reduz gradualmente a velocidade)
RESTITUICAO = 0.9                   # Coeficiente de restituição (perda de energia na colisão)
HEXAGON_RADIUS = 250                # Raio do hexágono (distância do centro aos vértices)
BALL_RADIUS = 12                    # Raio da bola

# Define as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# --- Classe que representa a bola ---
class Ball:
    def __init__(self):
        # Inicia a bola no centro da tela com uma velocidade inicial arbitrária
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.vx = 5
        self.vy = 0

    def update(self):
        # Aplica a gravidade
        self.vy += GRAVITY

        # Atualiza a posição com base na velocidade
        self.x += self.vx
        self.y += self.vy

        # Aplica o atrito do ar
        self.vx *= ATRITO_AR
        self.vy *= ATRITO_AR

# --- Função para calcular os vértices do hexágono giratório ---
def get_hexagon_vertices(center, radius, rotation):
    vertices = []
    # O hexágono possui 6 lados; calcula cada vértice usando ângulos igualmente espaçados
    for i in range(6):
        angle = math.radians(60 * i) + rotation
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        vertices.append((x, y))
    return vertices

# --- Função para calcular a distância de um ponto a um segmento de reta ---
def point_line_distance(point, line_start, line_end):
    px, py = point
    x1, y1 = line_start
    x2, y2 = line_end
    # Vetor da reta
    dx = x2 - x1
    dy = y2 - y1
    # Caso degenerate (segmento com comprimento zero)
    if dx == 0 and dy == 0:
        return math.hypot(px - x1, py - y1), (x1, y1)
    # Calcula o parâmetro t que indica a posição do ponto projetado sobre a reta
    t = ((px - x1) * dx + (py - y1) * dy) / (dx**2 + dy**2)
    t = max(0, min(1, t))
    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    distance = math.hypot(px - proj_x, py - proj_y)
    return distance, (proj_x, proj_y)

# --- Função para refletir a velocidade da bola ao colidir com uma parede ---
def reflect_velocity(vx, vy, normal):
    # Fórmula da reflexão: v' = v - 2*(v . n)*n, onde n é o vetor normal unitário
    dot = vx * normal[0] + vy * normal[1]
    rx = vx - 2 * dot * normal[0]
    ry = vy - 2 * dot * normal[1]
    return rx, ry

# --- Função principal da simulação ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChatGPT - Bola Quicando em Hexágono Giratório")
    clock = pygame.time.Clock()

    running = True
    ball = Ball()
    hex_rotation = 0  # Ângulo de rotação do hexágono
    center = (WIDTH / 2, HEIGHT / 2)  # Centro do hexágono (e da tela)

    # Define a fonte para exibir informações
    font = pygame.font.Font(None, 24)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Preenche o fundo da tela com preto
        screen.fill((0, 0, 0))

        # Atualiza a rotação do hexágono
        hex_rotation += 0.02
        hex_vertices = get_hexagon_vertices(center, HEXAGON_RADIUS, hex_rotation)

        # Desenha o hexágono (apenas as bordas, com 3 pixels de espessura)
        pygame.draw.polygon(screen, (0, 255, 0), hex_vertices, 4)

        # Atualiza a bola
        ball.update()

        # Verifica colisão da bola com cada uma das paredes do hexágono
        for i in range(6):
            p1 = hex_vertices[i]
            p2 = hex_vertices[(i + 1) % 6]
            distance, proj = point_line_distance((ball.x, ball.y), p1, p2)

            if distance < BALL_RADIUS:
                # Para obter o vetor normal apontando para o interior do hexágono,
                # usamos o fato de que o centro do hexágono está dentro dele.
                # Assim, a direção de (centro - ponto médio da parede) é a direção interna.
                wall_midpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
                nx = center[0] - wall_midpoint[0]
                ny = center[1] - wall_midpoint[1]
                n_length = math.hypot(nx, ny)
                if n_length != 0:
                    nx /= n_length
                    ny /= n_length

                # Verifica se a bola está se movendo em direção à parede (produto interno negativo)
                if ball.vx * nx + ball.vy * ny < 0:
                    # Reflete a velocidade da bola
                    ball.vx, ball.vy = reflect_velocity(ball.vx, ball.vy, (nx, ny))
                    # Aplica o coeficiente de restituição (perda de energia)
                    ball.vx *= RESTITUICAO
                    ball.vy *= RESTITUICAO
                    # Ajusta a posição da bola para que ela não fique "presa" dentro da parede
                    overlap = BALL_RADIUS - distance
                    ball.x += nx * overlap
                    ball.y += ny * overlap

        # Desenha a bola (em vermelho)
        pygame.draw.circle(screen, (255, 0, 0), (int(ball.x), int(ball.y)), BALL_RADIUS)

        program_name = font.render(f"ChatGPT", True, WHITE)
        screen.blit(program_name, (10, 10))

        # Atualiza a tela e regula os FPS
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
