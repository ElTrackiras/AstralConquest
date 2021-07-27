import pygame
pygame.init()
guideImg = pygame.image.load('Images/Faltar.png')
guideImg = pygame.transform.scale(guideImg, (50, 50))

SpaceBg = pygame.image.load('Images/spaceBG.jpg')
SpaceBg = pygame.transform.scale(SpaceBg, (500, 600))
SpaceBg2 = pygame.image.load('Images/spaceBG.jpg')
SpaceBg2 = pygame.transform.scale(SpaceBg, (500, 600))

Astralimg = pygame.image.load('Images/IntroTitle/Astral.png')
Astralimg = pygame.transform.scale(Astralimg, (300, 130))
TitleImg = [pygame.image.load('Images/IntroTitle/1.png'), pygame.image.load('Images/IntroTitle/2.png'), pygame.image.load('Images/IntroTitle/3.png'), pygame.image.load('Images/IntroTitle/4.png'), pygame.image.load('Images/IntroTitle/5.png'), pygame.image.load('Images/IntroTitle/6.png'), Astralimg]

class IntroWindow:
    color = 0
    currentTitleImg = 0
    TitleCountdownChange = 7
    myfont = pygame.font.SysFont("monospace", 30)
    bgy = 0
    bgy2 = -600
    @classmethod
    def animation(cls, window):
        window.blit(SpaceBg, (0, cls.bgy))
        window.blit(SpaceBg2, (0, cls.bgy2))
        cls.bgy += 1
        cls.bgy2 += 1
        if cls.bgy >= 600:
            cls.bgy = -600
        if cls.bgy2 >= 600:
            cls.bgy2 = -600

        cls.TitleCountdownChange -= 1
        if cls.currentTitleImg > 5:
            cls.currentTitleImg = 0
        window.blit(TitleImg[6], (-10, 90))
        window.blit(TitleImg[cls.currentTitleImg], (0, 160))
        if cls.TitleCountdownChange <= 0:
            cls.currentTitleImg += 1
            cls.TitleCountdownChange = 7

        cls.color += 4
        if cls.color >= 255:
            cls.color = 0

        label3 = cls.myfont.render("(Press Space)", 1, (cls.color, cls.color, cls.color))

        window.blit(label3, (100, 240))
        window.blit(guideImg, (20, 430))
        w = cls.myfont.render("W - Up", 1, (255, 255, 255))
        a = cls.myfont.render("A - Left", 1, (255, 255, 255))
        s = cls.myfont.render("S - Down", 1, (255, 255, 255))
        d = cls.myfont.render("D - Right", 1, (255, 255, 255))
        window.blit(w, (100, 350))
        window.blit(a, (100, 402))
        window.blit(s, (100, 452))
        window.blit(d, (100, 504))
        shootBomb = cls.myfont.render("K - Shoot  L - Bomb", 1, (255, 255, 255))
        window.blit(shootBomb, (24, 550))




    @classmethod
    def runIntro(cls, window):
        cls.animation(window)

