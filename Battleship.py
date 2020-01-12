import pygame,sqlite3,random
from pygame.constants import MOUSEBUTTONUP, MOUSEMOTION
pygame.init()
#width and height for the screen
display_width=800
display_height=600
#make the slide
gameDisplay = pygame.display.set_mode((display_width,display_height))
font = pygame.font.Font(None, 32)
FPS=60
Boardwidth=12
Boardheight=12
Tilesize=40
shots=25
X = int((display_width - (Boardwidth * Tilesize) - (200 + 50)) / 2)
Y = int((display_height - (Boardheight * Tilesize)) / 2)
# Define some colors
Black = (0, 0, 0)
Red = (255, 0, 0)
Sky_Blue=(0,238,238)
Dark_Blue=(100,149,237)
Yellow=(255,255,0)
White=(255,255,255)
Blue=(0,0,255)
Dark_Red=(218,47,10)
light_Red=(251,127,100)
Dark_yellow=(227,207,87)
light_yellow=(255,185,15)
# Set screen and icons
pygame.display.set_caption("BattleShip Fight To the Win!!!")
PickBackground=pygame.image.load("open.jpg")
Background=pygame.image.load("sea.jpg")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 80
#board
grid = []
for i in range(13):
    grid.append([0,0,0,0,0,0,0,0,0,0,0,0])

#set player
class Player: #player class to save the info about the player
    def __init__(self,color,name,ship_color,board_color,miss_color,score,stage,user,type=None):
        self.type=type
        self.color=color
        self.name=name
        self.ship_color=ship_color
        self.board_color=board_color
        self.miss_color=miss_color
        self.score=score
        self.stage=stage
        self.user=user 
           
player=Player(Black,"empty",Black,Black,Black,0,0,"empty") #global player
conn = sqlite3.connect('BattleShip.db')
c = conn.cursor()

def generate_default_tiles(default_value): #side function fill the reveled with false to fresh start
    default_tiles = []
    for i in range(Boardwidth):
        default_tiles.append([default_value] * Boardheight)
    return default_tiles

def run_game(): #9
    revealed_tiles = generate_default_tiles(False) #make fresh start
    make_ships() #make random ships
    mousex, mousey = 0, 0
    counter = []  #count hits and miss
    while True:
        # counter display (it needs to be here in order to refresh it)
        Smalltext = pygame.font.Font('freesansbold.ttf', 20)
        COUNTER_SURF = Smalltext.render(str(len(counter)), True, player.color)
        COUNTER_RECT = SHOTS_SURF.get_rect()
        COUNTER_RECT.topleft = (display_width - 680, display_height - 570)
        # end of the counter
        gameDisplay.blit(Background,(0,0))
        gameDisplay.blit(SHOTS_SURF, SHOTS_RECT)
        gameDisplay.blit(COUNTER_SURF, COUNTER_RECT)
        draw_board(grid,revealed_tiles)
        button("Quit",600,500,100,50,player.color,"quit")
        if len(counter)==shots:
            Game_over()
        mouse_clicked = False  
        for event in pygame.event.get():
            #click on board
            if event.type == MOUSEBUTTONUP:  
                mousex, mousey = event.pos
                mouse_clicked = True
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
                if grid[tilex][tiley] =='battleship':
                    player.score=player.score+10
                if grid[tilex][tiley] !='battleship':
                    player.score=player.score+3
        Exit_check()
           
def main(miss_color): #8 
    player.miss_color=miss_color  
    global SHOTS_SURF,SHOTS_RECT,COUNTER_SURF,COUNTER_RECT
    gameDisplay.blit(Background,(0,0))
    Smalltext = pygame.font.Font('freesansbold.ttf', 20)
    SHOTS_SURF = Smalltext.render("Shots: ",True, player.color)
    SHOTS_RECT = SHOTS_SURF.get_rect()
    SHOTS_RECT.topleft = (display_width -750, display_height - 570)
    while True:
        Exit_check()
        run_game() 
        
def get_tile_at_pixel(x, y):#side function
    for tilex in range(Boardwidth):
        for tiley in range(Boardheight):
            left = tilex * Tilesize + X
            top = tiley * Tilesize + Y
            tile_rect = pygame.Rect(left, top, Tilesize, Tilesize)
            if tile_rect.collidepoint(x, y):
                return (tilex, tiley)
    return (None, None)  
  
def draw_highlight_tile(x, y): #side function to show highlight follow the mouse
    left, top = x * Tilesize + X , y * Tilesize + Y
    pygame.draw.rect(gameDisplay, Black,(left, top, Tilesize, Tilesize), 4)  
    
