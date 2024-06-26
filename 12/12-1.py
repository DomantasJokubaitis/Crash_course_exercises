import pygame
import sys
from angel import Angel

class Exercise:

    def __init__(self):

        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (200, 0, 250)
        self.angel = Angel(self)

    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
        

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.angel.blitme()
        pygame.display.flip()


   



if __name__ == "__main__":

    ai = Exercise()
    ai.run_game()