import pygame, sys, math, cmath
from pygame.locals import *

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

class drawer():
    def __init__(self, ball, pad, brick, bonus, gameState, xSize, ySize, file):
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((xSize,ySize))
        pygame.display.set_caption('ARKANOID')
        self.font = pygame.font.Font("src/ARCADECLASSIC.TTF",40)
        self.smallFont = pygame.font.Font("src/ARCADECLASSIC.TTF", 20)
        self.bigFont = pygame.font.Font("src/ARCADECLASSIC.TTF", 120)
        self.ball = ball
        self.pad = pad
        self.brick = brick
        self.bonus = bonus
        self.gameState = gameState
        self.fileName = file

    def draw(self):

        self.surface.fill(BLACK)
        state = self.gameState.getGameState()
        if(state == "START"):
            image = pygame.image.load('img/logo.PNG')
            self.surface.blit(image, (60,50))
            image = self.font.render('PRESS   ANY   KEY   TO   START', True, WHITE, BLACK)
            self.surface.blit(image, (175,500))

        elif(state == "MENU"):
            image = pygame.image.load('img/logo.PNG')
            self.surface.blit(image,(60,50))
            cursor = self.gameState.cursor

            if(cursor == 0):
                image = self.font.render('START', True, BLUE, BLACK)
            else:
                image = self.font.render('START', True, WHITE, BLACK)
            self.surface.blit(image,(350,350))

            if(cursor == 1):
                image = self.font.render('HIGH    SCORES', True, BLUE, BLACK)
            else:
                image = self.font.render('HIGH    SCORES', True, WHITE, BLACK)
            self.surface.blit(image,(280,400))

            if(cursor == 2):
                image = self.font.render('CHOSE    LEVEL', True, BLUE, BLACK)
            else:
                image = self.font.render('CHOSE    LEVEL', True, WHITE, BLACK)
            self.surface.blit(image,(280,450))
            if(cursor == 3):
                image = self.font.render('EXIT', True, BLUE, BLACK)
            else:
                image = self.font.render('EXIT', True, WHITE, BLACK)
            self.surface.blit(image,(360,500))

        elif(state == "CHOSE LEVEL"):
            cursor = self.gameState.cursor

            for i in range(8):
                if(cursor == i):
                    image = self.font.render('LEVEL  '+str(i), True, BLUE, BLACK)
                else:
                    image = self.font.render('LEVEL  '+str(i), True, WHITE, BLACK)
                self.surface.blit(image,(350,50+i*50))

        elif(state == "RUNNING"):
            for brick in self.brick:
                img = brick.getImage()
                pos = brick.getPosition()
                self.surface.blit(img, pos)

            for ball in self.ball:
                img = ball.getImage()
                pos = ball.getPosition()
                self.surface.blit(img,pos)

            for bonus in self.bonus:
                img = bonus.getImage()
                pos = bonus.getPosition()
                self.surface.blit(img,pos)

            img = self.pad.getImage()
            pos = self.pad.getPosition()
            self.surface.blit(img,pos)
            img = pygame.image.load('img/heart.png')
            for i in range(self.gameState.lives):
                pos = (17+i*15,580)
                self.surface.blit(img,pos)

            string = "YOUR   SCORE  " + str(self.gameState.score)
            img = self.smallFont.render(string, True, WHITE, BLACK)
            self.surface.blit(img, (800-len(string)*10,575))

            string = "LEVEL  " + str(self.gameState.level)
            img = self.smallFont.render(string, True, WHITE, BLACK)
            self.surface.blit(img, (445-len(string)*10,575))
        elif(state == "PAUSE"):
            image = self.bigFont.render('PAUSE', True, WHITE, BLACK)
            self.surface.blit(image,(240,150))

            image = self.font.render('PRESS   ENTER   TO   EXIT', True, WHITE, BLACK)
            self.surface.blit(image,(205,500))

        elif(state == "HIGH SCORES"):
            try:
                file = open(self.fileName, "r")

            except:
                file = open(self.fileName, "w")
                file.close()
                file = open(self.fileName, "r")

            #file = open(self.fileName,"r")
            image = self.bigFont.render('HIGH   SCORES', True, WHITE, BLACK)
            self.surface.blit(image,(50,15))
            iterator = 0
            for line in file:
                iterator2 = 0
                for word in line.split():
                    image = self.font.render(str(word), True, WHITE, BLACK)

                    if(iterator2 == 0):
                        self.surface.blit(image,(150+iterator2*350,150 + iterator*50))
                    else:
                        lenght = len(str(word))
                        self.surface.blit(image,(650-21.5*lenght,150 + iterator*50))
                    iterator2 += 1

                iterator += 1
                if(iterator >=8):
                    break


        elif(state == "GAME OVER"):
            image = self.bigFont.render('GAME   OVER', True, WHITE, BLACK)
            self.surface.blit(image,(120,150))
            image = self.font.render("PRESS  ANY  KEY", True, WHITE, BLACK)
            self.surface.blit(image,(270,450))

        elif(state == "SAVE SCORE"):
            image = self.font.render('YOUR  NAME', True, WHITE, BLACK)
            self.surface.blit(image,(310,50))
            image = self.font.render(self.gameState.userName, True, WHITE, BLACK)
            lenght = len(self.gameState.userName)
            self.surface.blit(image,(400-10*lenght,250))

        pygame.display.update()
