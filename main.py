import pygame


# 우리의 어플리케이션!
class App:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

        # 게임의 창 크기
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()

        # 디스플레이 모드 설정
        pygame.display.set_mode(self.size, 0, 16)
        self.running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

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

            # 화면이 몇 초에 한번씩 바뀔 것인가를 설정
            self.clock.tick(60)

            # 화면 업데이트
            pygame.display.flip()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
