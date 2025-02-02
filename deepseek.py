import pygame
import math

# Inicialização do Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DeepSeek - Bola Quicando em Hexágono Giratório")

# Configurações de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Parâmetros do hexágono
centro = (width//2, height//2)
raio_hexagono = 200
num_lados = 6
velocidade_rotacao = math.radians(0.8)  # Mais lento para melhor visualização
angulo_hexagono = 0

# Parâmetros da bola
raio_bola = 12
bola_pos = [width//2, height//2]
bola_vel = [3.0, 0.0]
gravidade = 0.15
atrito = 0.985
coeficiente_restituicao = 0.85  # Perda de energia nas colisões


# Define a fonte para exibir informações
font = pygame.font.Font(None, 24)

def ponto_mais_proximo(A, B, P):
    """Calcula o ponto mais próximo de P no segmento AB"""
    ax, ay = A
    bx, by = B
    px, py = P
    
    vetor_ab = (bx - ax, by - ay)
    vetor_ap = (px - ax, py - ay)
    
    t = (vetor_ap[0] * vetor_ab[0] + vetor_ap[1] * vetor_ab[1]) / (vetor_ab[0]**2 + vetor_ab[1]**2 + 1e-8)
    t = max(0, min(1, t))
    
    return (ax + t * vetor_ab[0], ay + t * vetor_ab[1])

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza rotação do hexágono
    angulo_hexagono += velocidade_rotacao
    angulo_hexagono %= 2 * math.pi

    # Calcula vértices do hexágono
    vertices = []
    for i in range(num_lados):
        angulo = angulo_hexagono + i * (2 * math.pi / num_lados)
        x = centro[0] + raio_hexagono * math.cos(angulo)
        y = centro[1] + raio_hexagono * math.sin(angulo)
        vertices.append((x, y))

    # Aplica forças na bola
    bola_vel[1] += gravidade
    nova_pos = [bola_pos[0] + bola_vel[0], bola_pos[1] + bola_vel[1]]

    # Verifica colisões com cada parede
    colidiu = False
    for i in range(num_lados):
        A = vertices[i]
        B = vertices[(i+1) % num_lados]
        
        ponto_colisao = ponto_mais_proximo(A, B, nova_pos)
        dx = nova_pos[0] - ponto_colisao[0]
        dy = nova_pos[1] - ponto_colisao[1]
        distancia = math.hypot(dx, dy)
        
        if distancia < raio_bola:
            # Calcula vetores para a colisão
            vetor_ab = (B[0] - A[0], B[1] - A[1])
            normal = (-vetor_ab[1], vetor_ab[0])
            comprimento_normal = math.hypot(normal[0], normal[1])
            
            if comprimento_normal == 0:
                continue
                
            normal = (normal[0]/comprimento_normal, normal[1]/comprimento_normal)
            
            # Calcula velocidade da parede no ponto de colisão
            vx_parede = -velocidade_rotacao * (ponto_colisao[1] - centro[1])
            vy_parede = velocidade_rotacao * (ponto_colisao[0] - centro[0])
            
            # Velocidade relativa
            v_relativa = [bola_vel[0] - vx_parede, bola_vel[1] - vy_parede]
            
            # Reflexão do vetor velocidade
            produto_escalar = v_relativa[0] * normal[0] + v_relativa[1] * normal[1]
            v_relativa_reflexao = [
                v_relativa[0] - 2 * produto_escalar * normal[0],
                v_relativa[1] - 2 * produto_escalar * normal[1]
            ]
            
            # Aplica coeficiente de restituição e atualiza velocidade
            bola_vel[0] = (v_relativa_reflexao[0] + vx_parede) * coeficiente_restituicao
            bola_vel[1] = (v_relativa_reflexao[1] + vy_parede) * coeficiente_restituicao
            
            # Corrige posição para evitar sobreposição
            sobreposicao = raio_bola - distancia
            nova_pos[0] += normal[0] * sobreposicao * 1.1
            nova_pos[1] += normal[1] * sobreposicao * 1.1
            colidiu = True

    # Atualiza posição e aplica atrito
    if not colidiu:
        bola_pos = nova_pos
        bola_vel[0] *= atrito
        bola_vel[1] *= atrito

    # Desenha elementos
    screen.fill(BLACK)
    pygame.draw.polygon(screen, WHITE, vertices, 2)
    pygame.draw.circle(screen, RED, (int(bola_pos[0]), int(bola_pos[1])), raio_bola)
    program_name = font.render(f"DeepSeek", True, WHITE)
    screen.blit(program_name, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()