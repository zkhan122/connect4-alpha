from mainGame import *
from player import *
import pygame
import math
import sys
from pygame.locals import *
import tkinter
from tkinter import messagebox 
import sqlite3

class Game():
    
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

 

 ## menu


    def draw_text(self, text, font, color, surface, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    

    def main_menu(self):
 

        click = False

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
            
            #self.draw_text("vs AI!", self.font, (255, 255, 255), self.screen, 20, 20)
            
            Game.play(board, player_1, player_2, print_game=True)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    pass
                ##

                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)
    
    def vsOnline(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text("work in progress!", self.font, (255, 255, 255), self.screen, 200, 250)
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
            self.draw_text("-click on a button to start", self.font, (255, 255, 255), self.screen, 160, 250)
            self.draw_text("-press ESC to back out", self.font, (255, 255, 255), self.screen, 160, 300)
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
            self.draw_text("Connect 4 game with AI", self.font, (255, 255, 255), self.screen, 160, 250)
            self.draw_text("as part of school project", self.font, (255, 255, 255), self.screen, 160, 300)
            self.draw_text("Developed by: Zayaan Khan", self.font, (255, 255, 255), self.screen, 130, 530)
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
            pygame.time.wait(1000) # 1 sec delay 
            sys.exit()



###############
    @staticmethod
    def play(board, player_one, player_two, print_game=True):

        game_over = False
        turn = random.randint(PLAYER, AI) # player 1

        pygame.init() # initialize pygame

    
        # set title
        pygame.display.set_caption("Connect 4 Alpha!")

        screen = pygame.display.set_mode(size)


        draw_board(board, screen)


        pygame.display.update() # update window


        if print_game:
            print_board(board)

        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, color_black, (0, 0, width, square_size))
                    # image processing
                    screen.blit(text_1, (10, 10))
                    screen.blit(img1, (100, 5))

                    screen.blit(text_2, (610, 10))
                    screen.blit(img2, (570, 5))

                    # # timer
                    
                    # clock = pygame.time.Clock()
                    # font = pygame.font.SysFont(None, 100)
                    # counter = 300 # seconds
                    # text = font.render(str(counter), True, (0, 128, 0))

                    # timer_event = pygame.USEREVENT+1
                    # pygame.time.set_timer(timer_event, 1000)

                    # run = True
                    # while run:
                    #     clock.tick(60)
                    #     for event in pygame.event.get():
                    #         if event.type == pygame.QUIT:
                    #             run = False
                    #         elif event.type == timer_event:
                    #             counter -= 1
                    #             text = font.render(str(counter), True, (0, 128, 0))
                    #             if counter == 0:
                    #                 pygame.time.set_timer(timer_event, 0)   
                                                 
                    #     screen.fill((0, 0, 0), (300, 0, 300, 100)) # , (x, y, length, width)
                    #     text_rect = text.get_rect(center = (350, 50))
                    #     screen.blit(text, text_rect)
                    #     pygame.display.flip()
                    #     pygame.display.update()



                    posX = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, color_red, (posX, int(square_size/2)), radius)
                    
                    else:
                        pygame.draw.circle(screen, color_yellow, (posX, int(square_size/2)), radius)
                    pygame.display.update()



                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, color_black, (0, 0, width, square_size))
                    pygame.draw.rect(screen, color_black, (160, 400, width, square_size))

                    screen.blit(text_1, (10, 10))
                    screen.blit(img1, (100, 5))

                    screen.blit(text_2, (610, 10))
                    screen.blit(img2, (570, 5))

                    print(event.pos)

                    # player 1 
                    if turn == PLAYER: 
                        posX = event.pos[0] 
                        col = int(math.floor(posX / square_size)) # divide by 100

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, PLAYER_PIECE)

                            if bool(winning_move(board, PLAYER_PIECE)):
                                # print("Player 1 Wins! Congrats!")
                                winning_text = winning_font.render("Player 1 Wins! ", 1, color_red)
                                pygame.display.update(screen.blit(winning_text, (160, 50)))
                                pygame.display.update(screen.blit(end_gameImg, (100, width/2)))
                                pygame.time.wait(5000)
                                game_over = True

                                game.main_menu()
                                

                            turn += 1
                            turn = turn % 2


                            print_board(board)
                            draw_board(board, screen)


                        if game_over:
                            pygame.time.wait(3000)
                            sys.exit()

                            
            

                    
                # ai
                if turn == AI and not game_over:
                #   col = random.randint(0, COLUMN_COUNT-1)
                #   col = randomAI.pick_best_move(AI_PIECE)
                    col, minimax_score = minimax(board, 3, True) # depth = 2nd parameter

                    pygame.display.update()

                    if bool(is_valid_location(board, col)):
                        pygame.time.wait(500)
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, AI_PIECE)

                        if winning_move(board, AI_PIECE):
                            # print("Player 2 Wins! Congrats!")
                            winning_text = winning_font.render("Player 2 Wins! ", 1, color_yellow)
                            pygame.display.update(screen.blit(winning_text, (160, 50)))
                            pygame.display.update(screen.blit(end_gameImg, (100, width/2)))
                            pygame.time.wait(5000)
                            game_over = True

                            game.main_menu()

                        
                        turn += 1
                        turn = turn % 2
                        
                    
                        print_board(board)
                        draw_board(board, screen)


                    
                    if game_over:
                        pygame.time.wait(3000) # time until exit


    @staticmethod
    def loginForm():
        main_window = tkinter.Tk()
        main_window.title("Login Form")
        main_window.geometry("400x300")
        pad = 20
        main_window["padx"] = pad
        user_input = tkinter.StringVar()
        pass_input = tkinter.StringVar()
        info_label = tkinter.Label(main_window, text= "Login Application")
        info_label.grid(row=0, column=0, pady = 20)

        #username
        info_user  = tkinter.Label(main_window, text= "Username: ")
        info_user.grid(row=1, column=0, pady = 20)
        userinput = tkinter.Entry(main_window, textvariable=user_input)
        userinput.grid(row=1, column= 1)

        # password
        info_pass  = tkinter.Label(main_window, text= "Password: ")
        info_pass.grid(row=2, column=0, pady = 20)
        passinput = tkinter.Entry(main_window, textvariable=pass_input, show = "*")
        passinput.grid(row=2, column= 1)

        login_btn = tkinter.Button(main_window, text =  "Login", command=game.validate_login(user_input, pass_input))

        login_btn.grid(row=3, column=1)

        main_window.mainloop()

    @staticmethod
    def validate_login(user_input, pass_input):
        #creating db
        db = sqlite3.connect("login.sqlite")
        db.execute("CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)") # query
        db.execute("INSERT INTO login(username, password) VALUES('admin', '123')")
        cursor = db.cursor() # retrieving record
        cursor.execute("SELECT * FROM login where username=? AND password=?", (user_input.get(), pass_input.get()))

        row = cursor.fetchone() # return each row in db
        if row:
            messagebox.showinfo("info", "Login successful")
        else:
            messagebox.showinfo("info", "Login failed")
         
        cursor.connection.commit() # saving changes to db
        db.close() # closing db




if __name__ == '__main__':
    board = create_board()
    player_1 = RandomPlayer(1)
    player_2 = RandomPlayer(2)

    pygame.init()
    pygame.display.set_caption("Connect 4 Alpha!")

    
   # play(board, player_1, player_2, print_game=True)
    game = Game()
    game.loginForm()
    game.main_menu()

    
