import cmath
import pygame



class Ball():
    def __init__(self,x, y = 540, state = False):
        self.x = x
        self.y = y
        self.fraction = 0.8
        self.velocity = cmath.rect(2.5, cmath.pi)
        self.moveState = state
        self.image = pygame.image.load('img/ball.png')
        self.ballSize = 10


    def getImage(self):
        return self.image

    def colideWithVertical(self, obstaclePosition):
        prevBallXPosition = self.x - self.velocity.real
        distanceToObstacle = obstaclePosition - prevBallXPosition
        if(self.velocity.real > 0):
            #self.x = obstaclePosition - self.ballSize - (self.velocity.real-distanceToObstacle)
            self.x = obstaclePosition -2*self.ballSize -(self.x - obstaclePosition)
            self.xVelocityChange()
        elif(self.velocity.real < 0):
            self.x = obstaclePosition + (-self.velocity.real-distanceToObstacle)
            self.xVelocityChange()


    def colideWithHorizontal(self, obstaclePosition):
        prevBallYPosition = self.y - self.velocity.imag
        distanceToObstacle = obstaclePosition - prevBallYPosition

        if (self.velocity.imag < 0):
            self.y = obstaclePosition - 2*self.ballSize -( self.y - obstaclePosition)
            self.yVelocityChange()
        elif(self.velocity.imag > 0):
            distanceToObstacle = self.y - obstaclePosition
            self.y = obstaclePosition + abs(distanceToObstacle)
            self.yVelocityChange()

    def getBallSize(self):
        return self.ballSize

    def xVelocityChange(self):
        self.velocity = -self.velocity.real+self.velocity.imag*1j

    def yVelocityChange(self):
        self.velocity = self.velocity.real-self.velocity.imag*1j



    def move(self,x, paddleLenght):
        if(self.moveState == True):
            self.x = self.x + self.velocity.real
            self.y = self.y - self.velocity.imag
        else:
            self.x = x + paddleLenght / 2 - self.ballSize/2


    def getVelocity(self):
        return self.velocity

    def collision(self, object):
        return pygame.sprite.collide_rect(self,object)


    def getVelocityAngle(self):
        r, phi = cmath.polar(self.velocity)
        return phi

    def setVelocityAngle(self, newAngle):
        r, phi = cmath.polar(self.velocity)
        self.velocity = cmath.rect(r,newAngle)

    def getMovingState(self):
        return self.moveState

    def getPosition(self):
        return (self.x, self.y)

    def startMoving(self,x,paddleLenght):
        phase = ((x+paddleLenght/2-400)*cmath.pi)/1600
        self.velocity = cmath.rect(2.5,phase+cmath.pi/2)
        self.moveState = True

    def setVelocity(self,v):
        r, phi = cmath.polar(self.velocity)
        self.velocity = cmath.rect(v,phi)
