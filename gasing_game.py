import pygame
import sys
from pygame.locals import *
import random
#------------------------------colors-----------------------------------
blue=(0,0,255)
black=(0,0,0)
green=(0,255,0)
white=(255,255,255)
orange=(255,255,0)
dval=(0,255,255)
red=(255,0,0)
pink=(255,0,255)
#---------------------------shapes--------------------------------------
donut="donut"
circle="circle"
square="square"
triangle="triangle"
polygone="polygone"
allshapes=[donut,circle,triangle,polygone]
allshapes=allshapes[:]*2
allcolors=[black,green,orange,dval,red,pink]
#allcolors=allcolors[:]*2
list_items=[]
intetial_items=[]
cords=[]
intetial_shape="square"
cols=len(allshapes)
rows=len(allcolors)
assert (len(allcolors)*len(allshapes))%2==0,'the pair is incomplete.'
pygame.init()
#------------------------property---------------------------------------
s_height=470
s_weidth=680
rectx=190
fps=30
recty=100
width=20
all_x=[]
all_y=[]
message="this is the memory game"
copy_right="made by vikram gauda"
end_surface="Thanks fro playing"
end="press any key to the end the programe"
#---------------------inetial state-------------------------------------
screen=pygame.display.set_mode((s_weidth,s_height),0,32)
pygame.display.set_caption("memory game")
def draw_shape(shape,color,x_cord,y_cord):
    if shape==donut:
        pygame.draw.circle(screen,color,(x_cord+int(width/2),y_cord-int(width/2)),int(width/2),int(width/4))
    if shape==circle:
        pygame.draw.circle(screen,color,(x_cord+int(width/2),y_cord-int(width/2)),int(width/2),int(width/2))
    if shape==square:
        pygame.draw.rect(screen,color,(x_cord,y_cord,width-2,width-2))
    if shape==polygone:
        pygame.draw.polygon(screen,color,((x_cord,y_cord-int(width/2)),(x_cord+int(width/2),y_cord),(x_cord+int(width/2),y_cord-width),(x_cord+width,y_cord-int(width/2))))
    if shape==triangle:
        pygame.draw.polygon(screen,color,((x_cord+int(width/2),y_cord),(x_cord,y_cord-width),(x_cord+width,y_cord-width)))
    pygame.display.update()
def gameini(rectx,recty):
    x=1
    while x<=cols:
        y=1
        while y<=rows:
            pygame.draw.rect(screen,white,(rectx,recty,24,24))
            if rectx not in all_x:
            	all_x.append(rectx)
            if recty not in all_y:
            	all_y.append(recty)
            rectx+=40
            y+=1
            pygame.display.update() 
        x+=1
        rectx=190
        recty+=40      
def  gameSurface():
	screen.fill(blue)
	font=pygame.font.SysFont('arial',24)
	font_surface=font.render(message,True,orange,dval)
	patient=font.render(copy_right,True,black,blue)
	screen.blit(font_surface,(201,29))
	screen.blit(patient,(358,399))
	pygame.display.update()
def generate_labels():
	for shapes in allshapes:
		for color in allcolors:
			list_items.append((shapes,color))
	for y in all_y:
		for x in all_x:
			intetial_items.append((square,white))
			cords.append((x,y))
	random.shuffle(list_items)
def game_board(list_items1): 
	list_items2=list_items1
	assert len(list_items2)%len(cords)==0,'the items number error.'
	for first in range(len(list_items2)):
		for second in range(1):
			draw_shape(list_items2[first][second],list_items2[first][second+1],cords[first][second],cords[first][second+1])
def mouse_pos(p,q,time,first_selection,previous):
	m=0
	n=0
	for x,y in cords:
		if (p>=x and p<=x+24) and (q>=y and q<=y+24):
			intetial_items[m]=list_items[m]
			if time==1:
				first_selection=list_items[m]
				previous=m
				time+=1
				gameSurface()
				game_board(intetial_items)
			else:
				time=1
				gameSurface()
				game_board(intetial_items)
				if first_selection==list_items[m]:
					pass
				else:
					intetial_items[previous]=(square,white)
					intetial_items[m]=(square,white)
					gameSurface()
					game_board(intetial_items)
			m+=1
		else:
			m+=1
	return time,first_selection,previous
def winner_decider():
	if (square,white) not in intetial_items:
		gameSurface()
		font=pygame.font.SysFont('arial',32)
		#font1=pygame.font.SysFont('arial',14)
		font_surface=font.render(end_surface,True,orange,dval)
		#tip=font1.render(end,True,black,blue)
		screen.blit(font_surface,(119,170))
		#screen.blit(tip,(122,341))
def main():
	time=1
	first_selection=None
	previous=0
	gameSurface()
	gameini(rectx,recty)
	pygame.time.wait(1000)
	gameSurface()
	generate_labels()
	game_board(list_items)
	pygame.time.wait(50000)
	gameSurface()
	gameini(rectx,recty)
	while True:
		for events in pygame.event.get():
			if events.type==QUIT:
				exit()
			elif events.type==MOUSEBUTTONUP:
				mouse_x,mouse_y=events.pos
				time,first_selection,previous=mouse_pos(mouse_x,mouse_y,time,first_selection,previous)
				winner_decider()
		pygame.display.update()
if __name__ == '__main__':
	main() 