def button(msg,x,y,w,h,color,action=None): #side function to make buttons
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,color, (x,y,w,h))
        if click[0]==1 and action!=None:#if click on button do
            if action=="back":
                User_Pick()
            elif action=="back1" and player.stage==0:
                Start_Game(color)
            elif action=="back1" and player.stage==1:
                Guest_Menu()
            elif action=="back1" and player.stage==2:
                Admin_Menu()
            elif action=="renaming":
                Renaming()
            elif action=="quit":
                pygame.quit()
                quit()
            elif action=="color":
                c.execute('SELECT * FROM Type')
                data = c.fetchall()
                if msg=="Color1":
                    player.type="Deuteranope"
                    c.execute("UPDATE Type SET Number = ( ? ) WHERE Name = ( ? )",(data[0][1]+1 if player.type=="Deuteranope" else data[0][1],"Deuteranope"))
                if msg=="Color2":
                    player.type="Protanope"
                    c.execute("UPDATE Type SET Number = ( ? ) WHERE Name = ( ? )",(data[1][1]+1 if player.type=="Protanope" else data[1][1],"Protanope"))
                if msg=="Color3":
                    player.type="Tritanope"
                    c.execute("UPDATE Type SET Number = ( ? ) WHERE Name = ( ? )",(data[2][1]+1 if player.type=="Tritanope" else data[2][1],"Tritanope"))
                if msg=="Color4":
                    player.type="Normal Vision"
                    c.execute("UPDATE Type SET Number = ( ? ) WHERE Name = ( ? )",(data[3][1]+1 if player.type=="Normal Vision" else data[3][1],"Normal Vision"))
                Start_Game(color)
            elif action=="logout":
                Start_Game(color)
            elif action=="Statistics":
                Statistics()
            elif action=="Type":
                Type()
            elif action=="Games":
                Games()
            elif action=="get in touch":
                Get_in_touch()
            elif action=="guest":
                Guest_Login() 
            elif action=="login":
                Admin_Login()
            elif action=="play":
                Pick_ships_color() 
            elif action=="ship":
                Pick_Board_color(color)
            elif action=="board":
                Pick_Miss_color(color)
            elif action=="miss":
                main(color)
    else: #show the button
        pygame.draw.rect(gameDisplay, color, (x,y,w,h))    
    Print(msg,Black,20,x+(w/2),y+(h/2))
    
def draw_board(board, revealed): #side function draw the board
    for tilex in range(Boardwidth):
        for tiley in range(Boardheight):
            left = tilex * Tilesize + X
            top = tiley * Tilesize + Y
            if not revealed[tilex][tiley]:  #if not click draw the board color
                pygame.draw.rect(gameDisplay, player.board_color, (left, top, Tilesize,Tilesize))
            else:
                if board[tilex][tiley] == 'battleship': #if click and hit draw the hit color
                    pygame.draw.rect(gameDisplay, player.ship_color, (left, top, Tilesize, Tilesize))
                else:
                    #if click and miss draw the miss color
                    pygame.draw.rect(gameDisplay, player.miss_color, (left, top, Tilesize, Tilesize))
            
def make_ships(): #side function make all the ships on the boards random
    row=random.randrange(0,8)
    col=random.randrange(0,2)
    #ship 1
    for i in range(5):
        grid[col][row+i]='battleship'
    #ship 2
    row=random.randrange(0,9)
    col=random.randrange(2,5)
    for i in range(4):
        grid[col][row+i]='battleship'
    #ship 3
    row=random.randrange(0,5)
    col=random.randrange(5,10)
    for i in range(3):
        grid[col+i][row]='battleship'
    #ship 4  
    row=random.randrange(5,9)
    col=random.randrange(5,11)
    for i in range(2):
        grid[col][row+i]='battleship'
        #ship 5 
    row=random.randrange(8,10)
    col=random.randrange(5,12)
    for i in range(3):
        grid[col][row+i]='battleship'
    
def create_tables():
    c.execute("CREATE TABLE IF NOT EXISTS NamesAndScores(Name,Score)")
    c.execute("CREATE TABLE IF NOT EXISTS Type(Name,Number)")
    c.execute("CREATE TABLE IF NOT EXISTS Game(Name,Number)")
    c.execute('SELECT * FROM Type')
    data = c.fetchall()
    if data==[]:
        c.execute("INSERT INTO Type(Name, Number) VALUES (?,?)",("Deuteranope", 0))
        c.execute("INSERT INTO Type(Name, Number) VALUES (?,?)",("Protanope", 0))
        c.execute("INSERT INTO Type(Name, Number) VALUES (?,?)",("Tritanope", 0))
        c.execute("INSERT INTO Type(Name, Number) VALUES (?,?)",("Normal Vision", 0))
    conn.commit()

def dynamic_game_entry():
    c.execute('SELECT * FROM Game')
    data = c.fetchall()
    if data==[]:
        c.execute("INSERT INTO Game(Name,Number) VALUES (?,?)",("Games",0))
    conn.commit()

