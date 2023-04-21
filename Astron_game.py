import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screenRes =(1152,648)
screen = pygame.display.set_mode(screenRes, 0 ,32)

def menu():
    icone_sem_som = pygame.image.load('icon_sem_som.png').convert_alpha()
    icone_sem_som = pygame.transform.scale(icone_sem_som, (40,60))
    icone_com_som = pygame.image.load('icon_com_som.png').convert_alpha()
    icone_com_som = pygame.transform.scale(icone_com_som, (80,60))
    icone_som = icone_com_som
    icon_Iniciar = pygame.image.load('icon_Iniciar.png').convert_alpha()
    icon_Iniciar = pygame.transform.scale(icon_Iniciar, (150,50))
    icon_Logo = pygame.image.load('icon_Logo.png').convert_alpha()
    icon_Logo = pygame.transform.scale(icon_Logo, (400,100))
    icon_sair = pygame.image.load('icon_sair.png').convert_alpha()
    icon_sair = pygame.transform.scale(icon_sair, (100,50))

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
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= screenRes[0]/2-75 and pos[0] <= screenRes[0]/2+75 and pos[1] >= screenRes[1]/2 and pos[1] <= screenRes[1]/2+50:
                    pygame.draw.rect(screen,(0,255,255),(40,40,100,100))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= screenRes[0]/2-75 and pos[0] <= screenRes[0]/2+75 and pos[1] >= screenRes[1]/2 and pos[1] <= screenRes[1]/2+50:
                    game()
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= screenRes[0]/2-50 and pos[0] <= screenRes[0]/2+50 and pos[1] >= screenRes[1]/2 and pos[1] <= screenRes[1]/2+50:
                    pygame.draw.rect(screen,(0,255,255),(40,40,100,100))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= screenRes[0]/2-75 and pos[0] <= screenRes[0]/2+75 and pos[1] >= screenRes[1]/2 and pos[1] <= screenRes[1]/2+50:
                    pygame.quit()
            
            screen.blit(icone_som,(1000,550))
            screen.blit(icon_Logo,(screenRes[0]/2-200,screenRes[1]/2-200))
            screen.blit(icon_Iniciar,(screenRes[0]/2-75,screenRes[1]/2))
            screen.blit(icon_sair,(screenRes[0]/2-50,screenRes[1]/2+100))
            pygame.display.update()
        
def game():
    game = True

    while game:
        
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            screen.fill((255,255,255))
            pygame.draw.rect(screen,(255,255,0),(90,90,100,100))
            
            pos = pygame.mouse.get_pos()
            if pos[0] >= 90 and pos[0] <= 190 and pos[1] >= 90 and pos[1] <= 190:
               pygame.draw.rect(screen,(0,255,0),(90,90,100,100))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos >= (90,190) and pos <= (190,90):
                    menu()

            pygame.display.update()

menu()