import pygame
from pygame.locals import *
from sys import exit
from Astron_game_game import game
from Astron_image import alfabeto_mini













pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screenRes =(screen.get_width(),screen.get_height())
# Icones Menu
card_rank = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\card_rank.png"), (512,screenRes[1]-100))
instrucoes = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\card_instrucoes.png').convert_alpha()
instrucoes = pygame.transform.scale(instrucoes, (1300,900))

background = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\Background_logo.png"), screenRes)
background_instrus = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\Background_instrus.png"), screenRes)
background_no_logo = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Menu\Background_no_logo.png"), screenRes)

icone_sem_som_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_off_normal.png').convert_alpha()
icone_sem_som_n = pygame.transform.scale(icone_sem_som_n, (74,54))
icone_com_som_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_on_normal.png').convert_alpha()
icone_com_som_n = pygame.transform.scale(icone_com_som_n, (74,54))
icone_sem_som_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_off_onhover.png').convert_alpha()
icone_sem_som_oh = pygame.transform.scale(icone_sem_som_oh, (74,54))
icone_com_som_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\musica_on_onhover.png').convert_alpha()
icone_com_som_oh = pygame.transform.scale(icone_com_som_oh, (74,54))

icone_Instrucoes_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Instruções_normal.png').convert_alpha()
icone_Instrucoes_n = pygame.transform.scale(icone_Instrucoes_n, (326,90))
icone_Instrucoes_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Instruções_onhover.png').convert_alpha()
icone_Instrucoes_oh = pygame.transform.scale(icone_Instrucoes_oh, (326,90))

icon_Iniciar_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\iniciar_normal.png').convert_alpha()
icon_Iniciar_n = pygame.transform.scale(icon_Iniciar_n, (200,78))
icon_Iniciar_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\iniciar_onhover.png').convert_alpha()
icon_Iniciar_oh = pygame.transform.scale(icon_Iniciar_oh, (200,78))

icon_sair_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\sair_normal.png').convert_alpha()
icon_sair_n = pygame.transform.scale(icon_sair_n, (134,78))
icon_sair_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\sair_onhover.png').convert_alpha()
icon_sair_oh = pygame.transform.scale(icon_sair_oh, (134,78))

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
global Rank
Rank = [[2,3,4,100],[9,3,24,1000],[0,0,0,690],[17,16,13,90],[10,23,18,900]]

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
            if pos[0] >= screen.get_width()-150 and pos[0] <= screen.get_width()-150+icone_som.get_width() and pos[1] >= screen.get_height()-100 and pos[1] <= screen.get_height()-100+icone_som.get_height():
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
            if pos[0] >= screen.get_width()-330 and pos[0] <= screen.get_width()-330+icon_rank_oh.get_width() and pos[1] >= screen.get_height()-100 and pos[1] <= icon_rank_oh.get_height()+screen.get_height()-100:
                icon_rank = icon_rank_oh
                if event.type == pygame.MOUSEBUTTONDOWN:       
                    placar()
            else:
                icon_rank = icon_rank_n

            # Iniciar
            if pos[0] >= 110 and pos[0] <= 110+icon_Iniciar.get_width() and pos[1] >= 350 and pos[1] <= icon_Iniciar.get_height()+350:
                icon_Iniciar = icon_Iniciar_oh
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Rank.append(game(MUSIC))
            else:
                icon_Iniciar = icon_Iniciar_n

            # Instruções
            if pos[0] >= 110 and pos[0] <= 110+icone_Instrucoes.get_width() and pos[1] >= 450 and pos[1] <= icone_Instrucoes.get_height()+450:
                icone_Instrucoes = icone_Instrucoes_oh
                if event.type == pygame.MOUSEBUTTONDOWN: 
                  controles() 
            else:
                icone_Instrucoes = icone_Instrucoes_n 

            # Sair 
            if pos[0] >= 110 and pos[0] <= 110+icon_sair.get_width() and pos[1] >= 550 and pos[1] <= icon_sair.get_height()+550:
                icon_sair = icon_sair_oh
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro = False
                    pygame.quit()
                    quit()
            else:
                icon_sair = icon_sair_n
             
            screen.blit(background, (0, 0))
            screen.blit(icone_som,(screen.get_width()-150,screen.get_height()-100))
            screen.blit(icon_rank,(screen.get_width()-330,screen.get_height()-100))
            screen.blit(icon_Iniciar,(110,350))
            screen.blit(icone_Instrucoes,(110,450))  
            screen.blit(icon_sair,(110,550))  
            pygame.display.update()

def controles():
    
    control = True

    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            
        screen.blit(background,(0,0))
        screen.blit(instrucoes,(screenRes[0]/2-instrucoes.get_width()/2,screenRes[1]/2-instrucoes.get_height()/2))

        pygame.display.update()

def placar():
    global Rank 

    Rank = ordenar_decrescente(Rank)    
    
    ranks = True
    print(Rank)
    while ranks:
        pos_y = 100

        screen.blit(background_no_logo,(0,0))  
        screen.blit(card_rank,(100,50)) 

        for i in range(5):
            if i - 1 < len(Rank):
                L_pos_x = 150
                pos_y += 100
                N_pos_x = 400
                numero_string = str(Rank[i][3])
                digitos_lista = list(numero_string)

                for j in range(len(digitos_lista)):
                    varScore = int(digitos_lista[j])
                    screen.blit(pygame.transform.scale(pygame.image.load(f"AstronGame-main/Sprites/Numeros/N{varScore}.png"), (50, 50)), (N_pos_x, pos_y))
                    N_pos_x += 20

                for h in range(3):
                    screen.blit(alfabeto_mini[Rank[i][h]], (L_pos_x, pos_y)) 
                    L_pos_x += 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                return


          
        pygame.display.update()

def ordenar_decrescente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][3] < lista[j][3]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

pygame.mixer.music.load('AstronGame-main\musicas\musicamenu.mp3')
pygame.mixer.music.play()
menu()
