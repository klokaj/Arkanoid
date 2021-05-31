import sys
sys.path.append('src/')


import pygame, sys, math, cmath
from pygame.locals import *
import numpy as np
import ball
from ball import Ball
from pad import Pad
from bonus import Bonus
import random
from Brick import Brick
from drawer import drawer
import levels

MAX_LVL_NUMBER = 8

FPS = 200
X_SIZE = 800
Y_SIZE = 600
START_MAP = 0





class gameState():
    def __init__(self):
        self.state = "START"
        self.score = 0
        self.lives = 3
        self.startTime = 0
        self.cursor = 0
        self.level = START_MAP
        self.userName = ""
    def getGameState(self):
        return self.state

    def changeGameState(self, newState):
        self.state = newState

    def addPoints(self, x):
        self.points += x

    def addLive(self):
        self.lives += 1

    def removeLive(self):
        self.lives -= 1

    def reset(self):
        self.points = 0
        self.lives = 3
        self.startTime = 0
        self.cursor = 0
        #self.level = START_MAP
        self.score = 0


class Arkanoid:
    def __init__(self):
        self.balls = []
        self.pad = Pad()
        self.bricks = []
        self.createMap(2)
        self.bonus = []
        self.cursor = 0
        self.gameState = gameState()
        self.pressed = 0
        self.keydown = False
        self.drawer = drawer(self.balls,self.pad, self.bricks, self.bonus,  self.gameState, X_SIZE, Y_SIZE, "results.txt")
        self.fpsClock = pygame.time.Clock()



    def mainLoop(self):
        while (self.gameState.state != "QUIT"):
            self.fpsClock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif(event.type == KEYDOWN):
                    self.pressed = pygame.key.get_pressed()
                    self.keydown = True
            self.updateState()
            pressed = self.pressed
            self.drawer.draw()


            if(self.gameState.state == "RUNNING"):
                if(pressed[K_SPACE] and self.keydown):
                    self.startMoving()

                if(len(self.balls) == 0 and self.gameState.lives > 0):
                    self.gameState.lives -= 1
                    self.balls.append(Ball(self.pad.getPosition()[0]))
                self.moveBall()
                self.moveBonus()
                self.pressed = pygame.key.get_pressed()
                if self.pressed[K_LEFT]:
                    self.pad.moveLeft()
                elif self.pressed[K_RIGHT]:
                    self.pad.moveRight()
            elif(self.gameState.state == "MENU" and self.keydown):
                if (pressed[K_DOWN]):
                    self.gameState.cursor = (self.gameState.cursor+1)%4
                elif(pressed[K_UP]):
                    self.gameState.cursor = (self.gameState.cursor-1)%4
            elif(self.gameState.state == "CHOSE LEVEL" and self.keydown):
                if (pressed[K_DOWN]):
                    self.gameState.cursor = (self.gameState.cursor+1)%9
                elif(pressed[K_UP]):
                    self.gameState.cursor = (self.gameState.cursor-1)%9
            elif(self.gameState.state == "QUIT"):
                    pygame.quit()
                    sys.exit()

            elif(self.gameState.state == "NEW LEVEL"):
                del self.balls[:]
                del self.bonus[:]
                self.pad.reset()
                self.gameState.level +=1
                self.createMap(self.gameState.level % MAX_LVL_NUMBER)
                self.addBall()
                for ball in self.balls:
                    ball.setVelocity(self.gameState.level*0.5+2)
            elif(self.gameState.state == "NEW_GAME"):
                self.resetGame()
                self.createMap(self.gameState.level)
                self.addBall()
            elif(self.gameState.state == "SAVE SCORE" and self.keydown):
                if(pressed[K_BACKSPACE]):
                    self.gameState.userName = self.gameState.userName[:-1]
                elif(len(self.gameState.userName) <= 10):
                    if(pressed[K_0]):
                        self.gameState.userName += '0'
                    elif(pressed[K_1]):
                        self.gameState.userName += '1'
                    elif(pressed[K_2]):
                        self.gameState.userName += '2'
                    elif(pressed[K_3]):
                        self.gameState.userName += '3'
                    elif(pressed[K_4]):
                        self.gameState.userName += '4'
                    elif(pressed[K_5]):
                        self.gameState.userName += '5'
                    elif(pressed[K_6]):
                        self.gameState.userName += '6'
                    elif(pressed[K_7]):
                        self.gameState.userName += '7'
                    elif(pressed[K_8]):
                        self.gameState.userName += '8'
                    elif(pressed[K_9]):
                        self.gameState.userName += '9'
                    elif(pressed[K_a]):
                        self.gameState.userName += 'a'
                    elif(pressed[K_b]):
                        self.gameState.userName += 'b'
                    elif(pressed[K_c]):
                        self.gameState.userName += 'c'
                    elif(pressed[K_d]):
                        self.gameState.userName += 'd'
                    elif(pressed[K_e]):
                        self.gameState.userName += 'e'
                    elif(pressed[K_f]):
                        self.gameState.userName += 'f'
                    elif(pressed[K_g]):
                        self.gameState.userName += 'g'
                    elif(pressed[K_h]):
                        self.gameState.userName += 'h'
                    elif(pressed[K_i]):
                        self.gameState.userName += 'i'
                    elif(pressed[K_j]):
                        self.gameState.userName += 'j'
                    elif(pressed[K_k]):
                        self.gameState.userName += 'k'
                    elif(pressed[K_l]):
                        self.gameState.userName += 'l'
                    elif(pressed[K_m]):
                        self.gameState.userName += 'm'
                    elif(pressed[K_n]):
                        self.gameState.userName += 'n'
                    elif(pressed[K_o]):
                        self.gameState.userName += 'o'
                    elif(pressed[K_p]):
                        self.gameState.userName += 'p'
                    elif(pressed[K_q]):
                        self.gameState.userName += 'q'
                    elif(pressed[K_r]):
                        self.gameState.userName += 'r'
                    elif(pressed[K_s]):
                        self.gameState.userName += 's'
                    elif(pressed[K_t]):
                        self.gameState.userName += 't'
                    elif(pressed[K_u]):
                        self.gameState.userName += 'u'
                    elif(pressed[K_v]):
                        self.gameState.userName += 'v'
                    elif(pressed[K_w]):
                        self.gameState.userName += 'w'
                    elif(pressed[K_x]):
                        self.gameState.userName += 'x'
                    elif(pressed[K_y]):
                        self.gameState.userName += 'y'
                    elif(pressed[K_z]):
                        self.gameState.userName += 'z'
            elif(self.gameState.state == "SAVE"):
                self.saveScore()

            self.keydown = False

    def updateState(self):
        state = self.gameState.state
        newState = state
        pressed = self.pressed
        if(state=="START" and self.keydown == True):
                newState = "MENU"
        elif(state == "MENU" and self.keydown == True):
            if(pressed[K_RETURN]):
                if(self.gameState.cursor == 0):
                    newState = "NEW_GAME"
                if(self.gameState.cursor == 1):
                    newState = "HIGH SCORES"
                if(self.gameState.cursor == 2):
                    newState = "CHOSE LEVEL"
                    self.gameState.cursor = 0
                if(self.gameState.cursor == 3):
                    newState = "QUIT"
        elif(state == "HIGH SCORES" and self.keydown):
            if(pressed[K_ESCAPE]):
                newState = "MENU"
                self.gameState.cursor = 0
            elif(pressed[K_RETURN]):
                self.gameState.level = self.gameState.cursor
                newState = "MENU"
                self.gameState.cursor = 0

        elif(state == "CHOSE LEVEL" and self.keydown):
            if(pressed[K_ESCAPE]):
                newState = "MENU"
                self.gameState.cursor = 0
            elif(pressed[K_RETURN]):
                self.gameState.level = self.gameState.cursor
                self.gameState.cursor = 0
                newState = "MENU"
        elif(state == "NEW_GAME"):
            newState = "RUNNING"
        elif(state == "RUNNING"):
            if(self.gameState.lives <= 0):
                newState = "GAME OVER"
            elif(pressed[K_ESCAPE] and self.keydown):
                newState = "PAUSE"
            elif(pressed[K_RETURN] and self.keydown):
                newState = "RUNNING"
            elif(pressed[K_0] and self.keydown):
                self.multipleBalls()
           # elif(pressed[K_SPACE] and self.keydown):
            #    self.startMoving()

            if(len(self.bricks) == 0):
                newState = "NEW LEVEL"
        elif(state == "NEW LEVEL"):
            newState = "RUNNING"
        elif(state ==  "PAUSE" and self.keydown):
            if(pressed[K_RETURN]):
                newState = "MENU"
            elif(pressed[K_ESCAPE]):
                newState = "RUNNING"

        elif(state == "GAME OVER" and self.keydown):
            newState = "SAVE SCORE"

        elif(state == "SAVE SCORE" and self.keydown):
            if(pressed[K_ESCAPE]):
                newState = "MENU"
            elif(pressed[K_RETURN]):
                newState = "SAVE"
        elif(state == "SAVE"):
            newState = "MENU"

        self.gameState.state = newState


    def resetGame(self):
        del self.balls[:]
        del self.bricks[:]
        del self.bonus[:]
        self.pad.reset()
        self.gameState.reset()

    def addBall(self):
        self.balls.append(Ball(self.pad.getPosition()[0]))

    def moveBall(self):
        for ball in self.balls:
            ballSize = ball.ballSize
            ballPrevPos = (ball.x, ball.y)
            ball.move(self.pad.xPos,self.pad.lenght)

            ballPos = (ball.x, ball.y)

            #-----------------collide with ball---------------------------------
            if(ballPos[0] >= X_SIZE- 1 - ballSize):
                ball.colideWithVertical(X_SIZE-1)
            elif(ballPos[0] <= 0):
                ball.colideWithVertical(0)

            if(ballPos[1]+ballSize > self.pad.yPos and ballPos[1] <= self.pad.yPos+ballSize/2):
                if(ballPos[0] >= self.pad.xPos-ballSize/2 and ballPos[0] <= self.pad.xPos+self.pad.getLenght()-ballSize/2):
                    ball.colideWithHorizontal(self.pad.getPosition()[1])
                    r, phi = cmath.polar(ball.velocity)
                    dis = -ballPos[0] + self.pad.xPos-ballSize/2
                    dis = (dis+self.pad.lenght/2)/(self.pad.lenght/2)
                    angle = dis*cmath.pi/3 + phi
                    if(angle < cmath.pi/6):
                        angle = cmath.pi/6
                    elif( angle > cmath.pi - cmath.pi/6):
                        angle = cmath.pi - cmath.pi/6
                    ball.velocity = cmath.rect(r,angle)


            if(ballPos[1] <0 ):
                ball.yVelocityChange()
            elif(ballPos[1] > Y_SIZE):
                self.balls.pop(self.balls.index((ball)))

            s = False
            #-----------------collide with bricks---------------------------------
            for brick in self.bricks:
                brickPos = brick.getPosition()
                brickLenght = brick.getLenght()
                brickWidth  = brick.getWidth()
                #
                ballPos = ball.getPosition()

                if(( ballPos[0] <= brickPos[0] + brickLenght) and (ballPos[0] >= brickPos[0]- ballSize)
                     and (ballPos[1] <= brickPos[1]+brickWidth) and ballPos[1] >= brickPos[1]-ballSize):

                    if(ballPrevPos[0] < brickPos[0] - ballSize):
                        ball.colideWithVertical(brickPos[0])
                        brick.reduceLives()
                        s = True

                    elif(ballPrevPos[0] > brickPos[0] + brickLenght):
                        ball.colideWithVertical(brickPos[0]+brickLenght)
                        brick.reduceLives()
                        s = True

                    elif(ballPrevPos[1] > brickPos[1] + brickWidth):
                        ball.colideWithHorizontal(brickPos[1]+brickWidth)
                        brick.reduceLives()
                        s = True


                    elif(ballPrevPos[1] < brickPos[1] - ballSize):
                        ball.colideWithHorizontal(brickPos[1])
                        brick.reduceLives()
                        s = True

                    ## generate bonus
                    if(brick.lives <= 0):
                        self.gameState.score += brick.scoreValue
                        self.removeBrick(self.bricks.index((brick)))
                        random.seed()
                        randNumber = random.randrange(10)
                        if(randNumber == 1):
                            self.bonus.append(Bonus(brickPos[0],brickPos[1]))

                    if(s):
                        break
    def saveScore(self):
        file = open("results.txt","r")
        score = []
        name = []
        for line in file:
            i = 0
            for word in line.split():
                if(i == 0):
                    name.append(word)
                else:
                    score.append(int(word))

                i = (i+1)%2
        score.append(self.gameState.score)
        name.append(self.gameState.userName)

        swaped = True
        while(swaped == True):
            swaped = False
            for k in range(0,len(score)-1):
                if(score[k]<score[k+1]):
                    score[k], score[k+1] = score[k+1], score[k]
                    name[k], name[k+1] = name[k+1], name[k]
                    swaped = True

        file.close()

        file = open("results.txt","w")
        while(len(name)>8):
            name = name[:-1]
            score = score[:-1]
        iterator = 0
        for elem in name:
            s = elem + " " +str(int(score[iterator])) + '\n'
            file.write(s)
            iterator +=1

        file.close()



    def moveBonus(self):
        for bonus in self.bonus:
            bonus.move()
            bonusPos= bonus.getPosition()
            paddlePos  = self.pad.getPosition()
            paddleLenght = self.pad.getLenght()
            bonusSize = bonus.size
            if(bonus.getState() == "Active" and bonusPos[1]+bonusSize >= paddlePos[1] and bonusPos[0] + bonusSize >= paddlePos[0]
                    and bonusPos[0] <= paddlePos[0] + paddleLenght):

                if(bonus.type == "HEART"):
                    self.gameState.lives +=1
                elif(bonus.type == "BALL_BONUS"):
                    self.multipleBalls()
                elif(bonus.type == "BALL_SPEEDUP"):
                    for ball in self.balls:
                        r, phi = cmath.polar(ball.velocity)
                        ball.setVelocity(r + 0.5)
                elif(bonus.type == "BALL_SPEEDDOWN"):
                    for ball in self.balls:
                        r, phi = cmath.polar(ball.velocity)
                        v = r - 0.5
                        if(v <= 1):
                            v = 1
                        ball.setVelocity(v)
                elif(bonus.type == "PADDLE_SPEEDUP"):
                    self.pad.increaseSpeed()
                elif(bonus.type == "PADDLE_SPEEDDOWN"):
                    self.pad.decreaseSpeed()
                elif(bonus.type == "PADDLE_UP"):
                    self.pad.up()
                elif(bonus.type == "PADDLE_DOWN"):
                    self.pad.down()

                self.bonus.pop(self.bonus.index((bonus)))


            if(bonus.getPosition()[1] >= 600):
                self.bonus.pop(self.bonus.index((bonus)))

    def startMoving(self):
        for ball in self.balls:
            if(ball.moveState == False):
                ball.startMoving(self.pad.xPos, self.pad.lenght)

    def multipleBall(self, ball):
        #ball = self.balls[0]
        v = ball.getVelocity()
        angle = cmath.phase(v)
        pos = ball.getPosition()
        self.balls.append(Ball(pos[0],pos[1],True))
        self.balls[len(self.balls)-1].setVelocityAngle(angle + 0.2618 )
        self.balls.append(Ball(pos[0],pos[1],True))
        self.balls[len(self.balls)-1].setVelocityAngle(angle - 0.2618 )

    def multipleBalls(self):
        balls = self.balls.copy()

        for ball in balls:
            self.multipleBall(ball)

    def addBrick(self,type,x,y):
        self.bricks.append(Brick(type,x,y))

    def removeBrick(self,brick):
        self.bricks.pop(brick)

    def createMap(self,levelNumber):
        elem_iterator = 0
        row_iterator = 0
        levelNumber = levelNumber%MAX_LVL_NUMBER

        MAP = []
        if(levelNumber == 0 ):
            MAP = levels.map_0
        elif(levelNumber == 1):
            MAP = levels.map_1
        elif(levelNumber == 2):
            MAP = levels.map_2
        elif(levelNumber == 3):
            MAP = levels.map_3
        elif(levelNumber == 4):
            MAP = levels.map_4
        elif(levelNumber == 5):
            MAP = levels.map_5
        elif(levelNumber == 6):
            MAP = levels.map_6
        elif(levelNumber == 7):
            MAP = levels.map_7
        else:
            MAP = levels.map_0

        for row in MAP:
            for elem in row:
                if(elem == 1):
                    self.bricks.append(Brick("WHITE",elem_iterator*50,row_iterator*30))
                elif(elem == 2):
                    self.bricks.append(Brick("ORANGE",elem_iterator*50,row_iterator*30))
                elif(elem == 3):
                    self.bricks.append(Brick("BLUE",elem_iterator*50,row_iterator*30))
                elif(elem == 4):
                    self.bricks.append(Brick("GREEN",elem_iterator*50,row_iterator*30))
                elif(elem == 5):
                    self.bricks.append(Brick("RED",elem_iterator*50,row_iterator*30))
                elif(elem == 6):
                    self.bricks.append(Brick("DARK_BLUE",elem_iterator*50,row_iterator*30))
                elif(elem == 7):
                    self.bricks.append(Brick("PURPLE",elem_iterator*50,row_iterator*30))
                elif(elem == 8):
                    self.bricks.append(Brick("YELLOW",elem_iterator*50,row_iterator*30))
                elif(elem == 9):
                    self.bricks.append(Brick("SILVER",elem_iterator*50,row_iterator*30))
                elif(elem == 10):
                    self.bricks.append(Brick("GOLD",elem_iterator*50,row_iterator*30))

                elem_iterator +=1
            elem_iterator = 0
            row_iterator += 1












