import pygame
from Car import Car
from color import RED, WHITE


# 우리의 어플리케이션!
class App:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

        # 게임의 창 크기
        self.size = self.weight, self.height = 640, 400

        # FPS, Frame per second
        # 화면이 몇 초에 한번씩 바뀔 것인가를 설정, FPS, 1초에 60번 화면을 업데이트
        self.FPS = 60

    def on_init(self):
        pygame.init()

        # 디스플레이 모드 설정, self.screen에는 화면을 그릴 수 있도록 해주는 object가 담긴다
        self.screen = pygame.display.set_mode(self.size, 0, 16)

        # 창의 색깔을 정한다
        self.screen.fill(WHITE)

        # 창의 이름을 정한다.
        pygame.display.set_caption("Car Racing")

        # running flag, True 일때 게임이 계속되고 false 일때 종료된다
        self.running = True

        # 게임의 모든 sprite를 포함하는 변수
        self.sprites = pygame.sprite.Group()

        # 플레이어의 자동차 하나를 만든다
        playerCar = Car(RED, 20, 30)
        playerCar.rect.x = 0
        playerCar.rect.y = 0

        # 플레이어의 자동차를 게임에 추가한다
        self.sprites.add(playerCar)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.sprites.update()

    def on_render(self):
        self.sprites.draw(self.screen)

        # 화면 업데이트
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        # 이 코드는 무시하셔도 좋습니다.
        if self.on_init() == False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            # 화면이 몇 초에 한번씩 바뀔 것인가를 설정, FPS, 1초에 60번 화면을 업데이트
            self.clock.tick(self.FPS)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
