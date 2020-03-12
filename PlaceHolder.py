import pygame
from random import randint
class Ball:
    def __init__(self, radius, color, xcor, ycor, xvel, yvel):
        self.radius = radius
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.rect = pygame.Rect(
                            self.xcor,self.ycor,2*self.radius,2*self.radius)
    def move(self, Ninjaddle):
        if self.xcor < 0 or self.xcor > 1400 - self.radius:
            self.xvel = -self.xvel
        if self.ycor < 0 or self.ycor > 1000 - self.radius:
            self.yvel = -self.yvel
        if self.rect.colliderect(Ninjaddle):
            ninjaddle.ded()
        self.xcor += self.xvel
        self.ycor += self.yvel
        self.rect = pygame.draw.ellipse(screen, self.color,
                            [self.xcor,self.ycor,2*self.radius,2*self.radius])

class GreenBall(Ball):
    def __init__(self, radius, xcor, ycor, xvel, yvel):
        self.status = False
        super().__init__(radius, GREEN, xcor, ycor, xvel, yvel)

    def move(self, Ninjaddle):
        if not self.status:
            if self.xcor < 0 or self.xcor > 1400 - self.radius:
                self.xvel = -self.xvel
            if self.ycor < 0 or self.ycor > 1000 - self.radius:
                self.yvel = -self.yvel
            if self.rect.colliderect(Ninjaddle):
                self.status = True
                self = Ball(20,WHITE,0,0,self.xvel,self.yvel)
                ball_list.append(ball)
            self.xcor += self.xvel
            self.ycor += self.yvel
            self.rect = pygame.draw.ellipse(screen, self.color,
                            [self.xcor,self.ycor,2*self.radius,2*self.radius])

class Ninjaddle:
    def __init__(self,xcor,ycor, height, width, color, angle):
        self.rotatestate = True
        self.xcor = xcor
        self.ycor = ycor
        self.height = height
        self.width = width
        self.color = color
        self.movey = 0
        self.movex = 0
        self.angle = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = pygame.draw.rect(screen, self.color,
                            [self.xcor,self.ycor,self.width,self.height])
    def draw(self):
        self.ycor += self.movey
        if self.ycor > 1000 - self.height:
            self.ycor = 1000 - self.height
            self.movey = 0
        if self.ycor < 0:
            self.ycor = 0
            self.movey = 0   
        self.xcor += self.movex
        if self.xcor > 1400 - self.width:
            self.xcor = 1400 - self.width
            self.movex = 0
        if self.xcor < 0:
            self.xcor = 0
            self.movex = 0

        self.rect = pygame.draw.rect(screen, self.color,
                            [self.xcor,self.ycor,self.width,self.height])
    def rotate(self):
        self.image = pygame.Surface([self.height, self.width])
        self.height, self.width = self.width, self.height
        if self.rotatestate:
        	self.xcor -= 45
        	self.ycor += 45
        else:
        	self.xcor += 45
        	self.ycor -= 45
        self.rotatestate = not self.rotatestate
    def ded(self):
        self.xcor = 700
        self.ycor = 500    
#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ball_list = []
x = 200
y = 200

pygame.init()
screen = pygame.display.set_mode((1400,1000))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()

done = False

for i in range(0):
    ball = Ball(20,
                WHITE,
                randint(0,300),
                randint(0,950),
                randint(-3,3),
                randint(-3,3))

    ball_list.append(ball)

for i in range(10):
    greenball = GreenBall(20,
                randint(0,300),
                randint(0,950),
                randint(-3,3),
                randint(-3,3))
       
    ball_list.append(greenball)
ninjaddle = Ninjaddle(700, 500, 1000, 10, WHITE, 0)
acceleration = 1.2


while not done:
    xvelocity = 0
    yvelocity = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ninjaddle.movey = 5
            if event.key == pygame.K_w:
                ninjaddle.movey = -5
            if event.key == pygame.K_d:
                ninjaddle.movex = 5
            if event.key == pygame.K_a:
                ninjaddle.movex = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                ninjaddle.movex = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                ninjaddle.movey = 0
            if event.key == pygame.K_LEFT:
                ninjaddle.rotate()
            if event.key == pygame.K_RIGHT:
                ninjaddle.rotate()

    screen.fill(BLACK)
   


    ninjaddle.draw()


    for ball in ball_list:
        ball.move(ninjaddle)

    pygame.display.update()
    clock.tick(60)
pygame.quit()