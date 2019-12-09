import pygame, sys,fontTools
import time
from pyglet.window.mouse import buttons_string
from pyglet.text import Label
from pygame.constants import MOUSEBUTTONUP, MOUSEMOTION
from _overlapped import NULL
pygame.init()

#width and height for the screen
display_width=800
display_height=600
#make the slide
gameDisplay = pygame.display.set_mode((display_width,display_height))
font = pygame.font.Font(None, 32)
FPS=60
Nickname=""
Boardwidth=12
Boardheight=12
Tilesize=40
X = int((display_width - (Boardwidth * Tilesize) - (200 + 50)) / 2)
Y = int((display_height - (Boardheight * Tilesize)) / 2)
FPS=30
WIDTH = 100
HEIGHT = 80
highscore_list = []

# Define some colors
BLACK = (0, 0, 0)
white = (255, 255, 255)
Bright_Green = (0, 255, 0)
Green=(0,200,0)
RED = (255, 0, 0)
Bright_Red=(255,0,0)
Blue=(0,0,255)
Orange=(255,165,0)
Yellow=(255,255,0)
Sky_Blue=(0,191,255)
Gray=(128,128,128)
Pink=(255,20,147)
Brown=(160,82,45)
Bright_Brown=(139,69,19)
very_bright_brown=(205,133,63)

# Set screen and icons
pygame.display.set_caption("BattleShip Fight To the Win!!!")
all=pygame.image.load("all.png")
test=pygame.image.load("sea.jpg")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
Done = False
Enter=False

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 80

def Lost_the_game(color,bright_color):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when Exit button in the top right is pressed the window will close
                quit()
                break
        gameDisplay.blit(test,(0,0))
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("U lost the game xD",latgetext,color)
        TextRect.center=(400,100)
        gameDisplay.blit(TextSurf,TextRect)
        buttom("Back",200,500,100,50,color,bright_color,"back1",color,"3")
        buttom("Quit",600,500,100,50,color,bright_color,"quit",color)
        pygame.display.update()    
        
def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()
    
def message_display(text,color):
    latgeText=pygame.font.Font('freesansbold.ttf',115) #font and size
    textSurf,TextRect=text_objects(text,latgeText,color)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,TextRect)
    pygame.display.update()
    
def buttom(msg,x,y,w,h,ic,ac,action=None,color=BLACK,stage=None,write=BLACK):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac, (x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="back":
                User_Pick()
            elif action=="quit":
                pygame.quit()
                quit()
            elif action=="back1":
                if stage=="2":
                    Start_Game(ic,ac,action,color)
                elif stage=="3":
                    Guest_Menu(ic,ac,stage)
            elif action=="get in touch":
                Get_in_touch(ic,ac,color,action,stage)
            elif action=="color":
                Start_Game(ic,ac,action,color)
            elif action=="Statistics":
                Statistics(ic,ac,color,stage)
            elif action=="guest":
                Guest_Login(ic,ac,color,stage)
            elif action=="play":
                Pick_ships_color(ic,ac,color,stage,write)
            elif action=="ship":
                Pick_Board_color(ic,ac,color,stage,write)
            elif action=="board":
                Pick_Miss_color(ic,ac,color,stage,write)
            elif action=="miss":
                main(color,ac,ic,stage,write)
            elif action=="login":
                User_Login(ic,ac,color,stage)
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))    
    smalltext=pygame.font.Font('freesansbold.ttf',20) #font and size
    TextSurf,TextRect=text_objects(msg,smalltext,BLACK)
    TextRect.center=((x+(w/2)),(y+(h/2)))  
    gameDisplay.blit(TextSurf,TextRect)

def Statistics(ic,bright_color,color,stage):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                break
        gameDisplay.blit(test,(0,0))
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("Statistics of the Game:",latgetext,color)
        TextRect.center=(400,100)
        gameDisplay.blit(TextSurf,TextRect)
        buttom("Back",200,500,100,50,ic,bright_color,"back1",color,stage)
        buttom("Quit",600,500,100,50,ic,bright_color,"quit",color,stage)
        pygame.display.update()

