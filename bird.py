import pygame
bird0_pic = [pygame.image.load('src/bird0_0.png'),pygame.image.load('src/bird0_1.png'),pygame.image.load('src/bird0_2.png')]

class Bird(object):
    def __init__(self,x=50,y=50,width=64,height=64,win_width = 288):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0
        self.isJump = False
        self.jumpCount = 10
        self.g = 3
        self.jumpInterval = 1

        self.pic_width = 24
        self.pic_height = 24

    def move(self,keys):
        self.vel += self.g
        if self.vel > 25:
            self.vel = 25
        if self.jumpInterval>0:
            self.jumpInterval -= 1
        
        if keys[pygame.K_SPACE] and self.jumpInterval<=0:
            self.jumpInterval = 3
            self.vel = -20
        
        self.y += self.vel
        if self.y > 512:
            self.y = 0
        

    def draw(self,win):
        # draw bird
        if self.vel >= 1:
            pic = bird0_pic[0]
        elif self.vel <= -1:
            pic = bird0_pic[2]
        else:
            pic = bird0_pic[1]
        win.blit(pic,(self.x,self.y))

        