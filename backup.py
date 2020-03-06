    def jump_old2(self,keys):
        if not(self.isJump):
            self.y += self.vel
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if keys[pygame.K_SPACE]:
                self.jumpCount = 10

            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.25 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


    def jump_old(self,keys):
        if not(self.isJump):
            self.y += self.vel
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.25 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10