import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screenRes =(1152,648)
screen = pygame.display.set_mode(screenRes, 0 ,32)



def menu():
    pygame.mixer.music.load('AstronGame-main\musicas\musicamenu.mp3')
    pygame.mixer.music.play()
    background = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\Background_logo.png"), screenRes)
    icone_sem_som = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_off_normal.png').convert_alpha()
    icone_sem_som = pygame.transform.scale(icone_sem_som, (74,54))
    icone_com_som = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_on_onhover.png').convert_alpha()
    icone_com_som = pygame.transform.scale(icone_com_som, (74,54))
    icone_Instrucoes = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Instruções_normal.png').convert_alpha()
    icone_Instrucoes = pygame.transform.scale(icone_Instrucoes, (294,78))
    icone_som = icone_com_som
    icon_Iniciar = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\iniciar_normal.png').convert_alpha()
    icon_Iniciar = pygame.transform.scale(icon_Iniciar, (168,66))
    icon_sair = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\sair_normal.png').convert_alpha()
    icon_sair = pygame.transform.scale(icon_sair, (102,66))

    intro = True

    while intro:
        for event in pygame.event.get():
            screen.fill((255,255,255))
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            q1=pygame.draw.rect(screen,(255,255,0),(40,40,100,100))
            pygame.draw.rect(screen,(255,255,0),(1000,550,74,54))
            pygame.draw.rect(screen,(255,255,0),(screenRes[0]/2-75,screenRes[1]/2,168,68))
            pygame.draw.rect(screen,(255,255,0),(screenRes[0]/2-50,screenRes[1]/2+100,102,66))
            pos = pygame.mouse.get_pos()

            if pos[0] >= 40 and pos[0] <= 140 and pos[1] >= 40 and pos[1] <= 140:
               pygame.draw.rect(screen,(0,255,0),(40,40,100,100))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos >= (40,140) and pos <= (140,40):
                    game()
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= 1000 and pos[0] <= 1074 and pos[1] >= 550 and pos[1] <= 604:
                    if icone_som == icone_com_som:
                        icone_som = icone_sem_som
                    elif icone_som == icone_sem_som:   
                        icone_som = icone_com_som 
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= screenRes[0]/2-75 and pos[0] <= screenRes[0]/2+75 and pos[1] >= screenRes[1]/2 and pos[1] <= screenRes[1]/2+50:
                    game()
                    
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos[0] >= screenRes[0]/2-50 and pos[0] <= screenRes[0]/2+50 and pos[1] >= screenRes[1]/2+100 and pos[1] <= screenRes[1]/2+150:
                    intro = False
                    pygame.quit()
                    quit()
            
            screen.blit(background, (0, 0))
            screen.blit(icone_som,(1000,550))
            screen.blit(icon_Iniciar,(screenRes[0]/2-500,screenRes[1]/2-90))
            screen.blit(icon_sair,(screenRes[0]/2-500,screenRes[1]/2+65))
            screen.blit(icone_Instrucoes,(screenRes[0]/2-500,screenRes[1]/2-10))
            
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
            
            pygame.mixer.music.load('AstronGame-main\musicas\Hopeful Feeling.mp3')
            pygame.mixer.music.play()

            pos = pygame.mouse.get_pos()

           
            if pos[0] >= 90 and pos[0] <= 190 and pos[1] >= 90 and pos[1] <= 190:
               pygame.draw.rect(screen,(0,255,0),(90,90,100,100))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pos >= (90,190) and pos <= (190,90):
                    menu()

            
            pygame.display.update()

menu()
