#!/usr/bin/env python3

import random
import pygame
from bird import Bird
from pipe import Pipe


class MainLoop:
    """
    The game consists of three State:\n
    1. Ready\n
    2. Running\n
    3. End\n
    They appear in sequence
    """
    def __init__(self):
        random.seed()
        pygame.display.set_caption("Flippy Bird")
        # window size & FPS
        self.win_width = 288
        self.win_height = 512
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.clock = pygame.time.Clock()
        # game object
        self.bird = Bird()
        self.pipes = [Pipe(),Pipe()]
        self.pipes[0].randInit()
        self.pipes[1].randInit()
        self.pipes[1].x = 288 + 144
        # score
        self.score = 0
        # resourses
        self.bg_day = pygame.image.load('src/bg_day.png')
        

        
    def reInit(self):
        random.seed()
        pygame.display.set_caption("Flippy Bird")
        # window size & FPS
        self.win_width = 288
        self.win_height = 512
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.clock = pygame.time.Clock()
        # game object
        self.bird = Bird()
        self.pipes = [Pipe(),Pipe()]
        self.pipes[0].randInit()
        self.pipes[1].randInit()
        self.pipes[1].x = 288 + 170
        self.score = 0

    # refresh window
    def redrawGameWindow(self):
        # show background
        self.win.blit(self.bg_day,(0,0))
        self.bird.draw(self.win)
        self.pipes[0].draw(self.win)
        self.pipes[1].draw(self.win)
        # show parameters
        font = pygame.font.SysFont(None, 20)
        font_x = 5
        font_y = 5
        for (k,v) in self.getParameters().items():
            text = font.render("%s:%s"%(k,v), True, (255, 255, 255))
            self.win.blit(text,(font_x, font_y))
            font_y += text.get_height()
        # show score
        font = pygame.font.SysFont(None, 50)
        text = font.render(str(self.score),True,(255,255,255))
        self.win.blit(text,(130,100))
        pygame.display.update()

    def collisionDetection(self):
        """
        Return true when collsion happens
        """
        bird = self.bird
        if bird.y<=0 or bird.y>=self.win_height:
            return True
        for pipe in self.pipes:
            if bird.x+bird.pic_width>=pipe.x and bird.x<=pipe.x+pipe.pic_width:
                if bird.y<=pipe.upper_bound or bird.y+bird.pic_height>=pipe.lower_bound:
                    return True
        return False
    
    def gameController(self):
        run = True
        while run:
            self.reInit()
            self.readyState()
            self.runningState()
            if not(self.endState()):
                run = False

    def updateScore(self):
        for p in self.pipes:
            if p.x == 18:
                self.score += 1

    def readyState(self):
        pass

    # mainloop
    def runningState(self):
        run = True
        while run:
            self.clock.tick(30)
            
            # loop through all the event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # get all the pressed keys
            keys = pygame.key.get_pressed()
            self.bird.move(keys)
            self.pipes[0].move()
            self.pipes[1].move()
            if self.collisionDetection():
                run = False
            self.updateScore()
            self.redrawGameWindow()
        
        self.endState()

        
    def endState(self):
        isopen = True
        while isopen:
            self.clock.tick(30)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                isopen = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
        return True

    def getParameters(self):
        """
        Return all the parameters of bird and pipe in a dictionary so as to train the Network
        """
        d = {}
        d['bird_x'] = self.bird.x
        d['bird_y'] = self.bird.y
        d['pipe0_x'] = self.pipes[0].x
        d['pipe0_upper'] = self.pipes[0].upper_bound
        d['pipe0_lower'] = self.pipes[0].lower_bound
        d['pipe1_x'] = self.pipes[1].x
        d['pipe1_upper'] = self.pipes[1].upper_bound
        d['pipe1_lower'] = self.pipes[1].lower_bound
        d['score'] = self.score
        return d

def main():
    pygame.init()
    pygame.font.init()
    mainloop = MainLoop()
    mainloop.gameController()


if __name__ == '__main__':
    main()