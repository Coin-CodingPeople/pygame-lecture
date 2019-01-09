# pygame-lecture

- 모든 것을 이해하지는 못한다
- 보조자료
- 복습자료

2019 겨울 코딩캠프 강의 교안

목표

- 게임 프로그래밍 맛보기
- Pygame 사용해보기
- Python으로 무언가를 만들어보기

1. Pygame 이란?
	1. 모듈이란?
	2. Pygame이란?
	3. Pygame 설치하기
	4. Hello Pygame! 	
2. 게임 프로그래밍
	1. 게임이란?
	2. 게임의 필수요소
	3. 게임과 프로그래밍 
3. Pygame 시작하기

## 1. Pygame이란?

### 1. 모듈이란?
**유용한 코드조각들을 쓰기 쉽게 모아 놓은 것**

#### Keyword
- 반복작업
- 공유
- input/output
- 알아야 하는 것, 알 필요가 없는 것

우리는 닭의 모이를 주면 달걀이 나온다는 것을 안다. 그러나 닭이 무슨 작업을 하는지 어떻게 소화를 시키는지를 알 필요는 없다.

### 2. Pygame이란?
[Wikipedia](https://en.wikipedia.org/wiki/Pygame)

Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

- 비디오 게임을 제작하기 위해 필요
- 크로스 플랫폼 파이썬 모듈
- 컴퓨터 그래픽스와 사운드 관련 라이브러리(=모듈)을 포함하고 있다

### 3. Pygame 설치하기
[Pygame Getting Started](https://www.pygame.org/wiki/GettingStarted)

### 4. Hello Pygame!
[add first pygame app](https://github.com/Coin-CodingPeople/pygame-lecture/blob/8940b692e4b6d2d84843ab51a0d6e1181fbb14ad/main.py)

### 요약
- Pygame에 대한 간단한 소개
- 창 띄워보기
- 모듈이란?

## 2. 게임 프로그래밍

### 1. 게임이란?
정해진 규칙에 따라 정해진 목표를 향해가는 것

마우스, 키보드 등의 입력장치를 통해 여러 활동을 하다 보면 레벨업, 보스잡이와 같은 목표를 이룰 수 있다.

#### 비디오게임이란?
마우스, 키보드, 조이스틱과 같은 표준입력장치를 통해 입력을 하고 모니터를 이용하여 출력을 하여 게임을 진행하는 것

### 2. 게임의 필수요소
입력 받기, 처리하기, 출력 하기

1. 게임 실행
2. 초기화
3. 입력
4. 처리
5. 출력
6. 종료

### 3. 게임과 프로그래밍

<hr/>

1. Creating Simple Window
2. Creating Sprites using Pygame
3. How to control your sprites
4. Changing Sprites' image

## How to run?
```shell
$ virtualenv --no-site-packages -p python3.6 <env_name>
$ source <env_name>/bin/activate
(<env_name>)$ pip install -r path/to/requirements.txt
```

## Requirements

### Git Installation
[git](https://coding-factory.tistory.com/245)

### Clone This repository
`$ git clone https://github.com/Coin-CodingPeople/pygame-lecture.git`

## What is Pygame?
> Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
> 출처 [위키피디아](https://en.wikipedia.org/wiki/Pygame)
> 
> PyGame is based on SDL. A C library that is cross platform and also very simple. PyGame however is not just simple wrapper for it, but also add its own features, so writing games is even simpler.
> 출처 [PyGameTutorials](http://pygametutorials.wikidot.com/tutorials-basic)

- 크로스 플랫폼 파이썬 모듈
- 비디오 게임 제작용
- 컴퓨터 그래픽스와 사운드 라이브러리를 보함하고 있다.
- SDL 기반 라이브러리


## How to Install

### Requirements
python 3.6.1 or greater

[Pygame official site, Getting Started](https://www.pygame.org/wiki/GettingStarted)

## Tutorial

### Requirements

#### python3 basic syntax
variable, if, else, function, while, array

### Game Loop
Game loop is the place where events, game logic and rendering onto screen is performed. It should look similar to:

```python
while True:
    events()
    loop()
    render()
```
게임루프는 이벤트와, 게임 로직, 스크린 디스플레이 등이 실행되는 공간이다. 게임과 직접적으로 연관되는 모든 것들이 들어가는 곳.

#### 예시
플레이어가 움직인다, 오른쪽으로 회전한다, 곰돌이 모양 이미지를 보여준다, ESC를 누르면 메뉴를 보여주거나 게임을 종료한다 등

### First Code
```python
import pygame
from pygame.locals import *
 
class App:
    def on_execute(self):
        pass
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
```

As you can see I prefer classes than functions. That is because OOP is getting more and more fans in game programming due to it correlation with game design. Simply in game we have objects, theirs tasks etc. even when programing without classes.

App will be our main class. To run game we will only need call on_execute() function. Yes this function will contain our Game Loop.

App이라는 클래스를 통해 우리의 게임 어플리케이션을 통합적으로 관리한다. on_execute라는 오브젝트 메소드에서 Game Loop를 구현하여 게임을 만들 것이다.

### OOP in Pygame

#### class, object란?

##### object
object란 실물 대상을 추상화한 것, 즉. 코드를 통해 실제 대상을 표현한 것.

##### class
class(ification)

자동차를 예로 들어보자. 모든 자동차는 같이 공유하고 있는 것들이 있고 공유하지 않는 것들이 있다. 모든 자동차는 엔진을 가지고 있고 엑셀 페달이 있다. 하지만 번호판, 열쇠와 같은 것들은 각기 다른 속성을 가지고 있다.

이처럼 모든 자동차가 공유하는 것들과 아닌 것들을 구분하여 하나의 자동차라는 종류를 만들어 놓은 것이 class, 이 class를 이용하여 만든 나의 자동차, 아빠의 자동차, 엄마의 자동차와 같은 실물 대상을 object라고 한다.

붕어빵틀을 class, 붕어빵을 object라고 생각하면 편하다.

#### 그래서, OOP란?
Object Oriented Programming의 줄임말로 실물을 Object라는 단위체를 이용하여 프로그래밍을 설계한 것. 게임에서는 플레이어, 몬스터와 같이 하나의 실물 대상체를 코드로 표현하면 편리하기 때문에 OOP를 통하여 설계하는 경우가 많다.

Pygame에서도 마찬가지로 OOP를 이용하여 프로그램을 설계하면 보다 깔끔한 설계가 가능하다.

이 어플리케이션에서는 두개의 App을 통해 두개의 창을 띄워 창 간의 통신이 가능하도록 할 수 있다. (멀티 플레이)

### Creating simple window
```python
import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
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
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
```

on\_init, on\_event, on\_loop, on\_render, on\_cleanup 이라는 다섯가지 오브젝트 메소드를 on\_execute라는 메소드가 감싸고 있다.

즉, 앱을 실행하면 on\_execute가 실행이 되고 on\_execute에서 나머지 다섯 메소드가 적절한 순서에 따라 실행이 된다.

이 모든 것들을 다 구현할 필요는 없다.

#### on_init
on_init calls pygame.init() that initialize all PyGame modules. Then it create main display - 640x400 window and try to use hardware acceleration. At the end this routine sets \_running to True.

Pygame을 이용하여 게임을 만들기 위해서는 pygame.init을 실행해주어야 한다. 이 함수는 우리의 컴퓨터에게 메모리를 어느정도 사용할 것인지, 그래픽 연산이 어느정도 필요한지 등의 복잡한 처리를 대신 해준다.
 
#### on_event
on\_event check if Quit event happened if so sets _running to False wich will break game loop.

##### Example
ESC키를 누르면 게임이 종료된다.

#### on_loop
on_loop and OnRender do nothing.

Game Loop가 반복될때마다 실행될 로직이 놓이는 곳.

##### Example
게임 루프가 돌때 마다 플레이어의 체력이 1 깎인다

#### on_render
그래픽 구현을 위해 필요한 코드들이 놓이는 곳

#### on_cleanup
on_cleanup call pygame.quit() that quits all PyGame modules.

정상적으로 pygame프로그램을 종료하기 위해서는 pygame.quit()을 실행해주어야 하고 다른 네트워크 연결등을 끊어주기 위한 코드들이 이 곳에 위치한다.

### Creating Sprites using Pygame

```python
# Car.py
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
```

```python

```
