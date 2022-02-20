import pygame.image

class Seed:
    def __init__(self):
        self.count = 0
        self.image = pygame.image.load(r'img/Seed.png')
        self.pos = (750, 0)

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        self.write(screen)

    def write(self, screen):
        font = pygame.font.SysFont(None, 30)
        text = font.render(f'{self.count}', True, [255, 255, 255])
        screen.blit(text, (765, 65))