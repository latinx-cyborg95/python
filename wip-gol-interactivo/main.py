import pygame
from random import randint, shuffle
from math import floor

from gol import GameOfLife
# from helper import funcion_prueba


def main():
    regla = [2, 3]
    valores_validos = [x for x in range(9)]

    gol = GameOfLife(50, 50)
    gol_activo = True
    cell_color = (randint(100, 255), randint(100, 255), randint(100, 255))

    WIDTH = 800
    HEIGHT = 800

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()

    # Calculo el tamaño de la representacion de cada celula
    tam_x = WIDTH / gol.cells.shape[0]
    tam_y = HEIGHT / gol.cells.shape[1]
    margen = 0  # El espacio entre celula y celula

    running = True
    frame_count = 0
    while running:

        # Monitorear eventos
        for event in pygame.event.get():

            # Manejo el flujo del juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gol.set_random()

                if event.key == pygame.K_0:
                    gol.set_ceros()

                if event.key == pygame.K_SPACE:
                    gol_activo = not gol_activo
                    print(f"gol_activo = {gol_activo}")

            # Cuando termina el clic, obtengo la posición del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
                x = floor(mouse_position[0] / tam_x)
                y = floor(mouse_position[1] / tam_y)

                gol.switch(x, y)

            if event.type == pygame.QUIT:
                running = False


        screen.fill((255, 255, 255, 10))

        # Dibujar el array
        draw_array(screen, gol.cells,
                   cell_color,
                   # (255, 0, 0),
                   tam_x, tam_y, margen)

        # Cambiar la regla cada 30 cuadros
        #if frame_count % 30 == 0:
        #    shuffle(valores_validos)
        #    print(valores_validos[:3])

        # Computar la siguiente iteración
        if gol_activo and frame_count % 30 == 0:
            # gol.compute_next(valores_validos[:3])
            gol.compute_next(regla)

        pygame.display.flip()
        clock.tick(30)
        frame_count += 1

    pygame.quit()


def draw_array(screen, array, cell_color, x_size, y_size, margin):
    # Lo imprimo en pantalla

    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            #  print(f"{x} {y} {columna}")

            if array[y][x] != 0:
                pygame.draw.rect(
                    screen,
                    life2color(array[y][x], cell_color),  # el color
                    (x * x_size, y * y_size, x_size - margin, y_size - margin)  # pos y tam
                )
            else:
                pygame.draw.rect(
                    screen,
                    (0, 0, 0),
                    (x * x_size, y * y_size, x_size - margin, y_size - margin)
                )


def life2color(life, color):
    return (life + 1) * color[0] / 4,\
           (life + 1) * color[1] / 4,\
           (life + 1) * color[2] / 5

if __name__ == '__main__':
    main()