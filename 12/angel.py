import pygame

class Angel:

    def __init__(self, ai):

        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        self.image = pygame.image.load("C:/Users/doman/Desktop/Python_work/12/angel.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):

        self.screen.blit(self.image, self.rect)
