import pygame


class Brick:
    def __init__(self, type, xpos, ypos):
        self.type = type
        self.xpos = xpos
        self.ypos = ypos
        self.lenght = 50
        self.width = 30
        self.scoreValue = 0

        if(self.type == "WHITE"):
            self.image = pygame.image.load('img/brick/white_brick.png')
            self.lives = 1
            self.scoreValue = 50
        if(self.type == "ORANGE"):
            self.image = pygame.image.load('img/brick/orange_brick.png')
            self.lives = 1
            self.scoreValue = 60
        if(self.type == "BLUE"):
            self.image = pygame.image.load('img/brick/blue_brick.png')
            self.lives = 1
            self.scoreValue = 70
        elif(self.type == "GREEN"):
            self.image = pygame.image.load('img/brick/green_brick.png')
            self.lives = 1
            self.scoreValue = 80
        if(self.type == "RED"):
            self.image = pygame.image.load('img/brick/red_brick.png')
            self.lives = 1
            self.scoreValue = 90
        if(self.type == "DARK_BLUE"):
            self.image = pygame.image.load('img/brick/darkblue_brick.png')
            self.lives = 1
            self.scoreValue = 100
        if(self.type == "PURPLE"):
            self.image = pygame.image.load('img/brick/purple_brick.png')
            self.lives = 1
            self.scoreValue = 110
        if(self.type == "YELLOW"):
            self.image = pygame.image.load('img/brick/yellow_brick.png')
            self.lives = 1
            self.scoreValue = 120
        if(self.type == "SILVER"):
            self.image = pygame.image.load('img/brick/silver_brick.png')
            self.lives = 2
            self.scoreValue = 250
        elif(self.type == "GOLD"):
            self.image = pygame.image.load('img/brick/gold_brick.png')
            self.lives = 5
            self.scoreValue = 500

    def getLives(self):
        return self.lives

    def reduceLives(self):
        self.lives -= 1
        if(self.type == "DIAMOND" and self.lives == 2):
            self.image = pygame.image.load('diamond_brick_cracked.png')

    def getType(self):
        return self.type

    def getPosition(self):
        return (self.xpos,self.ypos)

    def getImage(self):
        return self.image

    def getLenght(self):
        return self.lenght

    def getWidth(self):
        return self.width
