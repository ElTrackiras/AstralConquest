import pygame
import random
import Intro
import PowerUps
from pygame import mixer
import Buttons
import UpgradeScreen
import math
pygame.init()

mixer.init()


""" All ships photos are here"""
ShipOne = pygame.image.load('Images/Falcon.png')
ShipFlips = [pygame.transform.flip(ShipOne, False, True), pygame.transform.rotate(ShipOne, 90), pygame.transform.rotate(ShipOne, 270)]
ShipDiscBossImg = pygame.image.load('Images/ShipDiscBoss.png')
ShipDiscBossImg = pygame.transform.flip(ShipDiscBossImg, False, True)
BlueStopperImage = pygame.image.load('Images/BlueStopper.png')
BlueStopperImgList = [pygame.transform.flip(BlueStopperImage, False, True)]
SpaceBg = pygame.image.load('Images/spaceBG.jpg')
SpaceBg = pygame.transform.scale(SpaceBg, (500, 600))
SpaceBg2 = pygame.image.load('Images/spaceBG.jpg')
SpaceBg2 = pygame.transform.scale(SpaceBg, (500, 600))
HitImg = pygame.image.load('Images/target.png')
HitImg = pygame.transform.scale(HitImg, (40, 40))
LaserBullet = pygame.image.load('Images/LaserShot.png')
GoldStack = pygame.image.load('Images/Money-icon.png')
Faltar = pygame.image.load('Images/Faltar.png')
Bluekle = pygame.image.load('Images/Bluekle.png')
Bluekle = pygame.transform.flip(Bluekle, False, True)
GreenJumperImg = pygame.image.load('Images/GreenJumper.png')
PoisonPlanet = pygame.image.load('Images/PoisonPlanet.png')
FieryPlanet = pygame.image.load('Images/FieryPlanet.png')
EarthPlanet = pygame.image.load('Images/EarthPlanet.png')
explosion1 = pygame.image.load('Images/explosion-1.png')
explosion2 = pygame.image.load('Images/explosion-2.png')
button = pygame.image.load('Images/button.png')
buttonGlow = pygame.image.load('Images/buttonGlow.png')
PurpleCircle = pygame.image.load('Images/PurpleCircle.png')
PurpleCircle = pygame.transform.rotate(PurpleCircle, 90)

""" ----------------------------------------- """

