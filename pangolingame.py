import pygame, sys
from pygame.locals import *
import math 
import time
import random
pygame.init()

green=(10,200,10)
red=(255,0,0)

display=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Pangolin")
panimage=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/pangolin.png")
background=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/forest.jpg")
pangolin_width=64




def food(ant_startx,ant_starty,ant):
	if ant==0:
		ant_come=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/ant1.jpg")
	if ant==1:
		ant_come=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/ant2.jpg")
	if ant==2:
		ant_come=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/ant3.jpg")
	display.blit(ant_come,(ant_startx,ant_starty)) 

def hunterx(hunter_startx,hunter_starty,hunter):
	if hunter==0:
		hunter_come=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/hunter.jpg")
	if hunter==1:
		hunter_come=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/trap.png")
	if hunter==2:
		hunter_come=pygame.image.load("C:/Users/Admin/Documents/code/Pygame/Resources/images/nettrap.png")

	display.blit(hunter_come,(hunter_startx,hunter_starty))		

font=pygame.font.Font("freesansbold.ttf",32)
ax=10
ay=10

score_value = 0
def show_score(score_x,score_y):
	score=font.render("SCORE: " + str(score_value), True, (255,255,255))
	display.blit(score,(score_x,score_y))

def death():
	message_display("Oops!")

def message_display(text):
	largetext=pygame.font.Font("freesansbold.ttf",80)
	textsurf,textrect=text_object(text,largetext)
	textrect.center=((400),(300))
	display.blit(textsurf,textrect)
	pygame.display.update()
	time.sleep(3)
	loop()

def text_object(text,font):
	textsurface=font.render(text,True,red)
	return textsurface,textsurface.get_rect()


def pangolin(x,y):
	display.blit(panimage, (x,y))

def loop():

	x=500
	y=500
	x_change=0
	y_change=0
	hunter_speed=5
	hunter=0
	hunter_startx=random.randrange(130,(1000-pangolin_width))
	hunter_starty=-600
	hunter_width=28
	hunter_height=50
	ant_speed=5
	ant=0
	ant_startx=random.randrange(130,(1000-pangolin_width))
	ant_starty=-600
	ant_width=20
	ant_height=20



	bumped=False
	while not bumped:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and x>0:
			x-=5
		if keys[pygame.K_RIGHT] and x<1000-pangolin_width: 
			x+=5

		display.fill(green)
		display.blit(background,(0,0))
		hunter_starty-=(hunter_speed/4)
		hunterx(hunter_startx,hunter_starty,hunter)
		hunter_starty+=hunter_speed
		ant_starty-=(ant_speed/4)
		food(ant_startx,ant_starty,ant)
		ant_starty+= ant_speed
		pangolin(x,y)
		if x<0 or x>1000-pangolin_width:
			x_change=0
		if ant_starty>600:
			ant_starty=0-ant_height
			ant_startx=random.randrange(130,(1000-300))
			ant=random.randrange(0,2)
		if hunter_starty>600:
			hunter_starty=0-hunter_height
			hunter_startx=random.randrange(130,(1000-300))
			hunter=random.randrange(0,2)

		if y<hunter_starty+hunter_height:
			if x >= hunter_startx and x <= hunter_startx + hunter_width:
				death() 
			if x + pangolin_width >= hunter_startx and x + pangolin_width <= hunter_width + hunter_startx:
				death()
			if x < hunter_startx and  hunter_startx + hunter_width < x + pangolin_width:
				death()
	
		if y<ant_starty+ant_height:
			if x < ant_startx and  ant_startx + ant_width < x + pangolin_width:
				score_value += 1 
		show_score(ax,ay)	
		pygame.display.update()
loop()
pygame.quit()
quit()
