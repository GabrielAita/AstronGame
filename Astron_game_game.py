import pygame
from pygame.locals import *
from sys import exit
import math
import random
from Astron_Classes import *


pygame.init()
screenRes =(1152,648)
screen = pygame.display.set_mode(screenRes, 0 ,32)



clock = pygame.time.Clock()

icon_voltar_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Voltar_normal.png').convert_alpha()
icon_voltar_n = pygame.transform.scale(icon_voltar_n, (60,40))
icon_voltar_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Voltar_onhover.png').convert_alpha()
icon_voltar_oh = pygame.transform.scale(icon_voltar_oh, (60,40))

# Player
p1 = Player("abc",1,screenRes[0]/2,screenRes[1]/2)
player_group = pygame.sprite.Group()
player_group.add(p1)
player_position = [screenRes[0]/2, screenRes[1]/2]

#Crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Bullet
bullet = Bullet(p1,2)
bullet_group = pygame.sprite.Group()


def game(MUSIC):

    if MUSIC:
        pygame.mixer.music.load('AstronGame-main\musicas\Hopeful Feeling.mp3')

    icon_voltar = icon_voltar_n

    pygame.mouse.set_visible(False)

    krebber = Enemy(30,1)

    black = (0, 0, 0)
    white = (255, 255, 255)

    # Set the font
    font = pygame.font.Font(None, 30)

    # Set the game loop
    game_loop = True
    
    while game_loop:

        #musica
        if MUSIC == True:
            pygame.mixer.music.play()
        if MUSIC == False:
            pygame.mixer.music.stop()

        screen.fill(white)



        # Draw the bullets
        for bullet in bullet_group:
            bullet_group.draw(screen)

        # Remove the bullets that are off the screen
        for bullet in bullet_group:
            if bullet.position[0] < 0 or bullet.position[0] > screenRes[0] or bullet.position[1] < 0 or bullet.position[1] > screenRes[1]:
                bullet_group.remove(bullet)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                bullet_angle = math.atan2(mouse_position[1] - p1.positionX, mouse_position[0] - p1.positionY)
                bullet_velocity = [math.cos(bullet_angle), math.sin(bullet_angle)]
                bullet_group.add(Bullet(p1,bullet_velocity))

        #Player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_position[0] > 0:
            player_position[0] -= 5
        if keys[pygame.K_d] and player_position[0] < screenRes[0] - 50:
            player_position[0] += 5
        if keys[pygame.K_w] and player_position[1] > 0:
            player_position[1] -= 5
        if keys[pygame.K_s] and player_position[1] < screenRes[1] - 50:
            player_position[1] += 5 

        #seta voltar

        pos = pygame.mouse.get_pos()

        if pos[0] >= 40 and pos[0] <= 40+icon_voltar.get_width() and pos[1] >= 40 and pos[1] <= icon_voltar.get_height()+40:
            icon_voltar = icon_voltar_oh
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.load('AstronGame-main\musicas\musicamenu.mp3')
                
        else:
            icon_voltar = icon_voltar_n
        
        # Update the screen
        player_group.draw(screen)
        player_group.update()
        crosshair_group.draw(screen)
        crosshair_group.update()
        bullet_group.update()
        pygame.display.update()
        

        # Set the FPS
        clock = pygame.time.Clock()
        
        clock.tick(60)

