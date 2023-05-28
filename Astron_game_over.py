import pygame
from pygame.locals import *
from sys import exit
from Astron_Classes import *
from Astron_image import *

pygame.init()

clock = pygame.time.Clock()

screenRes = (screen.get_width(),screen.get_height())














def gameover(score):

    letras1 = alfabeto
    cl1 = 0
    letras2 = alfabeto
    cl2 = 0
    letras3 = alfabeto
    cl3 = 0

    screen.fill((0,0,0))    
    gameover = True

    

    while gameover:

        pygame.mouse.set_visible(True)

        screen.blit(BG_GO,(screenRes[0]/2-BG_GO.get_width()/2,0))

        pos = pygame.mouse.get_pos()

        curretLetra1 = letras1[cl1]
        curretLetra2 = letras2[cl2]
        curretLetra3 = letras3[cl3]

        numero_string = str(score)
        digitos_lista = list(numero_string)
        pos_x = screenRes[0]/2 -70 
        pos_y = screenRes[1]/2 -70

        for i in range(len(digitos_lista)):
            varScore = int(digitos_lista[i])
            screen.blit(pygame.transform.scale(pygame.image.load(f"AstronGame-main/Sprites/Numeros/N{varScore}.png"),(50,50)), (pos_x, pos_y))
            pos_x += 20

        for event in pygame.event.get():
            if pos[1] >= screenRes[1]/2 and pos[1] <= screenRes[1]/2 +seta_cima.get_height():
                if pos[0] >= screenRes[0]/2-curretLetra1.get_width()/2 - 116 + seta_cima.get_width()/2 and pos[0] <= screenRes[0]/2-curretLetra1.get_width()/2 - 116 + seta_cima.get_width()/2 + seta_cima.get_width():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cl1 += 1
                        if cl1 == len(letras1):
                            cl1 = 0 
                if pos[0] >= screenRes[0]/2-curretLetra2.get_width()/2-96 + seta_cima.get_width()/2 + 77 and pos[0] <= screenRes[0]/2-curretLetra2.get_width()/2-96 + seta_cima.get_width()/2 + 77 + seta_cima.get_width():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cl2 += 1
                        if cl2 == len(letras1):
                            cl2 = 0 
                if pos[0] >= screenRes[0]/2-curretLetra2.get_width()/2-96 + seta_cima.get_width()/2 + 173 and pos[0] <= screenRes[0]/2-curretLetra2.get_width()/2-96 + seta_cima.get_width()/2 + 173 + seta_cima.get_width():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cl3 += 1
                        if cl3 == len(letras1):
                            cl3 = 0 

            if pos[1] >= screenRes[1]/2 +155 and pos[1] <= screenRes[1]/2 + 155 + seta_cima.get_height():
                if pos[0] >= screenRes[0]/2-curretLetra1.get_width()/2 - 116 + seta_cima.get_width()/2 and pos[0] <= screenRes[0]/2-curretLetra1.get_width()/2 - 116 + seta_cima.get_width()/2 + seta_cima.get_width():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cl1 <= 0:
                            cl1 = len(letras1)-1
                        else:
                            cl1 -= 1
                if pos[0] >= screenRes[0]/2-curretLetra1.get_width()/2 - 19 + seta_cima.get_width()/2 and pos[0] <= screenRes[0]/2-curretLetra1.get_width()/2 - 19 + seta_cima.get_width()/2 + seta_cima.get_width():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cl2 <= 0:
                            cl2 = len(letras1)-1
                        else:
                            cl2 -= 1
                if pos[0] >= screenRes[0]/2-curretLetra1.get_width()/2 + 77 + seta_cima.get_width()/2 and pos[0] <= screenRes[0]/2-curretLetra1.get_width()/2 + 77 + seta_cima.get_width()/2 + seta_cima.get_width():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cl3 <= 0:
                            cl3 = len(letras1)-1
                        else:
                            cl3 -= 1

        if pos[0] >= screenRes[0]/2-CONTINUAR.get_width()/2 and pos[0] <= screenRes[0]/2+CONTINUAR.get_width()/2:
            if pos[1] >= screenRes[1]-200 and pos[1]< screenRes[1]-200 +CONTINUAR.get_height():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return[cl1,cl2,cl3,score]
                    
                
           

        
        screen.blit(seta_cima,(screenRes[0]/2-curretLetra1.get_width()/2-96 - 20 + seta_cima.get_width()/2,screenRes[1]/2)) 
        screen.blit(seta_cima,(screenRes[0]/2-curretLetra2.get_width()/2-96 + seta_cima.get_width()/2 + 77,screenRes[1]/2)) 
        screen.blit(seta_cima,(screenRes[0]/2-curretLetra3.get_width()/2-96 + seta_cima.get_width()/2 + 173,screenRes[1]/2)) 
        screen.blit(seta_baixo,(screenRes[0]/2-curretLetra1.get_width()/2-96 - 20 + seta_cima.get_width()/2,screenRes[1]/2+155)) 
        screen.blit(seta_baixo,(screenRes[0]/2-curretLetra2.get_width()/2-96 + 77 + seta_cima.get_width()/2,screenRes[1]/2+155))
        screen.blit(seta_baixo,(screenRes[0]/2-curretLetra3.get_width()/2-96 + 173 + seta_cima.get_width()/2,screenRes[1]/2+155))

        screen.blit(curretLetra1,(screenRes[0]/2-curretLetra1.get_width()/2-86 -15,screenRes[1]/2+60))
        screen.blit(curretLetra2,(screenRes[0]/2-curretLetra2.get_width()/2+10 -15,screenRes[1]/2+60))
        screen.blit(curretLetra3,(screenRes[0]/2-curretLetra3.get_width()/2+106 -15,screenRes[1]/2+60))

        screen.blit(CONTINUAR,(screenRes[0]/2-CONTINUAR.get_width()/2,screenRes[1]-200))
        pygame.display.update()