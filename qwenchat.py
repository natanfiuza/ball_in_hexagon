import pygame
import math

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qwen - Bola Quicando em Hexágono Giratório")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Configurações do hexágono
HEXAGON_RADIUS = 300
HEXAGON_CENTER = (WIDTH // 2, HEIGHT // 2)
NUM_SIDES = 6

# Configurações da bola
BALL_RADIUS = 10
ball_pos = [WIDTH // 2 + HEXAGON_RADIUS // 2, HEIGHT // 2]
ball_velocity = [3, -5]  # Velocidade inicial da bola
gravity = 0.2  # Gravidade
friction = 0.99  # Atrito


# Define a fonte para exibir informações
font = pygame.font.Font(None, 24)

# Função para desenhar um hexágono rotacionado
def draw_rotated_hexagon(surface, color, center, radius, rotation_angle):
    angle_step = 2 * math.pi / NUM_SIDES
    points = []
    for i in range(NUM_SIDES):
        angle = angle_step * i + rotation_angle
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points, 2)

# Função para verificar colisão entre a bola e o hexágono
def check_collision(ball_pos, ball_radius, hexagon_center, hexagon_radius, rotation_angle):
    angle_step = 2 * math.pi / NUM_SIDES
    min_distance = float('inf')
    collision_normal = None

    for i in range(NUM_SIDES):
        # Calcula os pontos dos vértices do hexágono
        angle1 = angle_step * i + rotation_angle
        angle2 = angle_step * ((i + 1) % NUM_SIDES) + rotation_angle
        p1 = (
            hexagon_center[0] + hexagon_radius * math.cos(angle1),
            hexagon_center[1] + hexagon_radius * math.sin(angle1),
        )
        p2 = (
            hexagon_center[0] + hexagon_radius * math.cos(angle2),
            hexagon_center[1] + hexagon_radius * math.sin(angle2),
        )

        # Calcula a distância da bola à linha formada pelos vértices
        edge_vector = (p2[0] - p1[0], p2[1] - p1[1])
        ball_vector = (ball_pos[0] - p1[0], ball_pos[1] - p1[1])

        edge_length_sq = edge_vector[0] ** 2 + edge_vector[1] ** 2
        t = max(0, min((ball_vector[0] * edge_vector[0] + ball_vector[1] * edge_vector[1]) / edge_length_sq, 1))
        closest_point = (p1[0] + t * edge_vector[0], p1[1] + t * edge_vector[1])

        distance_sq = (ball_pos[0] - closest_point[0]) ** 2 + (ball_pos[1] - closest_point[1]) ** 2
        if distance_sq < min_distance:
            min_distance = distance_sq
            collision_normal = (
                (ball_pos[0] - closest_point[0]) / math.sqrt(distance_sq),
                (ball_pos[1] - closest_point[1]) / math.sqrt(distance_sq),
            )

    if min_distance <= ball_radius ** 2:
        return True, collision_normal
    return False, None

# Loop principal
clock = pygame.time.Clock()
rotation_angle = 0
running = True

while running:
    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a posição da bola
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Aplica gravidade
    ball_velocity[1] += gravity

    # Aplica atrito
    ball_velocity[0] *= friction
    ball_velocity[1] *= friction

    # Verifica colisão com o hexágono
    collided, normal = check_collision(ball_pos, BALL_RADIUS, HEXAGON_CENTER, HEXAGON_RADIUS, rotation_angle)
    if collided:
        # Reflete a velocidade da bola com base na normal da colisão
        dot_product = ball_velocity[0] * normal[0] + ball_velocity[1] * normal[1]
        ball_velocity[0] -= 2 * dot_product * normal[0]
        ball_velocity[1] -= 2 * dot_product * normal[1]

    # Desenha o hexágono giratório
    draw_rotated_hexagon(screen, BLUE, HEXAGON_CENTER, HEXAGON_RADIUS, rotation_angle)

    # Desenha a bola
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)


    program_name = font.render(f"Qwen Chat", True, BLACK)
    screen.blit(program_name, (10, 10))

    # Atualiza o ângulo de rotação do hexágono
    rotation_angle += 0.02

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()