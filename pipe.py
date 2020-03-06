import pygame
import random
# Generate Pipes

pipe_pic = [pygame.image.load('src/pipe_down.png'),pygame.image.load('src/pipe_up.png')]

class Pipe:
    def __init__(self):
        self.x = 200
        self.upper_bound = 30       # upper boundary of the gap
        self.lower_bound = 50       # lower boundary of the gap
        self.gap_height = 150       
        self.vel = -5
        self.pic_width = 52

    def move(self):
        """the pipe move right a little every frame"""
        self.x += self.vel
        if self.x < -60: 
            self.randInit()

    def randInit(self):
        """
        Regenerate a new Pipe start from the right edge\n
        A Pipe object actually consists of a pair of pipe's images
        and leaves a gap where the bird can path through
        """
        self.x = 288
        self.upper_bound = random.randint(140,320)
        self.lower_bound = self.upper_bound + self.gap_height
    
    def draw(self,win):
        """
        Creat the combined image based on the gap
        """
        # cut picture
        win.blit(pipe_pic[0],(self.x,self.upper_bound-310))
        win.blit(pipe_pic[1],(self.x,self.lower_bound))
