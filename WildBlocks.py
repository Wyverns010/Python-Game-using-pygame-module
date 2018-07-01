# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:08:30 2018
Purpose: A game made using pygame in python...Click run and enjoy!
@author: Yash
"""

import pygame as pyg
import time as t
import random

pyg.init()

# for the frame
width = 800
height = 600

#difining tuples for different colors in the order of RGB-red green blue
white = (255,255,255)
black = (0,0,0)
light_red = (255,0,0)
red = (175,0,0)
green = (0,175,0)
big_block = (51, 153, 255)
light_green = (0,255,0)



Gdisplay = pyg.display.set_mode((width,height))
pyg.display.set_caption('Dodge the Hurdles')
time = pyg.time.Clock()

#loading the bike image
bikeImg = pyg.image.load('bikeImg.png')
#print(bikeImg)

#function for displaying score
def score_game(dodged):
    string = 'Score  :  '+str(dodged)
    font = pyg.font.Font('freesansbold.ttf',25)
    text = font.render(string,True,black)
    Gdisplay.blit(text,(0,0))

#drawing boundary lines

def dividers(line_y):
    y = line_y
    pyg.draw.line(Gdisplay,black,(100,y),(100,y+100),1)
    pyg.draw.line(Gdisplay,black,(200,y),(200,y+100),1)
    pyg.draw.line(Gdisplay,black,(300,y),(300,y+100),1)
    pyg.draw.line(Gdisplay,black,(400,y),(400,y+100),1)   
    pyg.draw.line(Gdisplay,black,(500,y),(500,y+100),1)
    pyg.draw.line(Gdisplay,black,(600,y),(600,y+100),1)    

def boundary_lines():
    pyg.draw.line(Gdisplay,black,(100,0),(100,800),5)
    pyg.draw.line(Gdisplay,black,(700,0),(700,800),5)

#function for creating hurdles (Here rectangles)
def objects(o_x,o_y,o_w,o_h,color):#x_object,y_object,w_object,h_onject,color_object
    pyg.draw.rect(Gdisplay,color,[o_x,o_y,o_w,o_h])
    
def objects1(o_x1,o_y1,o_w1,o_h1,color):#x_object,y_object,w_object,h_onject,color_object
    pyg.draw.rect(Gdisplay,color,[o_x1,o_y1,o_w1,o_h1])


#a function for displaying bike image to the screen
def bike(x,y):
    Gdisplay.blit(bikeImg,(x,y))
    
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface , textSurface.get_rect()
    
def message(text,scalar):
    text_large = pyg.font.Font('freesansbold.ttf',70)
    textSurface , textRect = text_objects(text,text_large)
    textRect.center = (width/2,height*scalar/2)
    Gdisplay.blit(textSurface,textRect)
    pyg.display.update()
    #t.sleep(2)
    
#function for new game screen
def new_game():
    game_ended = True
    while game_ended:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()  
        
        x1 = width*0.35
        y1 = height*0.25
        wid = 300
        hei = 300
        pyg.draw.rect(Gdisplay,black,(x1,y1,wid,hei))
        pyg.draw.line(Gdisplay,light_red,(x1,y1),(x1,y1+hei),4)
        pyg.draw.line(Gdisplay,light_red,(x1,y1),(x1+wid,y1),4)
        pyg.draw.line(Gdisplay,light_red,(x1+wid,y1),(x1+wid,y1+hei),4)
        pyg.draw.line(Gdisplay,light_red,(x1,y1+hei),(x1+wid,y1+hei),4)
        
        text = "New Game"
        buttons(text,green,x1+50,y1+50,200,50)
        
        text = "quit"
        buttons(text,red,x1+50,y1+200,200,50)
        mouse_pos = pyg.mouse.get_pos()
        if x1+50+200>mouse_pos[0]>x1 and y1+50+50>mouse_pos[1]>y1+50:
            text = "New Game"
            buttons(text,light_green,x1+50,y1+50,200,50)
            for event in pyg.event.get():
                if event.type == pyg.MOUSEBUTTONDOWN:
                    game_mainloop()
        else:
            text = "New Game"
            buttons(text,green,x1+50,y1+50,200,50)
        
        if x1+50+200>mouse_pos[0]>x1+50 and y1+200+50>mouse_pos[1]>y1+200:
            text = "quit"
            buttons(text,light_red,x1+50,y1+200,200,50)
            for event in pyg.event.get():
                if event.type == pyg.MOUSEBUTTONDOWN:
                    pyg.quit()    
        else:
            text = "quit"
            buttons(text,red,x1+50,y1+200,200,50)
        
        
        pyg.display.update()
    #    t.sleep(2)
    #    game_enter()
        
 # function for displaying a message when the player strikes an object or the 
 # boundries   
def crash(score):
    message('Oops! You crashed',1)
    message('SCORE : '+str(score),1.2)
    t.sleep(2)
    
    new_game()
#    game_mainloop()
    

#function for defining buttons the game
def buttons(text,color1,x_pos,y_pos,w,h):
    
    pyg.draw.rect(Gdisplay,color1,(x_pos,y_pos,w,h))
        
    text_small = pyg.font.Font('freesansbold.ttf',20)
    textSurface , textRect = text_objects(text,text_small)
    textRect.center = (x_pos+(w)/2,y_pos+(h)/2)
    Gdisplay.blit(textSurface,textRect)
    return

#function for pause
def pause():
    paused = True
    while paused:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()  
        
        x1 = width*0.35
        y1 = height*0.25
        wid = 300
        hei = 300
        pyg.draw.rect(Gdisplay,black,(x1,y1,wid,hei))
        pyg.draw.line(Gdisplay,light_red,(x1,y1),(x1,y1+hei),4)
        pyg.draw.line(Gdisplay,light_red,(x1,y1),(x1+wid,y1),4)
        pyg.draw.line(Gdisplay,light_red,(x1+wid,y1),(x1+wid,y1+hei),4)
        pyg.draw.line(Gdisplay,light_red,(x1,y1+hei),(x1+wid,y1+hei),4)
        
        text = "resume"
        buttons(text,green,x1+50,y1+50,200,50)
        
        text = "quit"
        buttons(text,red,x1+50,y1+200,200,50)
        mouse_pos = pyg.mouse.get_pos()
        if x1+50+200>mouse_pos[0]>x1 and y1+50+50>mouse_pos[1]>y1+50:
            text = "resume"
            buttons(text,light_green,x1+50,y1+50,200,50)
            for event in pyg.event.get():
                if event.type == pyg.MOUSEBUTTONDOWN:
                    paused = False
        else:
            text = "resume"
            buttons(text,green,x1+50,y1+50,200,50)
        
        if x1+50+200>mouse_pos[0]>x1+50 and y1+200+50>mouse_pos[1]>y1+200:
            text = "quit"
            buttons(text,light_red,x1+50,y1+200,200,50)
            for event in pyg.event.get():
                if event.type == pyg.MOUSEBUTTONDOWN:
                    pyg.quit()    
        else:
            text = "quit"
            buttons(text,red,x1+50,y1+200,200,50)
        
        
        pyg.display.update()
    #    t.sleep(2)
    #    game_enter()

#function for the primary page of the game
def game_enter():
    
    x_pos = 150
    y_pos = 450
    w = 100
    h = 50
    x_pos1 = 450
    y_pos1 = 450
    w1 = 100
    h1 = 50 
    
    crashed = False
    Gdisplay.fill(white)
    while not crashed:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()            
    
        text = "Dodge the Hurdles"
        text_small = pyg.font.Font('freesansbold.ttf',70)
        textSurface , textRect = text_objects(text,text_small)
        textRect.center = (width/2,height/2)
        Gdisplay.blit(textSurface,textRect)
        
        text = "START!"
        buttons(text,green,150,450,100,50)
        text = "QUIT"
        buttons(text,red,450,450,100,50)
        mouse_pos = pyg.mouse.get_pos()
        if x_pos+w>mouse_pos[0]>x_pos and y_pos+h>mouse_pos[1]>y_pos:
            text = "START!"
            buttons(text,light_green,150,450,100,50)
            for event in pyg.event.get():
                if event.type == pyg.MOUSEBUTTONDOWN:
                    game_mainloop()    
        else:
            text = "START!"
            buttons(text,green,150,450,100,50)
        
        if x_pos1+w1>mouse_pos[0]>x_pos1 and y_pos1+h1>mouse_pos[1]>y_pos1:
            text = "QUIT"
            buttons(text,light_red,450,450,100,50)
            for event in pyg.event.get():
                if event.type == pyg.MOUSEBUTTONDOWN:
                    pyg.quit()    
        else:
            text = "QUIT"
            buttons(text,red,450,450,100,50)
       
        pyg.display.update()



# The main game loop
def game_mainloop():
    # changing the position of bike
    x_change = 0    
    x = width*0.35
    y = height*0.8
    car_width = 120
    
    o_x = random.choice([100,200,300,400,500,600])
    o_y = -500
    o_w = 100
    o_h = 100
    o_speed = 5
    
    o_x1 = random.choice([100,200,300,400,500,600])
    o_y1 = -500
    o_w1 = 50
    o_h1 = 50
    o_speed1 = 7
    
    line_y=0
    line_y1=-400
    line_speed = 10
    
    
    
    score = 0
    dodged = score

    crashed = False
    while not crashed:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()            
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    x_change = -7
                if event.key == pyg.K_RIGHT:
                    x_change = 7
                if event.key == pyg.K_p:
                    pause()
            if event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT:
                    x_change = 0
                if event.key == pyg.K_RIGHT:
                    x_change = 0
                    
                    
        x = x + x_change
            
        Gdisplay.fill(white)
        bike(x,y)
        boundary_lines()
        dividers(line_y)
        text1 = "press p to"
        buttons(text1,light_green,700,0,100,50)
        text1 = "pause"
        buttons(text1,light_green,700,50,100,50)

        line_y+=line_speed
        dividers(line_y1)
        line_y1+=line_speed
        
        if line_y > height:
            line_y=-200
         
        if line_y1 > height:
            line_y1 = -200
        #objects(o_x,o_y,o_w,o_h,color):#x_object,y_object,w_object,h_onject,color_object
        objects(o_x,o_y,o_w,o_h,big_block)
        o_y+=o_speed
        
        objects1(o_x1,o_y1,o_w1,o_h1,red)
        o_y1+=o_speed1
        
        if x > width - car_width - 100 or x < 0 - car_width/2 + 100:
            crash(score)
            
        if o_y > height:
            o_y = 0 - o_h
            o_x = random.choice([100,200,300,400,500,600])
            score+=1
            
        if o_y1 > height:
            o_y1 = 0 - o_h1
            o_x1 = random.choice([100,200,300,400,500,600])
            score+=2
        
        score_game(score)
        #for introducing a challenge in the game
        if score > 3*dodged:
            dodged = score
            o_speed+=2
            o_speed1+=1
        
        if y < o_y + o_h - 20 :
            if x+70>o_x and x+70<o_x+o_w or x+car_width>o_x and x+car_width<o_x+o_w:
                crash(score)
        
        if y < o_y1 + o_h1 - 20 :
            if x+70>o_x1 and x+70<o_x1+o_w1 or x+car_width>o_x1 and x+car_width<o_x1+o_w1:
                crash(score)
        
        
        pyg.display.update()
        time.tick(60)
        
game_enter()
#game_mainloop()    
pyg.quit()

    
            