# The class for all the screen.
class Screen:
    ScreenWidth = 500
    ScreenHeight = 600
    Gamewindow = pygame.display.set_mode((ScreenWidth, ScreenHeight))
    FPS = pygame.time.Clock()
    currentScreen = 'IntroScreen'
    gameRun = True
    bgYscroll = 0
    bgYscroll2 = 0 - ScreenHeight
    clickTimer = 0

    @classmethod
    def musicControl(cls):
        # The music here is something I cannot understand logically. The music meant for intro screen plays on the next screen insteas. Thus, I played corresponding music beforehand to match the expectation
        if cls.currentScreen == 'IntroScreen':
            mixer.music.load("BattleMusic.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play(loops=-1)
        elif cls.currentScreen == 'GameOver':
            mixer.music.stop()

# This is where all the functions for the buttons are withheld.
    @classmethod
    def StartGameFunc(cls):
        cls.currentScreen = 'MissionControl'

    @classmethod
    def Stage1Start(cls):
        cls.currentScreen = 'BattleScreen'
        GameFlowControl.currentStage = 1

    @classmethod
    def Stage2Start(cls):
        cls.currentScreen = 'BattleScreen'
        GameFlowControl.currentStage = 2

    @classmethod
    def Stage3Start(cls):
        cls.currentScreen = 'BattleScreen'
        GameFlowControl.currentStage = 3

    @classmethod
    def Stage4Start(cls):
        cls.currentScreen = 'BattleScreen'
        GameFlowControl.currentStage = 4

    @classmethod
    def Stage5Start(cls):
        cls.currentScreen = 'BattleScreen'
        GameFlowControl.currentStage = 5

    @classmethod
    def UpgradeFunc(cls):
        cls.currentScreen = 'UpgradeScreen'

    @classmethod
    def GoBackFunc(cls):
        cls.currentScreen = 'MenuScreen'

    @classmethod
    def QuitFunc(cls):
        pygame.quit()

    @classmethod
    def AddPowerRate(cls):
        if cls.clickTimer <= 0:


            if Falcon.firePower < 4:
                if Falcon.gold >= 3:
                    print('FireRateAdded')
                    Falcon.firePower += 1
                    Falcon.gold -= 3
                else:
                    print('Insufficient Gold.')
            else:
                print('Firing rate already maxed out.')
        cls.clickTimer = 10

    @classmethod
    def AddBomb(cls):
        if cls.clickTimer <= 0:


            if Falcon.totalBomb < 4:
                if Falcon.gold >= 4:
                    print('BombAdded')
                    Falcon.totalBomb += 1
                    Falcon.gold -= 4
                else:
                    print('Insufficient Gold.')
            else:
                print('Bomb already maxed out.')
        cls.clickTimer = 10
# Marks the end of the button's functions.



    @classmethod
    def GameLoop(cls):
        while cls.gameRun:
            cls.musicControl()
            cls.FPS.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cls.gameRun = False

            if cls.currentScreen == 'IntroScreen':
                Intro.IntroWindow.runIntro(cls.Gamewindow)
                myfont = pygame.font.SysFont('Monofont', 30)
                highScore = myfont.render('Highest Score: ' + str(GameFlowControl.HighestScore), 1, (255, 255, 255))
                cls.Gamewindow.blit(highScore, (10, 10))
                Keys = pygame.key.get_pressed()
                if Keys[pygame.K_SPACE]:
                    cls.currentScreen = 'MenuScreen'

            elif cls.currentScreen == 'MissionControl':
                cls.Gamewindow.blit(SpaceBg, (0, 0))

                myfont = pygame.font.SysFont('Monofont', 30)

                Back = Buttons.Button(x=380, y=10, width=100, height=30, fontSize=15, text='Back', image=button, image2=buttonGlow, leftTextPadding=35, topTextPadding=8)
                Back.Place(cls.Gamewindow, cls.GoBackFunc)


                Stage1 = Buttons.Button(50, 450, 100, 100, (255, 255, 255), text='', image=PoisonPlanet)
                Stage1.Place(cls.Gamewindow, cls.Stage1Start)
                Stage1txt = myfont.render('Stage 1', 1, (255, 255, 255))
                cls.Gamewindow.blit(Stage1txt, (65, 440))

                if GameFlowControl.stagesCleared > 0:
                    Stage2 = Buttons.Button(350, 350, 100, 100, (255, 255, 255), text='', image=FieryPlanet)
                    Stage2.Place(cls.Gamewindow, cls.Stage2Start)
                    Stage2txt = myfont.render('Stage 2', 1, (255, 255, 255))
                    cls.Gamewindow.blit(Stage2txt, (365, 340))

                if GameFlowControl.stagesCleared > 1:
                    Stage3 = Buttons.Button(70, 250, 100, 100, (255, 255, 255), text='', image=EarthPlanet)
                    Stage3.Place(cls.Gamewindow, cls.Stage3Start)
                    Stage3txt = myfont.render('Stage 3', 1, (255, 255, 255))
                    cls.Gamewindow.blit(Stage3txt, (85, 240))

                if GameFlowControl.stagesCleared > 2:
                    Stage4 = Buttons.Button(330, 170, 100, 100, (255, 255, 255), text='', image=EarthPlanet)
                    Stage4.Place(cls.Gamewindow, cls.Stage4Start)
                    Stage4txt = myfont.render('Stage 4', 1, (255, 255, 255))
                    cls.Gamewindow.blit(Stage4txt, (345, 160))

                if GameFlowControl.stagesCleared > 3:
                    Stage5 = Buttons.Button(10, 50, 100, 100, (255, 255, 255), text='', image=EarthPlanet)
                    Stage5.Place(cls.Gamewindow, cls.Stage5Start)
                    Stage5txt = myfont.render('Stage 5', 1, (255, 255, 255))
                    cls.Gamewindow.blit(Stage5txt, (25, 40))

            elif cls.currentScreen == 'MenuScreen':
                cls.Gamewindow.blit(SpaceBg, (0, cls.bgYscroll))
                cls.Gamewindow.blit(SpaceBg2, (0, cls.bgYscroll2))
                cls.bgYscroll += 0.5
                cls.bgYscroll2 += 0.5
                if cls.bgYscroll > cls.ScreenHeight:
                    cls.bgYscroll = 0 - cls.ScreenHeight
                if cls.bgYscroll2 > cls.ScreenHeight:
                    cls.bgYscroll2 = 0 - cls.ScreenHeight
                bwidth = 200
                bheight = 50
                Start = Buttons.Button((cls.ScreenWidth/2) - bwidth/2, 50, bwidth, bheight, (255, 255, 255), text='Start', textColor=(37, 23, 23), image=button, image2=buttonGlow, leftTextPadding= 66, topTextPadding=8)
                Upgrade = Buttons.Button((cls.ScreenWidth / 2) - bwidth / 2, 150, bwidth, bheight, (255, 255, 255), text='Upgrades', image=button, image2=buttonGlow, leftTextPadding= 40, topTextPadding=8)
                Quit = Buttons.Button((cls.ScreenWidth / 2) - 150 / 2, 250, 150, bheight, (255, 255, 255), text='Quit', image=button, image2=buttonGlow, leftTextPadding= 40, topTextPadding=8)
                Start.Place(cls.Gamewindow, cls.StartGameFunc)
                Upgrade.Place(cls.Gamewindow, cls.UpgradeFunc)
                Quit.Place(cls.Gamewindow, cls.QuitFunc)

            elif cls.currentScreen == 'UpgradeScreen':
                cls.Gamewindow.blit(SpaceBg, (0, 0))
                GoBack = Buttons.Button(x=10, y=10, width=100, height=30, fontSize=15, text='Back', image=button, image2=buttonGlow, leftTextPadding=35, topTextPadding=8)
                GoBack.Place(cls.Gamewindow, cls.GoBackFunc)
                myfont = pygame.font.SysFont("monospace", 40)
                gold = myfont.render('Gold: ' + str(Falcon.gold), 1, (255, 255, 0))
                cls.Gamewindow.blit(gold, (200, 10))

                cls.clickTimer -= 1
                add = Buttons.Button(x=350, y=100, width=60, height=40, text='+', color=(255, 255, 0))
                add.Place(cls.Gamewindow, cls.AddPowerRate)

                add = Buttons.Button(x=350, y=180, width=60, height=40, text='+', color=(255, 255, 0))
                add.Place(cls.Gamewindow, cls.AddBomb)
                Falcon.bomb = Falcon.totalBomb

                UpgradeScreen.Upgrades.display(cls.Gamewindow, Falcon)
                cls.Gamewindow.blit(GoldStack, (165, 15))

            elif cls.currentScreen == 'BattleScreen':
                    cls.Gamewindow.blit(SpaceBg, (0, cls.bgYscroll))
                    cls.Gamewindow.blit(SpaceBg2, (0, cls.bgYscroll2))
                    cls.bgYscroll += 0.5
                    cls.bgYscroll2 += 0.5
                    if cls.bgYscroll > cls.ScreenHeight:
                        cls.bgYscroll = 0 - cls.ScreenHeight
                    if cls.bgYscroll2 > cls.ScreenHeight:
                        cls.bgYscroll2 = 0 - cls.ScreenHeight

                    for a in Ship.ShipList:
                        Ship.ShipDraw(a)
                        Ship.HealthChecker(a)
                        a.AI()

                    for a in Animations.AnimationAdded:
                        if a.animType == 'Explosion':
                            a.explode()
                        if a.animType == 'BulletHit':
                            a.bulletHit()



                    Bullets.behaviour()
                    GameFlowControl.Initiate()
                    Falcon.ShipDeploy()

            elif cls.currentScreen == 'GameOver':
                cls.GameOverScreen()

            elif cls.currentScreen == 'VictoryScreen':
                cls.VictoryScreen()

            pygame.display.update()

    @classmethod
    def GameOverScreen(cls):
        myfont = pygame.font.SysFont("monospace", 30)
        myfont2 = pygame.font.SysFont("monospace", 40)
        myfont3 = pygame.font.SysFont("monospace", 20)
        label = myfont.render("You Died", 1, (255, 0, 0))
        label2 = myfont2.render("Your Score: " + str(Falcon.score), 1, (255, 255, 0))
        label3 = myfont3.render("(Press Backspace to Go back.)", 1, (255, 255, 255))
        cls.Gamewindow.blit(label, (180, 220))
        cls.Gamewindow.blit(label2, (70, 280))
        cls.Gamewindow.blit(label3, (70, 340))
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_BACKSPACE]:
            GameFlowControl.ResetGame()
            cls.currentScreen = 'IntroScreen'

    @classmethod
    def VictoryScreen(cls):
        cls.Gamewindow.blit(SpaceBg, (0, cls.bgYscroll))
        cls.Gamewindow.blit(SpaceBg2, (0, cls.bgYscroll2))
        cls.bgYscroll += 0.5
        cls.bgYscroll2 += 0.5
        if cls.bgYscroll > cls.ScreenHeight:
            cls.bgYscroll = 0 - cls.ScreenHeight
        if cls.bgYscroll2 > cls.ScreenHeight:
            cls.bgYscroll2 = 0 - cls.ScreenHeight
        Falcon.ShipDeploy()
        Falcon.y -= 10
        Falcon.shipControlEnabled = False
        myfont = pygame.font.SysFont("monospace", 30)
        myfont2 = pygame.font.SysFont("monospace", 20)
        label = myfont.render("You beat stage " + str(GameFlowControl.currentStage), 1, (255, 255, 0))
        label2 = myfont2.render("(Press Backspace to continue.)", 1, (255, 255, 255))
        cls.Gamewindow.blit(label, (130, 220))
        cls.Gamewindow.blit(label2, (70, 280))
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_BACKSPACE]:
            GameFlowControl.ResetGame()
            cls.currentScreen = 'MenuScreen'


