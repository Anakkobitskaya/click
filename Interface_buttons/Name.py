import pygame.image

class Name:
    def __init__(self):
        self.image = pygame.image.load(r'img/Name.png')
        self.pos = (100, 0)

    def draw(self, screen):
        screen.blit(self.image, self.pos)