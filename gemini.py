import pygame
import math

# Inicializa o Pygame
pygame.init()

# Define as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define as configurações da tela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gemini - Bola quicando em um hexágono giratório")

# Define as propriedades do hexágono
hex_radius = 200
hex_center = (WIDTH // 2, HEIGHT // 2)
hex_angle = 0
hex_rotation_speed = 0.02

# Define as propriedades da bola
ball_radius = 20
ball_position = [hex_center[0], hex_center[1] - hex_radius + ball_radius + 50]
ball_velocity = [5, -3]
gravity = 0.1
friction = 0.99
restitution = 0.8

# Define a fonte para exibir informações
font = pygame.font.Font(None, 24)

def calculate_hex_vertices(center, radius, angle):
    """Calcula os vértices de um hexágono."""
    vertices = []
    for i in range(6):
        x = center[0] + radius * math.cos(angle + i * math.pi / 3)
        y = center[1] + radius * math.sin(angle + i * math.pi / 3)
        vertices.append((x, y))
    return vertices

def is_point_inside_hexagon(point, vertices):
    """Verifica se um ponto está dentro do hexágono usando o método de enrolamento de raios."""
    x, y = point
    crossings = 0
    for i in range(6):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % 6]
        if (y1 <= y < y2 or y2 <= y < y1) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            crossings += 1
    return crossings % 2 == 1

def calculate_reflection(velocity, normal):
    """Calcula o vetor de reflexão de acordo com a lei da reflexão."""
    dot_product = velocity[0] * normal[0] + velocity[1] * normal[1]
    reflection = [velocity[0] - 2 * dot_product * normal[0],
                  velocity[1] - 2 * dot_product * normal[1]]
    return reflection

# Loop principal do jogo
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move a bola
    ball_velocity[1] += gravity
    ball_velocity[0] *= friction
    ball_velocity[1] *= friction
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # Gira o hexágono
    hex_angle += hex_rotation_speed
    hex_vertices = calculate_hex_vertices(hex_center, hex_radius, hex_angle)

    # Verifica se há colisão com as paredes do hexágono
    for i in range(6):
        x1, y1 = hex_vertices[i]
        x2, y2 = hex_vertices[(i + 1) % 6]
        # Calcula o vetor normal para a aresta
        normal = (-(y2 - y1), x2 - x1)
        # Normaliza o vetor
        length = math.hypot(*normal)
        normal = (normal[0] / length, normal[1] / length)

        # Verifica se a bola está dentro do hexágono e se movendo em direção à aresta
        if is_point_inside_hexagon(ball_position, hex_vertices):
            distance = normal[0] * (ball_position[0] - x1) + normal[1] * (ball_position[1] - y1)
            if distance < ball_radius and ball_velocity[0] * normal[0] + ball_velocity[1] * normal[1] < 0:
                # Reflete a velocidade da bola
                ball_velocity = calculate_reflection(ball_velocity, normal)
                ball_velocity[0] *= restitution
                ball_velocity[1] *= restitution

                # Corrige a posição da bola para evitar que ela fique presa na parede
                overlap = ball_radius - distance
                ball_position[0] += normal[0] * overlap
                ball_position[1] += normal[1] * overlap
                break

    # Limpa a tela
    screen.fill(BLACK)

    # Desenha o hexágono
    pygame.draw.polygon(screen, WHITE, hex_vertices, 2)

    # Desenha a bola
    pygame.draw.circle(screen, RED, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Exibe informações na tela
    program_name = font.render(f"Gemini", True, WHITE)
    velocity_text = font.render(f"Velocidade: ({ball_velocity[0]:.2f}, {ball_velocity[1]:.2f})", True, WHITE)
    gravity_text = font.render(f"Gravidade: {gravity:.2f}", True, WHITE)
    friction_text = font.render(f"Atrito: {friction:.2f}", True, WHITE)
    restitution_text = font.render(f"Restituição: {restitution:.2f}", True, WHITE)
    screen.blit(program_name, (10, 10))
    screen.blit(velocity_text, (10, 30))
    screen.blit(gravity_text, (10, 50))
    screen.blit(friction_text, (10, 70))
    screen.blit(restitution_text, (10, 90))

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros
    clock.tick(60)

# Sai do Pygame
pygame.quit()