boom1 = mixer.Sound('Sounds/boom1.wav')
thud1 = mixer.Sound('Sounds/bulletHitSound.wav')

class Animations:
    AnimationAdded = []
    def __init__(self, x, y, width, height, animType):
        self.explosionAni = 0
        self.aniDilation = 5
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.AnimationAdded.append(self)
        self.soundNumber = 1
        self.animType = animType

    def explode(self):
        if self.soundNumber > 0:
            boom1.play()
            self.soundNumber -= 1
        surf = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
        surf = surf.convert_alpha()
        surf.blit(explosion1, (0, 0), (self.explosionAni, 0, 100, 100))
        surf = pygame.transform.scale(surf, (self.width, self.height))
        Screen.Gamewindow.blit(surf, (self.x, self.y))


        self.aniDilation -= 1
        if self.aniDilation <= 0:
            self.explosionAni += 32
            self.aniDilation = 5

        if self.explosionAni > 300:
            self.AnimationAdded.remove(self)

    def bulletHit(self):
        if self.soundNumber > 0:
            thud1.play()
            self.soundNumber -= 1
        surf = pygame.Surface((128, 128), pygame.SRCALPHA, 32)
        surf = surf.convert_alpha()
        surf.blit(explosion2, (0, 0), (self.explosionAni, 0, 128, 128))
        surf = pygame.transform.scale(surf, (self.width, self.height))
        Screen.Gamewindow.blit(surf, (self.x, self.y))


        self.aniDilation -= 2
        if self.aniDilation <= 0:
            self.explosionAni += 128
            self.aniDilation = 5

        if self.explosionAni > 1600:
            self.AnimationAdded.remove(self)





