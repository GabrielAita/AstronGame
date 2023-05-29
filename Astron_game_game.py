import pygame
from pygame.locals import *
from sys import exit
import math
import time
from Astron_Classes import *
from Astron_game_over import gameover
import random


pygame.init()

clock = pygame.time.Clock()

screenRes = (screen.get_width(),screen.get_height())

audio_comendo = pygame.mixer.Sound("AstronGame-main/sonszinhos/comendo 2.wav")
tiro = pygame.mixer.Sound("AstronGame-main/sonszinhos/tiro.wav")
bixo_morrendo = pygame.mixer.Sound("AstronGame-main/sonszinhos/bixo morrendo.wav")
player_damage = pygame.mixer.Sound("AstronGame-main/sonszinhos/prota morrendo.wav")


def game(MUSIC):

    bg = pygame.transform.scale(pygame.image.load("background laboratorio2.png").convert_alpha(),screenRes)

    p1 = Player("abc",1,screenRes[0]/2,screenRes[1]/2)
    player_group = pygame.sprite.Group()
    player_group.add(p1)

    #Crosshair
    crosshair = Crosshair()
    crosshair_group = pygame.sprite.Group()
    crosshair_group.add(crosshair)

    #Bullet
    bullet = Bullet(p1,1)
    bullet_group = pygame.sprite.Group()

    #Enemy
    enemy_group = pygame.sprite.Group()
    enemy_spawnwed = 5
    enemy_killed = 0

    #Level
    lvl = Level()

    #Comida
    food_group = pygame.sprite.Group()

    #Stamina
    stam_group = pygame.sprite.Group()

    y = 120
    for i in range(25):
        stam_group.add(Raio(p1, 30+y,80))
        y += 5

    

    timer = 0
    tempo_inicial = time.time()

    score = 0
    bg_s = pygame.transform.scale(pygame.image.load("AstronGame-main/Sprites/Numeros/BG_SCORE.png"),(200,150))
    varScore = 0 

    if MUSIC:
        pygame.mixer.music.load('AstronGame-main/musicas/Hopeful Feeling.mp3')
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.mixer.music.play()

    pygame.mouse.set_visible(False)

    game_loop = True
    
    while game_loop:
        if MUSIC:   
            if pygame.mixer.music.get_busy() == 0:
                pygame.mixer.music.play()

        hb=pygame.image.load(f'AstronGame-main/Sprites/barra de vida/barra {p1.hp}.png').convert_alpha()

        # End condition
        if p1.stamina == 0:
            game_loop = False
            print("Exausto")
            return gameover(score)
            
        if p1.hp == 0:
            game_loop = False
            print("Morreu")
            return gameover(score)

        # Show score
        numero_string = str(score)
        digitos_lista = list(numero_string)
        pos_x = screenRes[0]-150
        pos_y = 30

        

        screen.blit(bg, (0,0))
        screen.blit(bg_s,(screenRes[0]-200,-20))
        screen.blit(hb,(10,10))

        for i in range(len(digitos_lista)):
            varScore = int(digitos_lista[i])
            screen.blit(pygame.transform.scale(pygame.image.load(f"AstronGame-main/Sprites/Numeros/N{varScore}.png"),(50,50)), (pos_x, pos_y))
            pos_x += 20
        
        
        # timer segundos
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial

        if tempo_decorrido >= 1.5:
            p1.stamina -= 1
            print(p1.stamina)
            tempo_inicial = time.time()
            stam_group.remove(stam_group.sprites()[-1])

        # Remove Bullets
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
                if MUSIC:
                    tiro.play()
                mouse_position = [crosshair.rect.x,crosshair.rect.y]
                bullet_angle = math.atan2(mouse_position[1] - p1.positionY, mouse_position[0] - p1.positionX)
                bullet_velocity = [math.cos(bullet_angle), math.sin(bullet_angle)]
                bullet_group.add(Bullet(p1,bullet_velocity))

        # Inimigo
        if lvl.clear:
            if timer >= 60:
                if len(enemy_group) < enemy_spawnwed:  
                    temp = random.randint(0,3)
                    if temp == 0:
                        position = (random.randint(-200,0),random.randint(224,424))
                    if temp == 1:
                        position = (random.randint(screenRes[0],screenRes[0]+200),random.randint(224,424))
                    if temp == 2:
                        position = (random.randint(476,676),random.randint(-200,0))
                    if temp == 3:
                        position = (random.randint(476,676),random.randint(screenRes[1],screenRes[1]+200))
                    
                    if enemy_killed >= 50:
                        enemy_spawnwed = 7
                        enemy.MAX_SPEED = 8
                        
                    enemy_group.add(Enemy(position[0],position[1],p1))

        # Colisão inimgo/bala
        for enemy in enemy_group:
            for bullet in bullet_group:
                if pygame.sprite.collide_rect(enemy,bullet):
                    if MUSIC:
                        bixo_morrendo.play()
                    enemy.hp -= 1
                    if enemy.hp <= 0:
                        enemy_group.remove(enemy)
                        bullet_group.remove(bullet)
                        score += 10
                        enemy_killed += 1
                        print(score)
                        if random.randint(1,3) == 1:
                            food_group.add(Food(enemy.rect.x,enemy.rect.y))
                        
        # Colisão imigo/player
        for enemy in enemy_group:
            for player in player_group:
                    if pygame.sprite.collide_rect(enemy,player):
                        if MUSIC:
                            player_damage.play()
                        enemy_group.remove(enemy)
                        player.hp -= 1
                        if player.hp == 0:
                            break
                        player.takingDamage()
                        if tempo_decorrido >= 1:
                           player.imunityFrame(player.hp)

        # Colisão player/food
        for food in food_group:
            if tempo_decorrido >= 5:
                food_group.remove(food)
            for player in player_group:
                if pygame.sprite.collide_rect(food,player):
                    if MUSIC:
                        audio_comendo.play()
                    food_group.remove(food)
                    energy_now = player.stamina
                    player.stamina += 10
                    if player.stamina >= 25:
                        player.stamina = 25
                    while player.stamina - energy_now >=0:
                        if energy_now == 25:
                            break
                        stam_group.add(Raio(p1, 5+stam_group.sprites()[-1].rect.center[0],80))
                        energy_now += 1

        
        # Update the screen

        player_group.draw(screen)
        player_group.update()
        bullet_group.update()
        enemy_group.draw(screen)
        for enemy in enemy_group:
            enemy.trackingPlayer(p1)
        enemy_group.update()
        food_group.draw(screen)
        stam_group.draw(screen)

        crosshair_group.draw(screen)
        crosshair_group.update()

        

        pygame.display.update()
        

        # Set the FPS
        clock = pygame.time.Clock()

        # Update timer
        timer += 1
        
        
        clock.tick(60)

