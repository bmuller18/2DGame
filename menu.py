import pygame, sys
from pygame.locals import *
import Resources.colors as colors
import images as img

#Siempre ejecutar esta funcion
pygame.init()

#Screen config
screen = pygame.display.set_mode((1000, 600))#Resolution
pygame.display.set_caption('First game')#Titulo de la ventana
screen.fill(colors.rojo)

#import images from python file
pygame.display.set_icon(img.icon)
screen.blit(img.bg, (0,0))#position of image
#mantiene la ventana ejecutandose constantemente
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()