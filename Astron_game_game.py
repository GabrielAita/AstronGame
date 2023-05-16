import pygame
from pygame.locals import *
from sys import exit
import math
from time import sleep
from Astron_Classes import *


pygame.init()

clock = pygame.time.Clock()

icon_voltar_n = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Voltar_normal.png').convert_alpha()
icon_voltar_n = pygame.transform.scale(icon_voltar_n, (60,40))
icon_voltar_oh = pygame.image.load('AstronGame-main\Sprites\Icon_Menu\Voltar_onhover.png').convert_alpha()
icon_voltar_oh = pygame.transform.scale(icon_voltar_oh, (60,40))

bg = pygame.image.load("teste_background.png").convert_alpha()

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
bullet = Bullet(p1,1)
bullet_group = pygame.sprite.Group()

#Enemy
enemy_group = pygame.sprite.Group()

#Level
lvl = Level()
lvl_group = pygame.sprite.Group()

timer = 0

score = 0

def game(MUSIC):

    global timer
    global score

    if MUSIC:
        pygame.mixer.music.load('AstronGame-main\musicas\Hopeful Feeling.mp3')
        pygame.mixer.music.play()

    pygame.mouse.set_visible(False)

    black = (0, 0, 0)
    white = (255, 255, 255)

    font = pygame.font.Font(None, 30)

    game_loop = True
    
    while game_loop:

        screen.blit(bg, (0,0))

        for bullet in bullet_group:

            bullet_group.draw(screen)

            if bullet.position[0] < 0 or bullet.position[0] > screenRes[0] or bullet.position[1] < 0 or bullet.position[1] > screenRes[1]:
                bullet_group.remove(bullet)
            if bullet.lifespam == 0:
                bullet_group.remove(bullet)
        


        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = [crosshair.rect.x,crosshair.rect.y]
                bullet_angle = math.atan2(mouse_position[1] - p1.positionY, mouse_position[0] - p1.positionX)
                bullet_velocity = [math.cos(bullet_angle), math.sin(bullet_angle)]
                bullet_group.add(Bullet(p1,bullet_velocity))

        # Inimigo
        if lvl.clear:
            if timer >= 60:
                if len(enemy_group) < 5:  
                    enemy_group.add(Enemy(random.randint(100,1000),random.randint(50,600)))

        # Colisão inimgo/bala
        for enemy in enemy_group:
            for bullet in bullet_group:
                if pygame.sprite.collide_rect(enemy,bullet):
                    enemy.hp -= 1
                    if enemy.hp <= 0:
                        enemy_group.remove(enemy)
                        score += 10
                        print(score)
                    bullet_group.remove(bullet)

        # Colisão imigo/player
        for enemy in enemy_group:
            for player in player_group:
                if pygame.sprite.collide_rect(enemy,player):
                    enemy_group.remove(enemy)
        
        # Update the screen

        player_group.draw(screen)
        player_group.update()
        bullet_group.update()
        enemy_group.draw(screen)
        enemy_group.update()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()
        

        # Set the FPS
        clock = pygame.time.Clock()

        # Update timer
        timer += 1
        
        clock.tick(60)