def sortSecond(val): 
    return val[1]

def min(first,sec):
    if first<sec:
        return first
    return sec
    
def Statistics(): #side function
    gameDisplay.blit(Background,(0,0)) #picture of background     
    c.execute('SELECT * FROM NamesAndScores')
    data = c.fetchall()
    location=0
    names_and_scores=[]
    Print("Statistics of the Game:",player.color,60,400,50)
    Print("Name      Score",player.color,60,400,100)
    for row in data:
        names_and_scores.append((row[0],row[1]))
    names_and_scores.sort(key = sortSecond, reverse = True)
    for i in range(min(len(names_and_scores),7)):
            Print(str(i+1)+".",player.color,40,120,175+location)
            Print(names_and_scores[0+i][0],player.color,40,250,175+location)
            Print(str(names_and_scores[0+i][1]),player.color,40,550,175+location)
            location+=50  
    while True:
        button("Back",200,500,100,50,player.color,"back1")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()  
        
def Type(): #side function
    gameDisplay.blit(Background,(0,0)) #picture of background     
    c.execute('SELECT * FROM Type')
    data = c.fetchall()
    location=0
    type_and_number=[]
    Print("Type of Players:",player.color,60,400,50)
    Print("Type:      Numbers:",player.color,60,400,100)
    for row in data:
        type_and_number.append((row[0],row[1]))
    type_and_number.sort(key = sortSecond, reverse = True)
    for i in range(min(len(type_and_number),4)):
            Print(str(i+1)+".",player.color,40,80,175+location)
            Print(type_and_number[0+i][0],player.color,40,250,175+location)
            Print(str(type_and_number[0+i][1]),player.color,40,550,175+location)
            location+=50  
    while True:
        button("Back",200,500,100,50,player.color,"back1")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()  

def Games(): #side function
    gameDisplay.blit(Background,(0,0)) #picture of background     
    c.execute('SELECT * FROM Game')
    data = c.fetchall()
    Print("Number of Games:",player.color,60,400,50)
    Print("1 . Games : "+str(data[0][1]),player.color,40,150,150)
    while True:
        button("Back",200,500,100,50,player.color,"back1")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()  
           
def Update_table():
    c.execute('SELECT * FROM Game')
    data = c.fetchall()
    c.execute("UPDATE Game SET Number = ( ? ) WHERE Name = ( ? ) ",(data[0][1]+1,"Games"))
    c.execute("INSERT INTO NamesAndScores(Name, Score) VALUES (?,?)",(player.name, player.score))
    conn.commit()
    
def Game_over(): #10
    Update_table()  #update count of games and player and score
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print(player.name+" your scores is : "+str(player.score),player.color,50,400,200)
    Print("Game Over xD ",player.color,60,400,100)
    while True:
        button("Back",200,500,100,50,player.color,"back1")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()
        
def Pick_Miss_color(board_color): #7 pick color of miss 
    player.board_color=board_color
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Pick Miss Color: ",player.color,40,300,250)
    while True: 
        #user pick color
        button("miss",450,300,100,50,Yellow,"miss")
        button("miss",300,300,100,50,light_yellow,"miss")
        button("miss",150,300,100,50,Dark_yellow,"miss")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()
           
def Pick_Board_color(ship_color): #6 pick color of the board
    player.ship_color=ship_color
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Pick Board Color: ",player.color,40,300,150)
    while True:
        #user pick board color
        button("board",450,220,100,50,Blue,"board")
        button("board",300,220,100,50,Sky_Blue,"board")
        button("board",150,220,100,50,Dark_Blue,"board")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()  
        
def Pick_ships_color(): #5  pick color of the hits
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Pick Ship: ",player.color,40,250,50)
    while True:
        #user pick color for hit
        button("ship",450,105,100,50,Red,"ship")
        button("ship",300,105,100,50,Dark_Red,"ship")
        button("ship",150,105,100,50,light_Red,"ship")
        button("Quit",600,500,100,50,player.color,"quit")
        Exit_check()

def Renaming(): #side function
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Please Enter your new Nickname :",player.color,40,400,150)
    Print("Nickname: ",player.color,40,180,220)
    while True:
        button("Quit",600,500,100,50,player.color,"quit")
        name_text_box(player.color) #text box
        Exit_check()       
       
def name_text_box(color): #side function
    input_box = pygame.Rect(330, 205, 140, 32) #position of the text box
    active = False
    text = ''  #to save the input
    while True:
        for event in pygame.event.get(): #loop to check if click on quit
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN: #get the text
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key==pygame.K_KP_ENTER or event.key==pygame.K_SPACE:
                        player.name=text  #after press enter go to admin/guest
                        if player.user=="guest":
                            Guest_Menu()
                        if player.user=="ADMIN" and text=="admin":
                            Admin_Menu()
                        if player.user=="ADMIN" and text!="admin":
                            wrong_input()
                    else:
                        text += event.unicode 
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(gameDisplay, color, input_box, 2)
        Exit_check()
         