warpJump = mixer.Sound('Sounds/warpJump.wav')
class Ship:
    ShipList = []
    def __init__(self, image, x, y, alive):
        self.image = image
        self.x = x
        self.y = y
        self.alive = alive
        self.width =  50
        self.height = 50
        self.lasershotSound = mixer.Sound('lasershot.wav')
        self.gunshotSound = mixer.Sound('gunshot.wav')
        self.bombLaserwave = mixer.Sound('explodeLaser.wav')
        self.hp = 3


    def HealthChecker(self):
        if self.hp <= 0:
            self.alive = False

    def ShipDraw(self):
        if self.alive:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            Screen.Gamewindow.blit(self.image, (self.x, self.y))


        else:
            if self.type == 'Player':
                GameFlowControl.DefeatCountdownStart = True
                Falcon.explodeTimes -= 1
                if Falcon.explodeTimes <= 0:
                    a = Animations(self.x, self.y, self.width, self.height, 'Explosion')
                    Falcon.explodeTimes = 1000


            else:
                try:
                    a = Animations(self.x, self.y, self.width, self.height, 'Explosion')
                    Ship.ShipList.remove(self)
                    if self.type == 'Boss':
                        print('Boss Killed.')
                        GameFlowControl.checkStageClear()
                        GameFlowControl.VictoryCountdownStart = True

                except:
                    print('An error occured here.')
                Falcon.score += 1





class PlayerShip(Ship):
    def __init__ (self, image, alive, x = 250, y = 500, fire = False ):
        super().__init__(image, x, y, alive)
        self.attackSpeed = 30
        self.totalBomb = 1
        self.bomb = self.totalBomb
        self.bombReady = 10
        self.score = 0
        self.damage = 1
        self.height = 60
        self.width = 60
        self.firePower = 1
        self.gold = 0
        self.type = 'Player'
        self.explodeTimes = 1
        self.shipControlEnabled = True


    def ShipControl(self):
        Keys = pygame.key.get_pressed()

        if self.shipControlEnabled:
            if self.alive:
                if Keys[pygame.K_k]:
                    if self.attackSpeed <= 0:
                        self.lasershotSound.play()
                        self.shotLevel()

                        self.attackSpeed = 30
                if self.attackSpeed > 0:
                    self.attackSpeed -= 5

                if Keys[pygame.K_a] and self.x > 0:
                    self.x -= 5
                if Keys[pygame.K_d] and self.x < 450:
                    self.x += 5
                if Keys[pygame.K_w] and self.y > 0:
                    self.y -= 5
                if Keys[pygame.K_s] and self.y < 550:
                    self.y += 5



                if self.bomb > 0:
                    self.bombReady -= 1
                    if self.bombReady <= 0:
                        if Keys[pygame.K_l]:
                            self.gunshotSound.play()
                            self.bombLaserwave.play()
                            self.gunshotSound.play()
                            for a in Ship.ShipList:
                                self.score += 1
                                a.hp -= 20
                            self.bomb -= 1
                            self.bombReady = 10
                            GameFlowControl.CountdownSummon = 100


    def shotLevel(self):
        if self.firePower == 1:
            shot = Bullets(x=Falcon.x + (Falcon.width/2) - 5, y=Falcon.y + (Falcon.height/2), image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot)

        elif self.firePower == 2:
            shot = Bullets(x=Falcon.x + 3, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot)
            shot2 = Bullets(x=Falcon.x + 47, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot2)

        elif self.firePower == 3:
            shot = Bullets(x=Falcon.x + 3, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot)
            shot2 = Bullets(x=Falcon.x + 47, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot2)
            shot3 = Bullets(x=Falcon.x + (Falcon.width/2) - 5, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot3)

        elif self.firePower > 3:
            shot = Bullets(x=Falcon.x + 3, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot)
            shot2 = Bullets(x=Falcon.x + 18, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot2)
            shot3 = Bullets(x=Falcon.x + 33, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot3)
            shot4 = Bullets(x=Falcon.x + 47, y=Falcon.y + 23, image=PurpleCircle, width=10, height=20)
            Bullets.PlayerBullets.append(shot4)





    def DisplayStats(self):
        myfont = pygame.font.SysFont("monospace", 30)
        Bombs = myfont.render('Bomb: ' + str(self.bomb), 1, (255, 255, 255))
        Gold = myfont.render('Gold: ' + str(self.gold), 1, (255, 255, 0))
        Score = myfont.render('Score: ' + str(self.score), 1, (255, 255, 255))
        CurrentStage = myfont.render('Stage: ' + str(GameFlowControl.currentStage), 1, (255, 255, 255))
        Screen.Gamewindow.blit(Bombs, (10, 10))
        Screen.Gamewindow.blit(Score, (300, 50))
        Screen.Gamewindow.blit(Gold, (10, 50))
        Screen.Gamewindow.blit(CurrentStage, (300, 10))


    def ShipDeploy(self):
        self.ShipControl()
        self.ShipDraw()
        self.DisplayStats()

class BossShip(Ship):
    def __init__ (self, image, x, y, alive = True):
        Ship.__init__(self, image, x, y, alive)
        self.width = 100
        self.height = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.ShipList.append(self)
        self.hp = 200
        self.fireTime = 150
        self.shotPause = 10
        self.shotRounds = 6
        self.directionMove = 'Left'
        self.type = 'Boss'


    def AI(self):
        self.fireTime -= 1
        if self.fireTime <= 0:
            if self.shotRounds > 0:
                self.shotPause -= 1
                if self.shotPause < 0:
                    self.gunshotSound.play()
                    shot = Bullets(x=self.x + (self.width/2), y=self.y + (self.height/2))
                    Bullets.EnemyBullets.append(shot)
                    self.shotRounds -= 1
                    self.shotPause = 10
                if self.shotRounds <= 0:
                    self.shotRounds = 6
                    self.fireTime = 150

        if self.y < 100:
            self.y += 1

        if self.y >= 100:
            if self.directionMove == 'Left':
                self.x -= 0.5
                if self.x < 0:
                    self.directionMove = 'Right'

            elif self.directionMove == 'Right':
                self.x += 0.5
                if self.x + self.width > Screen.ScreenWidth:
                    self.directionMove = 'Left'




