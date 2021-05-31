

import pygame, sys, math, cmath

class Pad:
    def __init__(self):
        self.xPos = 350
        self.yPos = 550
        self.lenght = 100
        self.speed = 2.5
        self.image = pygame.image.load('img/paddle/paddle100.png')

    def reset(self):
        self.xPos = 350
        self.yPos = 550
        self.lenght = 100
        self.speed = 3
        self.image = pygame.image.load('img/paddle/paddle100.png')

    def getImage(self):
        return self.image

    def getLenght(self):
        return self.lenght

    def getPosition(self):
        return self.xPos,self.yPos

    def getVelocity(self):
        return self.speed

    def setVelocity(self,v):
        self.velocity = v

    def moveLeft(self):
        self.xPos -= self.speed
        if(self.xPos < 0):
            self.xPos = 0

    def moveRight(self):
        self.xPos += self.speed

        if(self.xPos + self.lenght > 800):
            self.xPos = 800 - self.lenght

    def increaseSpeed(self):
        self.speed +=  0.5

    def decreaseSpeed(self):
        self.speed -= 0.5


    def up(self):
        if(self.lenght < 160):
            self.lenght = self.lenght + 20
            self.xPos = self.xPos -10
        if(self.lenght == 60):
            self.image = pygame.image.load('img/paddle/paddle60.png')
        elif(self.lenght == 80):
            self.image = pygame.image.load('img/paddle/paddle80.png')
        elif(self.lenght == 100):
            self.image = pygame.image.load('img/paddle/paddle100.png')
        elif(self.lenght == 120):
            self.image = pygame.image.load('img/paddle/paddle120.png')
        elif(self.lenght == 140):
            self.image = pygame.image.load('img/paddle/paddle140.png')
        elif(self.lenght == 160):
            self.image = pygame.image.load('img/paddle/paddle160.png')


    def down(self):
        if(self.lenght > 40):
            self.lenght = self.lenght - 20
            self.xPos = self.xPos + 10
        if(self.lenght == 40):
            self.image = pygame.image.load('img/paddle/paddle40.png')
        elif(self.lenght == 60):
            self.image = pygame.image.load('img/paddle/paddle60.png')
        elif(self.lenght == 80):
            self.image = pygame.image.load('img/paddle/paddle80.png')
        elif(self.lenght == 100):
            self.image = pygame.image.load('img/paddle/paddle100.png')
        elif(self.lenght == 120):
            self.image = pygame.image.load('img/paddle/paddle120.png')
        elif(self.lenght == 140):
            self.image = pygame.image.load('img/paddle/paddle140.png')
