import pygame


BulletIcon = pygame.image.load('Images/Mics-Bullet-2-icon.png')
BulletIcon = pygame.transform.scale(BulletIcon, (45, 45))
NuclearIcon = pygame.image.load('Images/nuclear.png')
NuclearIcon = pygame.transform.scale(NuclearIcon, (45, 45))
goldCoin = pygame.image.load('Images/Coin-icon.png')
goldCoin = pygame.transform.scale(goldCoin, (40, 40))


class Upgrades:
    clickTimer = 0

    @classmethod
    def display(cls, screen, ship):
        cls.FireRate(screen, ship)
        cls.Bomb(screen, ship)

    l1Opacity = 0
    l2Opacity = 0
    l3Opacity = 0
    @classmethod
    def FireRate(cls, screen, ship):
        screen.blit(BulletIcon, (100, 100))


        l1 = pygame.Surface((60, 40))
        pygame.draw.rect(l1, (55, 1, 255), pygame.Rect(0, 0, 60, 40))
        l1.set_alpha(cls.l1Opacity)

        l2 = pygame.Surface((60, 40))
        pygame.draw.rect(l2, (55, 1, 255), pygame.Rect(0, 0, 60, 40))
        l2.set_alpha(cls.l2Opacity)

        l3 = pygame.Surface((60, 40))
        pygame.draw.rect(l3, (55, 1, 255), pygame.Rect(0, 0, 60, 40))
        l3.set_alpha(cls.l3Opacity)

        screen.blit(l1, (160, 100))
        screen.blit(l2, (220, 100))
        screen.blit(l3, (280, 100))

        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(160, 100, 60, 40), 2)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(220, 100, 60, 40), 2)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(280, 100, 60, 40), 2)

        myfont = pygame.font.SysFont('Monofont', 30)




        mx, my = pygame.mouse.get_pos()
        if mx > 100 and mx < 145:
            if my > 100 and my < 145:
                tooltipAttckspeed = pygame.Surface((350, 50))
                pygame.draw.rect(tooltipAttckspeed, (255, 255, 255), pygame.Rect(0, 0, 400, 50))
                tooltipAttckspeed.set_alpha(150)

                text = myfont.render('Defines the number of your bullets.', 1, (0, 0, 0))

                screen.blit(tooltipAttckspeed, (mx, my))
                screen.blit(text, (mx, my + 13))

        if mx > 350 and mx < 410:
            if my > 100 and my < 140:
                myfont = pygame.font.SysFont('Monofont', 40)
                tooltipAttckspeed = pygame.Surface((100, 50))
                pygame.draw.rect(tooltipAttckspeed, (255, 255, 255), pygame.Rect(0, 0, 400, 50))
                tooltipAttckspeed.set_alpha(150)
                tooltipAttckspeed.blit(goldCoin, (40, 5))

                text = myfont.render('  3', 1, (0, 0, 0))

                screen.blit(tooltipAttckspeed, (mx, my))
                screen.blit(text, (mx, my + 13))



        if ship.firePower > 1:
            cls.l1Opacity = 256

        if ship.firePower > 2:
            cls.l1Opacity = 256
            cls.l2Opacity = 256

        if ship.firePower > 3:
            cls.l1Opacity = 256
            cls.l2Opacity = 256
            cls.l3Opacity = 256


    bomb1Opacity = 0
    bomb2Opacity = 0
    bomb3Opacity = 0
    @classmethod
    def Bomb(cls, screen, ship):
        screen.blit(NuclearIcon, (100, 180))


        l1 = pygame.Surface((60, 40))
        pygame.draw.rect(l1, (55, 1, 255), pygame.Rect(0, 0, 60, 40))
        l1.set_alpha(cls.bomb1Opacity)

        l2 = pygame.Surface((60, 40))
        pygame.draw.rect(l2, (55, 1, 255), pygame.Rect(0, 0, 60, 40))
        l2.set_alpha(cls.bomb2Opacity)

        l3 = pygame.Surface((60, 40))
        pygame.draw.rect(l3, (55, 1, 255), pygame.Rect(0, 0, 60, 40))
        l3.set_alpha(cls.bomb3Opacity)

        screen.blit(l1, (160, 180))
        screen.blit(l2, (220, 180))
        screen.blit(l3, (280, 180))

        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(160, 180, 60, 40), 2)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(220, 180, 60, 40), 2)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(280, 180, 60, 40), 2)

        myfont = pygame.font.SysFont('Monofont', 30)

        mx, my = pygame.mouse.get_pos()
        if mx > 100 and mx < 145:
            if my > 180 and my < 225:
                tooltipAttckspeed = pygame.Surface((250, 50))
                pygame.draw.rect(tooltipAttckspeed, (255, 255, 255), pygame.Rect(0, 0, 400, 50))
                tooltipAttckspeed.set_alpha(150)

                text = myfont.render('Adds number of bombs.', 1, (0, 0, 0))

                screen.blit(tooltipAttckspeed, (mx, my))
                screen.blit(text, (mx, my + 13))

        if mx > 350 and mx < 410:
            if my > 180 and my < 225:
                myfont = pygame.font.SysFont('Monofont', 40)
                tooltipAttckspeed = pygame.Surface((100, 50))
                pygame.draw.rect(tooltipAttckspeed, (255, 255, 255), pygame.Rect(0, 0, 400, 50))
                tooltipAttckspeed.set_alpha(150)
                tooltipAttckspeed.blit(goldCoin, (40, 5))

                text = myfont.render('  4', 1, (0, 0, 0))

                screen.blit(tooltipAttckspeed, (mx, my))
                screen.blit(text, (mx, my + 13))

        if ship.totalBomb > 1:
            cls.bomb1Opacity = 256

        if ship.totalBomb > 2:
            cls.bomb1Opacity = 256
            cls.bomb2Opacity = 256

        if ship.totalBomb > 3:
            cls.bomb1Opacity = 256
            cls.bomb2Opacity = 256
            cls.bomb3Opacity = 256