class DiscBoss(BossShip):
    def __init__ (self, image, x, y, alive = True):
        Ship.__init__(self, image, x, y, alive)
        self.width = 100
        self.height = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.ShipList.append(self)
        self.hp = 250
        self.fireTime = 150
        self.shotPause = 10
        self.shotRounds = 14
        self.directionMove = 'Left'
        self.type = 'Boss'
        self.chase = False
        self.speed = 2
        self.chargeSkillCountdown = 1000
        self.chargeSkill = False

    def AI(self):
        self.chargeSkillCountdown -= 1
        if self.chargeSkillCountdown <= 0:
            self.chargeSkill = True
            self.chargeSkillCountdown = 1000
        if self.chargeSkill:
            self.y += 10
            if self.y > Screen.ScreenHeight:
                self.y = -100
                self.chargeSkill = False

        else:
            self.fireTime -= 1
            if self.fireTime <= 0:
                if self.shotRounds > 0:
                    self.shotPause -= 1
                    if self.shotPause < 0:
                        self.gunshotSound.play()
                        shot = Bullets(x=self.x + (self.width/2), y=self.y + (self.height/2), targetx=Falcon.x, targety=Falcon.y, speed=5)
                        Bullets.EnemyBullets.append(shot)
                        self.shotRounds -= 1
                        self.shotPause = 10
                    if self.shotRounds <= 0:
                        self.shotRounds = 14
                        self.fireTime = 150

            if Falcon.y < 100:
                self.chase = True
            else:
                self.chase = False

            if self.chase:
                if self.y > Falcon.y:
                    self.y -= self.speed

                if self.x > Falcon.x:
                    self.x -= self.speed

                else:
                    self.x += self.speed

            elif self.y < 100:
                self.y += self.speed

            if self.y >= 100:
                if self.x < Falcon.x:
                    self.directionMove = 'Right'
                else:
                    self.directionMove = 'Left'

                if self.directionMove == 'Left':
                    self.x -= self.speed - 1
                    if self.x < 0:
                        self.directionMove = 'Right'

                elif self.directionMove == 'Right':
                    self.x += self.speed - 1
                    if self.x + self.width > Screen.ScreenWidth:
                        self.directionMove = 'Left'


class BlueKur(BossShip):
    def __init__(self, image, x, y, alive=True):
        Ship.__init__(self, image, x, y, alive)
        self.width = 100
        self.height = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.ShipList.append(self)
        self.hp = 300
        self.fireTime = 150
        self.shotPause = 10
        self.shotRounds = 11
        self.directionMove = 'Left'
        self.type = 'Boss'

    def AI(self):
        self.fireTime -= 1
        if self.fireTime <= 0:
            if self.shotRounds > 0:
                self.shotPause -= 1
                if self.shotPause < 0:
                    self.gunshotSound.play()
                    shot1 = Bullets(x=self.x, y=self.y + 50, targetx=self.x - 10, targety=self.y + 100, speed=5)
                    Bullets.EnemyBullets.append(shot1)
                    shot2 = Bullets(x=self.x + 50, y=self.y + 50, targetx=Falcon.x+50, targety=Falcon.y, speed=5)
                    Bullets.EnemyBullets.append(shot2)
                    shot3 = Bullets(x=self.x + self.width - 10, y=self.y + 50, targetx=self.x + 110, targety=self.y + 100, speed=5)
                    Bullets.EnemyBullets.append(shot3)
                    self.shotRounds -= 1
                    self.shotPause = 10
                if self.shotRounds <= 0:
                    self.shotRounds = 11
                    self.fireTime = 150

        if self.y < 100:
            self.y += 1

        if self.y >= 100:
            if self.directionMove == 'Left':
                self.x -= 0.5
                if self.x < 0:
                    self.directionMove = 'Right'

            elif self.directionMove == 'Right':
                self.x += 0.5
                if self.x + self.width > Screen.ScreenWidth:
                    self.directionMove = 'Left'


