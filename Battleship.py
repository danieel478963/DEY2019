
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

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
Done = False
Enter=False

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 80

def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()
    
def message_display(text,color):
    latgeText=pygame.font.Font('freesansbold.ttf',115) #font and size
    textSurf,TextRect=text_objects(text,latgeText,color)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,TextRect)
    pygame.display.update()
    
def buttom(msg,x,y,w,h,ic,ac,action=None,color=BLACK,stage=None):
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
        gameDisplay.fill(white)
        latgetext=pygame.font.Font('freesansbold.ttf',60) #font and size
        TextSurf,TextRect=text_objects("Statistics of the Game:",latgetext,color)
        TextRect.center=(400,100)
        gameDisplay.blit(TextSurf,TextRect)
        buttom("Back",200,500,100,50,ic,bright_color,"back1",color,stage)
        buttom("Quit",600,500,100,50,ic,bright_color,"quit",color,stage)
        pygame.display.update()
        
def Guest_Login(ic,ac,color,stage):#3
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)        
        pygame.display.update()
        clock.tick(60)

def Guest_Menu(color,bright_color,stage):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        buttom("Play",300,200,200,100,color,bright_color,"play",color)
        buttom("Get in touch",550,50,200,50,color,bright_color,"get in touch",color,stage)
        buttom("Quit",600,500,100,50,color,bright_color,"quit",color)
        buttom("Statistics",350,500,100,50,color,bright_color,"Statistics",color,"3")
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
        pygame.display.update()
        clock.tick(60) 
        
def Get_in_touch(ic,ac,color,action,stage):
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
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
        
def Start_Game(ic,ac,action,color):#2
    log=True
    while log:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
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
Project.py
