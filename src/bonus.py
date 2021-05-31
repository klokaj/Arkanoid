import random
import pygame

class Bonus():
    def __init__(self, xpos, ypos):
        random.seed()
        self.xpos = xpos
        self.ypos = ypos
        self.yVelocity = 1
        self.type = ""
        self.state = "Active"
        self.size = 0

        randNumber = random.randrange(8)
        if(randNumber == 0):
            self.image = pygame.image.load('img/bonus/heartBonus.png')
            self.type = "HEART"
            self.size = 44
        elif(randNumber == 1):
            self.image = pygame.image.load('img/bonus/ballBonus.png')
            self.type = "BALL_BONUS"
            self.size = 40
        elif(randNumber == 2):
            self.image = pygame.image.load('img/bonus/ballSpeedUp.png')
            self.type = "BALL_SPEEDUP"
            self.size = 40
        elif(randNumber == 3):
            self.image = pygame.image.load('img/bonus/ballSpeedDown.png')
            self.type = "BALL_SPEEDDOWN"
            self.size = 40
        elif(randNumber == 4):
            self.image = pygame.image.load('img/bonus/paddleUp.png')
            self.type = "PADDLE_UP"
            self.size = 12
        elif(randNumber == 5):
            self.image = pygame.image.load('img/bonus/paddleDown.png')
            self.type = "PADDLE_DOWN"
            self.size = 12
        elif(randNumber == 6):
            self.image = pygame.image.load('img/bonus/paddleSpeedUp.png')
            self.type = "PADDLE_SPEEDUP"
            self.size = 18
        elif(randNumber == 7):
            self.image = pygame.image.load('img/bonus/paddleSpeedDown.png')
            self.type = "PADDLE_SPEEDDOWN"
            self.size = 18

    def getImage(self):
        return self.image

    def getPosition(self):
        return self.xpos, self.ypos

    def move(self):
        self.ypos = self.ypos + self.yVelocity

    def getState(self):
        return self.state

    def disactive(self):
        self.state = "Disactive"

