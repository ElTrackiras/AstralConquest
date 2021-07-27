import pygame


class Button:
    def __init__(self, x, y, width, height, color = (255, 255, 255), text = 'Button', textColor = (0, 0, 0), fontSize = 30, image = None, image2=None, live = True, topTextPadding = 0, leftTextPadding = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image2 = image2
        self.color = color
        self.text = text
        self.textColor = textColor
        self.fontSize = fontSize
        self.live = live
        self.topTextPadding = topTextPadding
        self.leftTextPadding = leftTextPadding




    def Place(self, surface, function=None):
        if self.live:
            myfont = pygame.font.SysFont('rockwell', self.fontSize)
            text = myfont.render(self.text, 1, self.textColor)

            mx, my = pygame.mouse.get_pos()
            def blittheImg():
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                surface.blit(self.image, (self.x, self.y))

            if self.image != None:
                if self.image2 != None:
                    blittheImg()

                    if mx > self.x and mx < self.x + self.width:
                        if my > self.y and my < self.y + self.height:
                            self.image = self.image2
                            blittheImg()
                            if pygame.mouse.get_pressed()[0]:  # 0 = leftClick 1 = middleClick 2 = rightClick
                                function()
                else:
                    blittheImg()

                    if mx > self.x and mx < self.x + self.width:
                        if my > self.y and my < self.y + self.height:
                            self.width += 30
                            self.height += 30
                            self.x -= 10
                            self.y -= 10
                            blittheImg()
                            if pygame.mouse.get_pressed()[0]:  # 0 = leftClick 1 = middleClick 2 = rightClick
                                function()
            else:
                pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

                if mx > self.x and mx < self.x + self.width:
                    if my > self.y and my < self.y + self.height:
                        self.color = (233, 0, 2)
                        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
                        if pygame.mouse.get_pressed()[0]:  # 0 = leftClick 1 = middleClick 2 = rightClick
                            function()




            surface.blit(text, (self.x + self.leftTextPadding, self.y + self.topTextPadding))