class GreenJumper(BossShip):
    def __init__(self, image, x, y, alive=True):
        Ship.__init__(self, image, x, y, alive)
        self.width = 100
        self.height = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.ShipList.append(self)
        self.hp = 300
        self.fireTime = 300
        self.shotPause = 10
        self.shotRounds = 11
        self.firing = False
        self.directionMove = 'Left'
        self.type = 'Boss'
        self.jumpCountdown = 400
        self.blinkxDir = 200
        self.blinkyDir = 100
        self.rotatetime = 5

    def AI(self):
        self.rotatetime -= 1
        if self.rotatetime <= 0:
            self.image = pygame.transform.rotate(self.image, 90)
            self.rotatetime = 5
        if self.jumpCountdown < 150:
            Screen.Gamewindow.blit(HitImg, (self.blinkxDir + 30, self.blinkyDir + 30))

        self.jumpCountdown -= 2
        if not self.firing:
            if self.jumpCountdown <= 0:
                warpJump.play()
                self.x = self.blinkxDir
                self.y = self.blinkyDir
                self.jumpCountdown = 400
                self.blinkxDir = random.randrange(0, Screen.ScreenWidth - 100)
                self.blinkyDir = random.randrange(0, Screen.ScreenHeight - 200)



        self.fireTime -= 1
        if self.fireTime <= 0:
            self.firing = True
            if self.shotRounds > 0:
                self.shotPause -= 1
                if self.shotPause < 0:
                    self.gunshotSound.play()
                    shot1 = Bullets(x=self.x + 50, y=self.y + 50, targetx=random.randrange(0, 500), targety=random.randrange(0, 600), speed=4)
                    Bullets.EnemyBullets.append(shot1)
                    shot2 = Bullets(x=self.x + 50, y=self.y + 50, targetx=Falcon.x+50, targety=Falcon.y, speed=4)
                    Bullets.EnemyBullets.append(shot2)
                    shot3 = Bullets(x=self.x + 50, y=self.y + 50, targetx=random.randrange(0, 500), targety=random.randrange(0, 600), speed=4)
                    Bullets.EnemyBullets.append(shot3)
                    shot4 = Bullets(x=self.x + 50, y=self.y + 50, targetx=random.randrange(0, 500), targety=random.randrange(0, 600), speed=4)
                    Bullets.EnemyBullets.append(shot4)
                    shot5 = Bullets(x=self.x + 50, y=self.y + 50, targetx=random.randrange(0, 500), targety=random.randrange(0, 600), speed=4)
                    Bullets.EnemyBullets.append(shot5)
                    self.shotRounds -= 1
                    self.shotPause = 10
                if self.shotRounds <= 0:
                    self.shotRounds = 11
                    self.fireTime = 150
                    self.firing = False


class RedDiscShip(Ship):
    def __init__ (self, image, x, y, ai, alive = True, lDir = random.choice((True, False))):
        Ship.__init__(self, image, x, y, alive)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.alive = alive
        self.lDir = lDir
        self.ai = ai
        self.ShipList.append(self)
        self.fireTime = 150
        self.shotPause = 10
        self.shotRounds = 1
        self.type = 'Pawn'
        self.hp = 4



    def AI(self):
        if self.ai == 'leftright':
            if self.x > 480:
                self.lDir = True



            elif self.x < 0:
                self.lDir = False

            self.fireTime -= 1
            if self.fireTime <= 0:
                if self.shotRounds > 0:
                    self.shotPause -= 1
                    if self.shotPause < 0:
                        self.gunshotSound.play()
                        if self.x  < (Screen.ScreenWidth/2):
                            shot = Bullets(x=self.x + (self.width / 2), y=self.y + (self.height / 2), speed=5, width= 10, height= 10, direction='Right')
                        else:
                            shot = Bullets(x=self.x + (self.width / 2), y=self.y + (self.height / 2), speed=5, width=10,height=10, direction='Left')
                        Bullets.SlantBullets.append(shot)
                        self.shotRounds -= 1
                        self.shotPause = 10
                    if self.shotRounds <= 0:
                        self.shotRounds = 1
                        self.fireTime = 150

            if self.lDir:
                self.x -= 0.5
                self.image = ShipFlips[1]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))


            else:
                self.x += 0.5
                self.image = ShipFlips[2]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))




        elif self.ai == 'RandPatt':
            if self.x > 450:
                self.lDir = False
            elif self.x < 0:
                self.lDir = True
            if self.lDir:
                self.x += 1
            else:
                self.x -= 1

            self.y += 1
            if self.y > 600:
                self.alive = False



class BlueStopper(Ship):
    def __init__ (self, image, x, y, alive = True):
        Ship.__init__(self, image, x, y, alive)
        self.image = BlueStopperImgList[0]
        self.height = 70
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.alive = alive
        self.ShipList.append(self)
        self.type = 'Pawn'
        self.hp = 10

    def ShipDraw(self):
        if self.alive:
            Screen.Gamewindow.blit(self.image, (self.x, self.y))


    def AI(self):
        self.y += 2
        if self.y > Screen.ScreenHeight:
            try:
                Ship.ShipList.remove(self)
            except:
                print('An error occured here.')


class Bullets:
    PlayerBullets = []
    EnemyBullets = []
    SlantBullets = []

    def __init__(self, x, y, speed = 10, width = 7, height = 7, direction = 'Left', targetx = 0, targety = 0, image = LaserBullet):
        self.image = image
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        angle = math.atan2(targety - y, targetx - x)
        self.dx = math.cos(angle)*self.speed
        self.dy = math.sin(angle)*self.speed

    @classmethod
    def behaviour(cls):
        for a in cls.PlayerBullets:
            Screen.Gamewindow.blit(a.image, (a.x, a.y))
            a.y -= 13
            if a.y < -100:
                cls.PlayerBullets.remove(a)

        for a in cls.EnemyBullets:
            Screen.Gamewindow.blit(a.image, (a.x, a.y))
            a.x = a.x + int(a.dx)
            a.y = a.y + int(a.dy)
            if a.y > Screen.ScreenHeight or a.y < 0 or a.x > Screen.ScreenWidth or a.x < 0:
                cls.EnemyBullets.remove(a)



        for a in cls.SlantBullets:
            Screen.Gamewindow.blit(a.image, (a.x, a.y))
            if a.direction == 'Right':
                destx, desty = Falcon.x + 400, Falcon.y + 400
                if a.x < destx:
                    a.x += a.speed
                if a.y < desty:
                    a.y += a.speed
            elif a.direction == 'Left':
                destx, desty = Falcon.x - 400, Falcon.y + 400
                if a.x > destx:
                    a.x -= a.speed
                if a.y < desty:
                    a.y += a.speed

            if a.y > Screen.ScreenHeight or a.x > Screen.ScreenHeight or a.x < 0:
                try:
                    cls.EnemyBullets.remove(a)
                except:
                    pass

