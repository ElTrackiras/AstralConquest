import pygame
import random
goldCoin = pygame.image.load('Images/Coin-icon.png')


class powerUps:
    powerUpsOnScreen = []
    def __init__(self, x, y):
        self.image = goldCoin
        self.width = 30
        self.height = 30
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = x
        self.y = y
        self.powerUpsOnScreen.append(self)
        self.direction = random.choice(("Right", "Left"))

    def summon(self, screen):
        screen.Gamewindow.blit(self.image, (self.x, self.y))
        self.behaviour(screen)

    def behaviour(self, screen):
        if self.direction == "Right":
            self.x += 1
            if self.x + self.width > screen.ScreenWidth:
                self.direction = "Left"
        elif self.direction == "Left":
            self.x -= 1
            if self.x < 0:
                self.direction = "Right"

