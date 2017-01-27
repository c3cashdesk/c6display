import sys

import pygame
from pygame.locals import QUIT


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def main():
    pygame.init()
    surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),  # resolution=,
        pygame.FULLSCREEN,  # flags=
        8,  # depth=
    )
    image = pygame.image.load('myimage.png')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        surface.blit(
            source=image,
            dest=(
                (SCREEN_WIDTH - image.get_rect().w)/2,
                (SCREEN_HEIGHT - image.get_rect().h)/2,
            ),
        )
        pygame.display.flip()


if __name__ == '__main__':
    main()
