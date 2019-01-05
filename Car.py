import pygame
from color import WHITE


class Car(pygame.sprite.Sprite):
    # pygame에서 어떤 물체하나를 만들기 위해선 pygame.sprite.Sprite를 상속받아야 한다.

    def __init__(self, color, width, height):
        # pygame에서 어떤 물체 하나를 만들기 위해선 super().__init__()을 사용해야 한다.
        super().__init__()

        # 차의 모습을 결정한다
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # 실제로 차를 그린다!
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