class Stages:
    bossCountdown = 100
    bossReady = 1

    stage1Pawn = 30
    countdownSummon = 50
    @classmethod
    def stage1(cls):
        cls.bossCountdown -= 1
        if cls.stage1Pawn <= 0:
            if cls.bossCountdown <= 0:
                if cls.bossReady > 0:
                    EnemyBoss = DiscBoss(ShipDiscBossImg, 250, -100)
                    cls.bossReady = 0

        toSummon = random.choice(('horPlane', 'downPlane'))
        cls.countdownSummon -= 1
        if cls.stage1Pawn > 0:
            if cls.countdownSummon <= 0:
                if toSummon == 'horPlane':
                    Enemy = RedDiscShip(ShipOne, random.choice((-50, 550)), random.randrange(-50, 300), 'leftright')
                else:
                    Enemy = RedDiscShip(ShipFlips[0], random.choice((-50, 550)), random.randrange(-50, 300), 'RandPatt')
                cls.countdownSummon = 50
                cls.stage1Pawn -= 1

    stage2Pawn = 50
    @classmethod
    def stage2(cls):
        cls.bossCountdown -= 1
        if cls.stage2Pawn <= 0:
            if cls.bossCountdown <= 0:
                if cls.bossReady > 0:
                    EnemyBoss = BlueKur(Bluekle, 250, -100)
                    cls.bossReady = 0


        cls.countdownSummon -= 1
        if cls.stage2Pawn > 0:
            if cls.countdownSummon <= 0:
                Enemy = BlueStopper(BlueStopperImgList[0], random.randrange(0, 450), -50)
                cls.countdownSummon = 50
                cls.stage2Pawn -= 1

    stage3Pawn = 60
    @classmethod
    def stage3(cls):
        cls.bossCountdown -= 1
        if cls.stage3Pawn <= 0:
            if cls.bossCountdown <= 0:
                if cls.bossReady > 0:
                    EnemyBoss = GreenJumper(GreenJumperImg, -200, -100)
                    cls.bossReady = 0

        toSummon = random.choice(('horPlane', 'downPlane'))
        cls.countdownSummon -= 1
        if cls.stage3Pawn > 0:
            if cls.countdownSummon <= 0:
                Enemy = BlueStopper(BlueStopperImgList[0], random.randrange(0, 550), -50)
                if toSummon == 'horPlane':
                    Enemy = RedDiscShip(ShipOne, random.choice((-50, 550)), random.randrange(-50, 300), 'leftright')
                else:
                    Enemy = RedDiscShip(ShipFlips[0], random.choice((-50, 550)), random.randrange(-50, 300), 'RandPatt')
                cls.countdownSummon = 30
                cls.stage3Pawn -= 2

    @classmethod
    def stage4(cls):
        cls.bossCountdown -= 1
        if cls.stage1Pawn <= 0:
            if cls.bossCountdown <= 0:
                if cls.bossReady > 0:
                    EnemyBoss = BossShip(ShipFlips[0], 250, -100)
                    cls.bossReady = 0

        toSummon = random.choice(('horPlane', 'downPlane'))
        cls.countdownSummon -= 1
        if cls.stage1Pawn > 0:
            if cls.countdownSummon <= 0:
                if toSummon == 'horPlane':
                    Enemy = RedDiscShip(ShipOne, random.choice((-50, 550)), random.randrange(-50, 300), 'leftright')
                else:
                    Enemy = RedDiscShip(ShipFlips[0], random.choice((-50, 550)), random.randrange(-50, 300), 'RandPatt')
                cls.countdownSummon = 50
                cls.stage1Pawn -= 1

    stage5Pawn = 100
    @classmethod
    def stage5(cls):
        cls.bossCountdown -= 1
        if cls.stage5Pawn <= 0:
            if cls.bossCountdown <= 0:
                if cls.bossReady > 0:
                    EnemyBoss = BossShip(ShipFlips[0], 250, -100)
                    cls.bossReady = 0

        toSummon = random.choice(('horPlane', 'downPlane'))
        cls.countdownSummon -= 1
        if cls.stage5Pawn > 0:
            if cls.countdownSummon <= 0:
                Enemy = BlueStopper(BlueStopperImgList[0], random.randrange(0, 550), -50)
                if toSummon == 'horPlane':
                    Enemy = RedDiscShip(ShipOne, random.choice((-50, 550)), random.randrange(-50, 300), 'leftright')
                else:
                    Enemy = RedDiscShip(ShipFlips[0], random.choice((-50, 550)), random.randrange(-50, 300), 'RandPatt')
                cls.countdownSummon = 30
                cls.stage5Pawn -= 2

    @classmethod
    def reset(cls):
        cls.bossCountdown = 100
        cls.bossReady = 1
        cls.countdownSummon = 100
        cls.stage1Pawn = 30
        cls.stage2Pawn = 50
        cls.stage3Pawn = 70
        cls.stage5Pawn = 100


