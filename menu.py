from mainGame import *
import pygame, sys
 
from pygame.locals import *



class Menu():
    def __init__(self, ):
        self.mainClock = pygame.time.Clock()
      #  self.pygame.init()
       # self.pygame.display.set_caption('game base')
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0 , 32)
 
        self.font = pygame.font.SysFont("Lexend Deca", 40)
        self.font2 = pygame.font.SysFont("Lexend Deca", 10)

        self.menu_img1 = pygame.image.load("C:\\Users\\ayesh\OneDrive\\Documents\\Zayaan\\code base\\nea\\vsAIbuttonimg.JPG")
        self.menu_img2 = pygame.image.load("C:\\Users\\ayesh\OneDrive\\Documents\\Zayaan\\code base\\nea\\vsOnlinebuttonimg.JPG")
        self.menu_img3 = pygame.image.load("C:\\Users\\ayesh\OneDrive\\Documents\\Zayaan\\code base\\nea\\helpButtonimg.JPG")
        self.menu_img4 = pygame.image.load("C:\\Users\\ayesh\OneDrive\\Documents\\Zayaan\\code base\\nea\\aboutButtonimg.JPG")
        self.menu_img5 = pygame.image.load("C:\\Users\\ayesh\OneDrive\\Documents\\Zayaan\\code base\\nea\\quitButtonimg.JPG")
        self.menu_img6 = pygame.image.load("C:\\Users\\ayesh\OneDrive\\Documents\\Zayaan\\code base\\nea\\logo.JPG")
    

 
    def draw_text(self, text, font, color, surface, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    click = False

    def main_menu(self):
        while True:
    
            self.screen.fill((0,0,0))
          #  self.draw_text("Connect 4 Alpha!", self.font, (255, 255, 255), self.screen, 200, 20)
            pygame.display.update(self.screen.blit(self.menu_img6, (160, 20)))
            self.draw_text("v1.1", self.font2, (255, 255, 255), self.screen, 10, 550)

            self.draw_text("click", self.font2, (255, 255, 255,), self.screen, 10, 200)
            self.draw_text("a", self.font2, (255, 255, 255,), self.screen, 10, 235)
            self.draw_text("option!", self.font2, (255, 255, 255,), self.screen, 10, 270)
    
            mx, my = pygame.mouse.get_pos()
    
            button_1 = pygame.Rect(200, 100, 200, 50) # vs AI
            button_2 = pygame.Rect(200, 200, 200, 50) # vs Online
            button_3 = pygame.Rect(200, 300, 200, 50) # Help
            button_4 = pygame.Rect(200, 400, 200, 50) # About
            button_5 = pygame.Rect(450, 500, 100, 50) # Quit

            if button_1.collidepoint((mx, my)):
                if click:
                    self.vsAI()
            if button_2.collidepoint((mx, my)):
                if click:
                    self.vsOnline()
            if button_3.collidepoint((mx, my)):
                if click:
                    self.Help()
            if button_4.collidepoint((mx, my)):
                if click:
                    self.About()
            if button_5.collidepoint((mx, my)):
                if click:
                    self.Quit()


            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            pygame.draw.rect(self.screen, (255, 0, 0), button_2)
            pygame.draw.rect(self.screen, (255, 0, 0), button_3)
            pygame.draw.rect(self.screen, (255, 0, 0), button_4)
            pygame.draw.rect(self.screen, (255, 0, 0), button_5)
            
            pygame.display.update(self.screen.blit(self.menu_img1, (200, 100)))
            pygame.display.update(self.screen.blit(self.menu_img2, (200, 200)))
            pygame.display.update(self.screen.blit(self.menu_img3, (200, 300)))
            pygame.display.update(self.screen.blit(self.menu_img4, (200, 400)))
            pygame.display.update(self.screen.blit(self.menu_img5, (425, 500)))
    
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            self.mainClock.tick(60)
    
    def vsAI(self, ):
        running = True
        while running:
            self.screen.fill((0,0,0))
            
            self.draw_text("vs AI!", self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # enter game

                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)
    
    def vsOnline(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text("vs Online!", self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)

            self.mainClock.tick(60)
    
    def Help(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text("Help!", self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)

            self.mainClock.tick(60)
    
    def About(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text("About!", self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)

            self.mainClock.tick(60)
    
    def Quit(self):

        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text("Quit!", self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)
 
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Connect 4 Alpha!")
    menu = Menu()
    menu.main_menu()