def Guest_Menu(color,bright_color,stage):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        buttom("Play",300,200,200,100,color,bright_color,"play",color)
        buttom("Get in touch",550,50,200,50,color,bright_color,"get in touch",color,stage)
        buttom("Quit",600,500,100,50,color,bright_color,"quit",color)
        buttom("Logout",475,500,100,50,color,bright_color,"back1",color,"2")
        buttom("Statistics",350,500,100,50,color,bright_color,"Statistics",color,"3")
        pygame.display.update()
        clock.tick(60)
        
def Pick_Miss_color(board,ship,color,stage,write):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        text = pygame.font.Font('freesansbold.ttf',40)       
        name=text.render("Pick Miss Color: ",1,color)
        buttom("miss1",450,300,100,50,Gray,board,"miss",ship,write,color)
        buttom("miss2",300,300,100,50,Orange,board,"miss",ship,write,color)
        buttom("miss3",150,300,100,50,Brown,board,"miss",ship,write,color)
        gameDisplay.blit(name,(100,250))
        buttom("Quit",600,500,100,50,color,color,"quit",color,write)
        pygame.display.update()
        clock.tick(60) 
               
def Pick_Board_color(ship,ac,color,stage,write):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        text = pygame.font.Font('freesansbold.ttf',40)       
        name=text.render("Pick Board Color: ",1,color)
        buttom("board1",450,220,100,50,Sky_Blue,ship,"board",write,write)
        buttom("board2",300,220,100,50,Pink,ship,"board",write,write)
        buttom("board3",150,220,100,50,Yellow,ship,"board",write,write)
        gameDisplay.blit(name,(100,150))
        buttom("Quit",600,500,100,50,color,ac,"quit",write,write)
        pygame.display.update()
        clock.tick(60)  

def Pick_ships_color(ic,ac,color,stage,write):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        text = pygame.font.Font('freesansbold.ttf',40)
        name=text.render("Pick Ship: ",1,color)
        gameDisplay.blit(name,(100,50))
        buttom("ship1",450,105,100,50,RED,ac,"ship",color,color,color)
        buttom("ship2",300,105,100,50,Green,ac,"ship",color,color,color)
        buttom("ship3",150,105,100,50,Blue,ac,"ship",color,color,color)
        buttom("Quit",600,500,100,50,color,ac,"quit",color,color,color)
        pygame.display.update()
        clock.tick(60)
                           
def Guest_Login(ic,ac,color,stage):#3
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("Please Enter your Info:",latgetext,color)
        TextRect.center=(400,150)
        gameDisplay.blit(TextSurf,TextRect)
        smalltext = pygame.font.Font('freesansbold.ttf',40)
        name=smalltext.render("Nickname: ",1,color)
        gameDisplay.blit(name,(100,200))
        buttom("Quit",600,500,100,50,ic,ac,"quit",color)
        name_text_box(ic,ac,stage)
        pygame.display.update()
        clock.tick(60)
        
def User_Login(ic,ac,color,stage):#3
    log=True
    active = False
    done = False
    input_box = pygame.Rect(100, 200, 50, 50)
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("Please Enter your Info:",latgetext,color)
        TextRect.center=(400,150)
        gameDisplay.blit(TextSurf,TextRect)
        smalltext = pygame.font.Font('freesansbold.ttf',40)
        name=smalltext.render("Username: ",1,(0,0,0))
        gameDisplay.blit(name,(100,200))
        buttom("Quit",600,500,100,50,ic,ac,"quit",color)
        name_text_box(ic,ac,stage)
        pygame.display.update()
        clock.tick(60) 
        
