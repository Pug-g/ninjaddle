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
    def move(self, Ninjaddle, PinkBall):
        if self.xcor < 0 or self.xcor > 1400 - self.radius:
            self.xvel = -self.xvel
        if self.ycor < 0 or self.ycor > 1000 - self.radius:
            self.yvel = -self.yvel
        if self.rect.colliderect(Ninjaddle) and ninjaddle.color == PINK:
            ninjaddle.ded()
        self.xcor += self.xvel
        self.ycor += self.yvel
        self.rect = pygame.draw.ellipse(screen, self.color,
                            [self.xcor,self.ycor,2*self.radius,2*self.radius])
    def reset(self):
        self.xcor = randint(0,300)
        self.ycor = randint(0,950)

    def __str__(self):

        return str(self.color)

class GreenBall(Ball):
    def __init__(self, radius, xcor, ycor, xvel, yvel):
        self.status = False
        super().__init__(radius, GREEN, xcor, ycor, xvel, yvel)

    def move(self, Ninjaddle, PinkBall):
        if not self.status:
            if self.xcor < 0 or self.xcor > 1400 - self.radius:
                self.xvel = -self.xvel
            if self.ycor < 0 or self.ycor > 1000 - self.radius:
                self.yvel = -self.yvel
            if self.rect.colliderect(Ninjaddle) or self.rect.colliderect(PinkBall):
                self.status = True
                self = Ball(20,WHITE,0,0,self.xvel,self.yvel)
                ball_list.append(self)
                return
            self.xcor += self.xvel
            self.ycor += self.yvel
            self.rect = pygame.draw.ellipse(screen, self.color,
                            [self.xcor,self.ycor,2*self.radius,2*self.radius])

class PinkBall(Ball):
    def __init__(self, radius, xcor, ycor, xvel, yvel, offset):
        self.offset=offset
        super().__init__(radius, PINK, xcor, ycor, xvel, yvel)

    def move(self, Ninjaddle, PinkBall):
        self.xcor += (self.xcor-Ninjaddle.xcor)/100*-1 + self.offset
        self.ycor += (self.ycor-Ninjaddle.ycor)/100*-1 
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
        self.lives = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = pygame.draw.rect(screen, self.color,
                            [self.xcor,self.ycor,self.width,self.height])
    def draw(self):
        if self.color == PINK:
            self.ycor += self.movey
        if self.ycor > 1000 - self.height:
            self.ycor = 1000 - self.height
            self.movey = 0
        if self.ycor < 0:
            self.ycor = 0
            self.movey = 0   
        if self.color == PINK:
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
        global done
        self.xcor = 1400
        self.ycor = 1000
        greenball = GreenBall(20,
                randint(0,300),
                randint(0,950),
                randint(-3,3),
                randint(-3,3))
        
        ball_list.append(greenball)
        for ball in ball_list:
            ball.reset()
        if self.lives > 1:
            self.lives -= 1
        else:
            self.lives -= 1
            done = True

    def colorswap(self):
        if self.color == PINK:
            self.color = BLACK
        else:
            self.color = PINK

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (255,105,180)
ball_list = []
x = 200
y = 200
#hasgb = False

pygame.init()
screen = pygame.display.set_mode((1400,1000))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',30)
done = False

for i in range(5):
    ball = Ball(20,
                WHITE,
                randint(0,300),
                randint(0,950),
                randint(-3,3),
                randint(-3,3))

    ball_list.append(ball)

for i in range(1):
    greenball = GreenBall(20,
                randint(0,300),
                randint(0,950),
                randint(-3,3),
                randint(-3,3))
       
    ball_list.append(greenball)
ninjaddle = Ninjaddle(1400, 1000, 100, 10, PINK, 0)
acceleration = 1.2

for i in range(3):
    pinkball = PinkBall(20,
                randint(1100, 1400),
                randint(0,950),
                randint(-3,3),
                randint(-3,3),
                i-1)
       
    ball_list.append(pinkball)

for ball in ball_list:
    print("pre" + str(ball))

while not done:
    hasgb = False
    xvelocity = 0
    yvelocity = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ninjaddle.movey = 5
            if event.key == pygame.K_w:
                ninjaddle.movey = -5
            if event.key == pygame.K_d:
                ninjaddle.movex = 5
            if event.key == pygame.K_a:
                ninjaddle.movex = -5
            if event.key == pygame.K_SPACE:
                ninjaddle.colorswap()  
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
   

    print("precheck: " + str(hasgb))
    ninjaddle.draw()
    for ball in ball_list:
        ball.move(ninjaddle, pinkball)
        if ball.color == (0, 255, 0):
            print(ball)
            hasgb = True
    print("post: " + str(hasgb))
    if hasgb == False:
        print("GG, you win I guess or something")
        done = True
    text = font.render(str(pygame.time.get_ticks()/1000), True, WHITE)
    text2 = font.render(str(ninjaddle.lives), True, WHITE)
    screen.blit(text, (50, 50))
    screen.blit(text2, (200, 50))
    pygame.display.update()
    clock.tick(60)
if ninjaddle.lives < 1:
    print("All out of lives.")


pygame.quit()