def Guest_Menu(): #4
    player.stage=1
    player.score=0
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Player : "+player.name,player.color,60,400,150)
    while True:
        button("Renaming",50,50,200,50,player.color,"renaming")
        button("Play",300,200,200,100,player.color,"play")
        button("Get in touch",550,50,200,50,player.color,"get in touch")
        button("Quit",600,500,100,50,player.color,"quit")
        button("Logout",475,500,100,50,player.color,"logout")
        button("Statistics",350,500,100,50,player.color,"Statistics")
        Exit_check()
        
def Admin_Menu(): #4
    player.stage=2
    player.score=0
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Admin : "+player.name,player.color,60,400,150)
    while True:
        button("Renaming",50,50,200,50,player.color,"renaming")
        button("Play",300,200,200,100,player.color,"play")
        button("Get in touch",550,50,200,50,player.color,"get in touch")
        button("Quit",600,500,100,50,player.color,"quit")
        button("Logout",475,500,100,50,player.color,"logout")
        button("Statistics",480,400,100,50,player.color,"Statistics")
        button("Types",350,400,100,50,player.color,"Type")
        button("Games",220,400,100,50,player.color,"Games")
        Exit_check()
             
def Guest_Login(): #3
    player.user="guest"
    player.stage=1
    gameDisplay.blit(Background,(0,0)) #picture of background 
    Print("Please Enter your Info:",player.color,60,400,150)
    Print("Nickname:",player.color,40,180,220)
    while True:
        button("Quit",600,500,100,50,player.color,"quit")
        name_text_box(player.color) #text box
        Exit_check()
def wrong_input():
    player.stage=0
    gameDisplay.blit(Background,(0,0)) #picture of background 
    Print("You Enter Wrong Info",player.color,60,400,150)
    Print("go back and try again",player.color,60,400,250)
    while True:
        button("Quit",600,500,100,50,player.color,"quit")
        button("Back",200,500,100,50,player.color,"back1")
        Exit_check()  
        
def Admin_Login(): #3
    player.user="ADMIN"
    player.stage=2
    gameDisplay.blit(Background,(0,0)) #picture of background 
    Print("Please Enter your Info:",player.color,60,400,150)
    Print("Username:",player.color,40,180,220)
    while True:
        button("Quit",600,500,100,50,player.color,"quit")
        name_text_box(player.color) #text box
        Exit_check()  
        
def Get_in_touch(): #side function
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Ways to Contact:",player.color,60,400,150)
    Print("Mail = help@battleship.help ",player.color,40,400,200)
    Print("phone = 0204060 ",player.color,40,400,250)
    while True:
        button("Quit",600,500,100,50,player.color,"quit")
        button("Back",200,500,100,50,player.color,"back1")
        Exit_check()

def Print(text,color,font_size,cord1,cord2):
    latgetext=pygame.font.Font('freesansbold.ttf',font_size) #font and size
    textSurface=latgetext.render(text,True,color)
    TextRect=textSurface.get_rect()
    TextRect.center=(cord1,cord2)
    gameDisplay.blit(textSurface,TextRect) #display the text
    
def Start_Game(color):#2
    player.color=color
    player.stage=0
    gameDisplay.blit(Background,(0,0)) #picture of background
    Print("Welcome to Battleship",player.color,60,400,150)
    while True:
        button("Guest",480,220,90,50,player.color,"guest")
        button("Login",220,220,90,50,player.color,"login")
        button("Quit",600,500,100,50,player.color,"quit")
        button("Back",100,500,100,50,player.color,"back")
        button("Statistics",50,50,100,50,player.color,"Statistics")
        button("Get in touch",550,50,200,50,player.color,"get in touch")
        Exit_check()
         
def User_Pick(): #1
    #crate tables in database
    dynamic_game_entry()
    while True:
        #user pick type of color blindness
        button("Color1",75,180,140,150,Yellow,"color")
        button("Color2",333,175,140,150,Yellow,"color")
        button("Color3",575,175,140,150,Red,"color")
        button("Color4",332,400,140,150,Red,"color")
        gameDisplay.blit(PickBackground,(0,0)) #picture of background
        button("Quit",600,500,100,50,White,"quit")
        Exit_check()

def Exit_check(): #check if click on exit and update display
    for event in pygame.event.get(): #loop to check if click on quit
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(FPS)
    
create_tables()
User_Pick()
pygame.quit()
quit()
c.close
conn.close()