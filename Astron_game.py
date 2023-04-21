import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen =(1152,648)
screen = pygame.display.set_mode(screen, 0 ,32)

def menu():
    icone_sem_som = pygame.image.load('icon_sem_som.png').convert_alpha()
    icone_sem_som = pygame.transform.scale(icone_sem_som, (40,60))
    icone_com_som = pygame.image.load('icon_com_som.png').convert_alpha()
    icone_com_som = pygame.transform.scale(icone_com_som, (74,60))
    icone_som = icone_sem_som

    intro = True

    while intro:
        for event in pygame.event.get():
            screen.fill((255,255,255))
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            q1=pygame.draw.rect(screen,(255,255,0),(40,40,100,100))
            
            pos = pygame.mouse.get_pos()

            if pos[0] >= 40 and pos[0] <= 140 and pos[1] >= 40 and pos[1] <= 140:
               pygame.draw.rect(screen,(0,255,0),(40,40,100,100))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos >= (40,140) and pos <= (140,40):
                    game()
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= 1000 and pos[0] <= 1040 and pos[1] >= 550 and pos[1] <= 610:
                    if icone_som == icone_com_som:
                        icone_som = icone_sem_som
                    elif icone_som == icone_sem_som:   
                        icone_som = icone_com_som 
            
            screen.blit(icone_som,(1000,550))
            pygame.display.update()
        
def game():
    game = True

    while game:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

            pygame.draw.rect(screen,(255,255,0),(90,90,100,100))
            screen.fill((255,255,255))
            pygame.display.update()
menu()