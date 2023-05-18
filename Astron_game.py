import pygame
from pygame.locals import *
from sys import exit
from Astron_game_game import game

pygame.init()
screenRes =(1152,648)
screen = pygame.display.set_mode(screenRes, pygame.FULLSCREEN)

# Icones Menu
instrucoes = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\card_instrucoes.png').convert_alpha()
instrucoes = pygame.transform.scale(instrucoes, (1300,900))

background = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\Background_logo.png"), screenRes)
background_instrus = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\Background_instrus.png"), screenRes)

icone_sem_som_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_off_normal.png').convert_alpha()
icone_sem_som_n = pygame.transform.scale(icone_sem_som_n, (74,54))
icone_com_som_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_on_normal.png').convert_alpha()
icone_com_som_n = pygame.transform.scale(icone_com_som_n, (74,54))
icone_sem_som_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_off_onhover.png').convert_alpha()
icone_sem_som_oh = pygame.transform.scale(icone_sem_som_oh, (74,54))
icone_com_som_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_on_onhover.png').convert_alpha()
icone_com_som_oh = pygame.transform.scale(icone_com_som_oh, (74,54))

icone_Instrucoes_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Instruções_normal.png').convert_alpha()
icone_Instrucoes_n = pygame.transform.scale(icone_Instrucoes_n, (294,78))
icone_Instrucoes_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Instruções_onhover.png').convert_alpha()
icone_Instrucoes_oh = pygame.transform.scale(icone_Instrucoes_oh, (294,78))

icon_Iniciar_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\iniciar_normal.png').convert_alpha()
icon_Iniciar_n = pygame.transform.scale(icon_Iniciar_n, (168,66))
icon_Iniciar_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\iniciar_onhover.png').convert_alpha()
icon_Iniciar_oh = pygame.transform.scale(icon_Iniciar_oh, (168,66))

icon_sair_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\sair_normal.png').convert_alpha()
icon_sair_n = pygame.transform.scale(icon_sair_n, (102,66))
icon_sair_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\sair_onhover.png').convert_alpha()
icon_sair_oh = pygame.transform.scale(icon_sair_oh, (102,66))

icon_rank_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Rank_normal.png').convert_alpha()
icon_rank_n = pygame.transform.scale(icon_rank_n, (160,54))
icon_rank_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Rank_onhover.png').convert_alpha()
icon_rank_oh = pygame.transform.scale(icon_rank_oh, (160,54))

icon_voltar_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Voltar_normal.png').convert_alpha()
icon_voltar_n = pygame.transform.scale(icon_voltar_n, (60,40))
icon_voltar_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Voltar_onhover.png').convert_alpha()
icon_voltar_oh = pygame.transform.scale(icon_voltar_oh, (60,40))

# Musica
pygame.mixer.music.load('AstronGame-main\musicas\musicamenu.mp3')
pygame.mixer.music.play()

global MUSIC 
MUSIC = True

def menu():

    global MUSIC 

    icone_som = icone_com_som_n
    icon_rank = icon_rank_n
    icon_Iniciar = icon_Iniciar_n
    icone_Instrucoes = icone_Instrucoes_n
    icon_sair = icon_sair_n

    intro = True

    while intro:
        
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            pos = pygame.mouse.get_pos()

            #Som
            if pos[0] >= 1000 and pos[0] <= 1074 and pos[1] >= 550 and pos[1] <= 604:
                if MUSIC == True:
                    icone_som = icone_com_som_oh
                elif MUSIC == False:   
                    icone_som = icone_sem_som_oh
                if event.type == pygame.MOUSEBUTTONDOWN:   
                    if MUSIC == True:
                        icone_som = icone_sem_som_oh
                        pygame.mixer.music.stop() 
                        MUSIC = False
                    elif MUSIC == False:   
                        icone_som = icone_com_som_oh 
                        pygame.mixer.music.play() 
                        MUSIC = True 
            else:
                if MUSIC == True:
                    icone_som = icone_com_som_n
                elif MUSIC == False:   
                    icone_som = icone_sem_som_n 
                     
            
            # Rank 
            if pos[0] >= 830 and pos[0] <= 830+icon_rank_oh.get_width() and pos[1] >= 550 and pos[1] <= icon_rank_oh.get_height()+550:
                icon_rank = icon_rank_oh
                if event.type == pygame.MOUSEBUTTONDOWN:       
                    intro = False
                    pygame.quit()
                    quit()
            else:
                icon_rank = icon_rank_n

            # Iniciar
            if pos[0] >= 74 and pos[0] <= 74+icon_Iniciar.get_width() and pos[1] >= 235 and pos[1] <= icon_Iniciar.get_height()+235:
                icon_Iniciar = icon_Iniciar_oh
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game(MUSIC)
            else:
                icon_Iniciar = icon_Iniciar_n

            # Instruções
            if pos[0] >= 74 and pos[0] <= 74+icone_Instrucoes.get_width() and pos[1] >= 315 and pos[1] <= icone_Instrucoes.get_height()+315:
                icone_Instrucoes = icone_Instrucoes_oh
                if event.type == pygame.MOUSEBUTTONDOWN: 
                  controles() 
            else:
                icone_Instrucoes = icone_Instrucoes_n 

            # Sair 
            if pos[0] >= 74 and pos[0] <= 74+icon_sair.get_width() and pos[1] >= 395 and pos[1] <= icon_sair.get_height()+395:
                icon_sair = icon_sair_oh
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro = False
                    pygame.quit()
                    quit()
            else:
                icon_sair = icon_sair_n
             
            screen.blit(background, (0, 0))
            screen.blit(icone_som,(1000,550))
            screen.blit(icon_rank,(830,550))
            screen.blit(icon_Iniciar,(screenRes[0]/2-500,screenRes[1]/2-90))
            screen.blit(icon_sair,(screenRes[0]/2-500,screenRes[1]/2+65))
            screen.blit(icone_Instrucoes,(screenRes[0]/2-500,screenRes[1]/2-10))    

            pygame.display.update()

def controles():
    
    control = True

    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu()
        screen.blit(background,(0,0))
        screen.blit(instrucoes,(screenRes[0]/2-instrucoes.get_width()/2,screenRes[1]/2-instrucoes.get_height()/2))

        pygame.display.update()

pygame.mixer.music.load('AstronGame-main\musicas\musicamenu.mp3')
pygame.mixer.music.play()
menu()