def Get_in_touch(ic,ac,color,action,stage):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("Ways to Contact:",latgetext,color)
        TextRect.center=(400,150)
        gameDisplay.blit(TextSurf,TextRect)
        smalltext = pygame.font.Font('freesansbold.ttf',40)
        name=smalltext.render("Mail = help@battleship.help ",1,color)
        gameDisplay.blit(name,(100,200))
        name=smalltext.render("phone = 02040608 ",1,color)
        gameDisplay.blit(name,(100,250))
        buttom("Quit",600,500,100,50,ic,ac,"quit",color)
        buttom("Back",200,500,100,50,ic,ac,"back1",color,stage)
        pygame.display.update()
        clock.tick(60)
        
def name_text_box(color,bright_color,stage):
    input_box = pygame.Rect(330, 205, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    active = False
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color if active else bright_color
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key==pygame.K_KP_ENTER or event.key==pygame.K_SPACE:
                        Guest_Menu(color,bright_color,stage)
                    else:
                        text += event.unicode 
        Nickname=text 
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(gameDisplay, color, input_box, 2)
        pygame.display.flip()                        
        clock.tick(60)   
           
def Start_Game(ic,ac,action,color):#2
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(test,(0,0))
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("Welcome to Battleship",latgetext,BLACK)
        TextRect.center=(400,150)
        gameDisplay.blit(TextSurf,TextRect)
        buttom("Guest",410,200,100,50,ic,ac,"guest",color,"3")
        buttom("Login",290,200,100,50,ic,ac,"login",color,"3")
        buttom("Quit",600,500,100,50,ic,ac,"quit",color)
        buttom("Back",100,500,100,50,ic,ac,"back",color)
        buttom("Statistics",350,500,100,50,ic,ac,"Statistics",color,"2")
        buttom("Get in touch",550,50,200,50,ic,ac,"get in touch",color,"2")
        pygame.display.update()
        clock.tick(60)
def draw_highlight_tile(x, y):
    left, top = left_top_coords_tile(x, y)
    pygame.draw.rect(gameDisplay, Blue,(left, top, Tilesize, Tilesize), 4)
     
def get_tile_at_pixel(x, y):
    for tilex in range(Boardwidth):
        for tiley in range(Boardheight):
            left = tilex * Tilesize + X
            top = tiley * Tilesize + Y
            tile_rect = pygame.Rect(left, top, Tilesize, Tilesize)
            if tile_rect.collidepoint(x, y):
                return (tilex, tiley)
    return (None, None) 

def left_top_coords_tile(x, y):
    left = x * Tilesize + X
    top = y * Tilesize + Y
    return (left, top)    

def generate_default_tiles(default_value):
    default_tiles = []
    for i in range(Boardwidth):
        default_tiles.append([default_value] * Boardheight)
    return default_tiles 

def make_ships():
    slist = []
    # make battleship
    ship = []
    for i in range(4):
        ship.append(('battleship',False))
    slist.append(ship)    
    # make destroyer
    ship = []
    for i in range(3):
        ship.append(('destroyer',False))
    slist.append(ship)
    # make submarine
    ship = []
    for i in range(3):
        ship.append(('submarine',False))
    slist.append(ship) 
    return slist

def draw_board(board, revealed,color_board,color_ship,miss):
    for tilex in range(Boardwidth):
        for tiley in range(Boardheight):
            left = tilex * Tilesize + X
            top = tiley * Tilesize + Y
            if not revealed[tilex][tiley]:
                pygame.draw.rect(gameDisplay, color_board, (left, top, Tilesize,Tilesize))
            else:
                if board[tilex][tiley] != (None, None):
                    pygame.draw.rect(gameDisplay, color_ship, (left, top, Tilesize, Tilesize))
                else:
                    pygame.draw.rect(gameDisplay, miss, (left, top, Tilesize, Tilesize))
                    
def run_game(ship_color,board_color,miss,stage,whrite):
    revealed_tiles = generate_default_tiles(False)
    main_board = generate_default_tiles((None, None))
    ship_objs = make_ships() # list of ships to be used, holds list of tuples
    main_board = add_ships_to_board(main_board, ship_objs)
    mousex, mousey = 0, 0
    counter = [] 
    count=0
    count_hit=0
    while True:
        # counter display (it needs to be here in order to refresh it)
        Smalltext = pygame.font.Font('freesansbold.ttf', 20)
        COUNTER_SURF = Smalltext.render(str(len(counter)), True, RED)
        COUNTER_RECT = SHOTS_SURF.get_rect()
        COUNTER_RECT.topleft = (display_width - 680, display_height - 570)
        # end of the counter
        gameDisplay.blit(test,(0,0))
        gameDisplay.blit(SHOTS_SURF, SHOTS_RECT)
        gameDisplay.blit(COUNTER_SURF, COUNTER_RECT)
        draw_board(main_board, revealed_tiles,board_color,ship_color,miss)
        buttom("Quit",600,500,100,50,whrite,whrite,"quit",whrite)
        if count>15 :
            Lost_the_game(whrite,whrite)
        mouse_clicked = False  
        for event in pygame.event.get():
            #click on board
            if event.type == MOUSEBUTTONUP:  
                mousex, mousey = event.pos
                mouse_clicked = True
                count+=1
            #follow Square
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos 
        tilex, tiley = get_tile_at_pixel(mousex, mousey)
        if tilex != None and tiley != None:
            if not revealed_tiles[tilex][tiley]:
                draw_highlight_tile(tilex, tiley)
            if not revealed_tiles[tilex][tiley] and mouse_clicked:
                revealed_tiles[tilex][tiley] = True
                counter.append((tilex, tiley))
        pygame.display.update()
        clock.tick(FPS)
        
def main(color_board,ac,color_ship,stage,write):  
    global SHOTS_SURF,SHOTS_RECT,COUNTER_SURF,COUNTER_RECT
    gameDisplay.blit(test,(0,0))
    Smalltext = pygame.font.Font('freesansbold.ttf', 20)
    SHOTS_SURF = Smalltext.render("Shots: ", True, ac)
    SHOTS_RECT = SHOTS_SURF.get_rect()
    SHOTS_RECT.topleft = (display_width - 750, display_height - 570)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        run_game(color_board,ac,color_ship,stage,write) 

def add_ships_to_board(board, ships):
    new_board = board[:]
    for ship in ships:
        for i in range(len(ship)):
            if ship[i][0] == 'battleship':
                new_board[1][1+i] = ship[i]
            elif ship[i][0] == 'destroyer':
                new_board[3][2+i] = ship[i]
            elif ship[i][0] == 'submarine':
                new_board[3+i][8] = ship[i]
    return new_board
        
def draw_tile_covers(board, tile, coverage):
    left, top = left_top_coords_tile(tile[0][0], tile[0][1])
    if board[tile[0][0]][tile[0][1]] != (None, None):
        pygame.draw.rect(gameDisplay, Pink, (left, top, Tilesize,Tilesize))
    else:
        pygame.draw.rect(gameDisplay, Orange, (left, top, Tilesize, Tilesize))
    if coverage > 0:
        pygame.draw.rect(gameDisplay, Brown, (left, top, coverage, Tilesize))
    pygame.display.update()
    clock.tick(FPS)
            
def User_Pick(): #1
    Pick=True
    while Pick:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        buttom("Color1",23,250,230,88,Blue,Sky_Blue,"color",Blue)
        buttom("Color2",280,248,230,85,Brown,Bright_Brown,"color",Brown)
        buttom("Color3",540,250,230,85,RED,Bright_Red,"color",RED)
        buttom("Color4",280,480,230,85,Green,Bright_Green,"color",Green)
        gameDisplay.blit(all,(0,0))
        buttom("Quit",600,500,100,50,Green,Bright_Green,"quit",Green)
        pygame.display.update()
        clock.tick(60)

User_Pick()
pygame.quit()
quit()