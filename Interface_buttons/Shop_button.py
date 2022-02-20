import pygame.image

class ShopButton:
    def __init__(self):
        self.image = pygame.image.load(r'img/Shop_button.png')
        self.pos = (0, 0)

    def draw(self, screen):
        screen.blit(self.image, self.pos)