class GameFlowControl:
    HighestScore = 0
    VictoryCountdown = 100
    VictoryCountdownStart = False
    DefeatCountdown = 100
    DefeatCountdownStart = False

    @classmethod
    def CheckCollision(cls):
        for a in RedDiscShip.ShipList:
            if Falcon.x + Falcon.width - 15 > a.x and Falcon.x + Falcon.width - 15 < a.x + a.width - 15 or Falcon.x < a.x + a.width - 15 and Falcon.x > a.x:
                if Falcon.y + Falcon.height - 15 > a.y and Falcon.y + Falcon.height - 10 < a.y + a.height - 15 or Falcon.y < a.y + a.height - 15 and Falcon.y > a.y:
                    Falcon.alive = False
                    myfont = pygame.font.SysFont("monospace", 20)
                    killedBy = myfont.render('CRASHED', 1, (255, 0, 0))
                    Screen.Gamewindow.blit(killedBy, (a.x, a.y))
                    if Falcon.score > cls.HighestScore:
                        cls.HighestScore = Falcon.score



        for y in Ship.ShipList:
            for x in Bullets.PlayerBullets:
                if x.y <= y.y + y.height and x.y > y.y:
                    if x.x + 10 < y.x + y.width and x.x > y.x:
                        y.hp -= Falcon.damage
                        a = Animations(x.x - 15, x.y - 35, 30, 30, 'BulletHit')



                        try:
                            Bullets.PlayerBullets.remove(x)
                        except:
                            print('An error occured here.')

        if cls.VictoryCountdownStart:
            cls.VictoryCountdown -= 1
            if cls.VictoryCountdown <= 0:
                Screen.currentScreen = 'VictoryScreen'

        if cls.DefeatCountdownStart:
            cls.DefeatCountdown -= 1
            if cls.DefeatCountdown <= 0:
                Screen.currentScreen = 'GameOver'

        for x in Bullets.EnemyBullets:
            if Falcon.alive:
                if x.y <= Falcon.y + Falcon.height and x.y > Falcon.y:
                    if x.x + 10 < Falcon.x + Falcon.width and x.x > Falcon.x:
                        Falcon.alive = False
                        Bullets.EnemyBullets.remove(x)
                        if Falcon.score > cls.HighestScore:
                            cls.HighestScore = Falcon.score

        for x in Bullets.SlantBullets:
            if Falcon.alive:
                if x.y <= Falcon.y + Falcon.height and x.y > Falcon.y:
                    if x.x + 10 < Falcon.x + Falcon.width and x.x > Falcon.x:
                        Screen.Gamewindow.blit(HitImg, (x.x, x.y - 25))
                        Falcon.alive = False
                        Bullets.SlantBullets.remove(x)
                        if Falcon.score > cls.HighestScore:
                            cls.HighestScore = Falcon.score

    currentStage = 1
    @classmethod
    def stageControl(cls):
        if cls.currentStage == 1:
            Stages.stage1()

        elif cls.currentStage == 2:
            Stages.stage2()

        elif cls.currentStage == 3:
            Stages.stage3()

        elif cls.currentStage == 4:
            Stages.stage4()

        elif cls.currentStage == 5:
            Stages.stage5()

    PowerUpCountown = 1000
    @classmethod
    def PowerUpControl(cls):
        for x in PowerUps.powerUps.powerUpsOnScreen:
            x.summon(Screen)
            if x.y <= Falcon.y + Falcon.height and x.y > Falcon.y:
                if x.x + 10 < Falcon.x + Falcon.width and x.x > Falcon.x:
                    PowerUps.powerUps.powerUpsOnScreen.remove(x)
                    Falcon.gold += 1

        cls.PowerUpCountown -= 1
        if cls.PowerUpCountown < 0:
            apple = PowerUps.powerUps(random.randrange(1, Screen.ScreenWidth - 50), random.randrange(1,Screen.ScreenHeight - 50))
            cls.PowerUpCountown = 1000

    stagesCleared = 0
    @classmethod
    def checkStageClear(cls):
        if cls.currentStage == 1:
            if cls.stagesCleared < 1:
                cls.stagesCleared += 1

        elif cls.currentStage == 2:
            if cls.stagesCleared < 2:
                cls.stagesCleared += 1

        elif cls.currentStage == 3:
            if cls.stagesCleared < 3:
                cls.stagesCleared += 1

        elif cls.currentStage == 4:
            if cls.stagesCleared < 4:
                cls.stagesCleared += 1

    @classmethod
    def Initiate(cls):
        cls.CheckCollision()
        cls.PowerUpControl()
        cls.stageControl()



    @classmethod
    def ResetGame(cls):
        RedDiscShip.ShipList.clear()
        Bullets.PlayerBullets.clear()
        Bullets.EnemyBullets.clear()
        Bullets.SlantBullets.clear()
        Falcon.alive = True
        Falcon.x = (Screen.ScreenWidth/2) - Falcon.width
        Falcon.y = Screen.ScreenHeight - (Screen.ScreenHeight/3)
        Falcon.bomb = Falcon.totalBomb
        Falcon.score = 0
        Falcon.explodeTimes = 1
        Falcon.shipControlEnabled = True
        PowerUps.powerUps.powerUpsOnScreen.clear()
        cls.VictoryCountdown = 100
        cls.VictoryCountdownStart = False
        cls.DefeatCountdown = 100
        cls.DefeatCountdownStart = False
        Stages.reset()
        Animations.AnimationAdded.clear()

""" All objects are written here"""
Falcon = PlayerShip(Faltar, True)
""" ==================================  """


Screen.GameLoop()


pygame.quit()
