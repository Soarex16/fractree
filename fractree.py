import pygame
import math

window_width = 1280
window_heigth = 720

min_length = 1
line_width = 1

length_scale = 0.65
incremental_angle = 30


def fractree(x, y, angle, length, level):
    if level > 0 and length > min_length:
        rad_angle = math.radians(angle)

        x_new = x - math.cos(rad_angle) * length
        y_new = y - math.sin(rad_angle) * length

        pygame.draw.line(surface, (0, 0, 0), (x, y), (x_new, y_new), line_width)

        fractree(x_new, y_new, angle - incremental_angle, length * length_scale, level - 1)
        fractree(x_new, y_new, angle + incremental_angle, length * length_scale, level - 1)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)


pygame.init()
window = pygame.display.set_mode((window_width, window_heigth))
pygame.display.set_caption("Fractree")

surface = pygame.display.get_surface()

window.fill((255, 255, 255))
pygame.display.update()

fractree(window_width / 2, window_heigth, 90, window_heigth / 3, 10)

pygame.display.flip()

while True:
    input(pygame.event.wait())
