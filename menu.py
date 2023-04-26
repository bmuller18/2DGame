import pygame as game, sys
from pygame.locals import *
import Resources.colors as colors
import settings
import Buildings.farm as farm
import Buildings.my_resources

#Siempre ejecutar esta funcion
game.init()

#Screen config
screen = game.display.set_mode((settings.w, settings.h))#Resolution from settings (width, height)
game.display.set_caption('First game')#Game title

#Back color game
screen.fill((43, 52, 119))
#Start Button
start_game = Rect(100, 100, 150, 50)#Button configure (Xpos, Ypos, width,)
startgame = game.font.SysFont("Arial", 30)
startbtn = startgame.render("Grow Grain", True, (50, 100, 150))

#mantiene la ventana ejecutandose constantemente
while True:
    for event in game.event.get():
        if event.type == QUIT:
            game.quit()
            sys.exit()
        game.draw.rect(screen, (50, 50, 100), start_game, 0)
        game.draw.rect(screen, (50, 60, 110), start_game, 3)
        
        # Borra la superficie de la ventana
        screen.fill((43, 52, 119))
        
        # Renderiza el texto actualizado
        fuente = game.font.Font(None, 36)
        texto = fuente.render("Grain: "+str(Buildings.my_resources.grain), True, (0, 0, 0))
        texto = fuente.render("Grain: "+str(Buildings.my_resources.grain), True, (50, 0, 0))
        
        #Click Button
        if event.type == MOUSEBUTTONDOWN:
            if start_game.collidepoint(event.pos):
                farm.grain()#make grain in building
        
        #Center X position text function-->(width buton + (button.width - text.get_with())/2, "height")
        #Center y position text function-->(height buton + ("width", button.height - text.height())/2)
        screen.blit(startbtn, (100+(start_game.width-startbtn.get_width())/2,100+(start_game.height - startbtn.get_height())/2))
    
        #Draw text into button rect
        screen.blit(texto, (10, 10))
        game.display.update()
