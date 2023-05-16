import pygame
from pygame.locals import *
from sys import exit
import math
import time
from Astron_Classes import *


pygame.init()

clock = pygame.time.Clock()

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

#Comida
food_group = pygame.sprite.Group()

#Stamina
stam_group = pygame.sprite.Group()

y = 130
for i in range(25):
    stam_group.add(Raio(p1, 30+y,30))
    y += 5
y = 130
for i in range(25):
    stam_group.add(Raio(p1, 30+y,50))
    y += 5

#Vida
hp_group = pygame.sprite.Group()

x = 0
for i in range(p1.hp):
    hp_group.add(Heart(p1, 30+x))
    x += 35

timer = 0
tempo_inicial = time.time()

score = 0

def game(MUSIC):

    global tempo_inicial
    global timer
    global score
    speed = (0,0)

    if MUSIC:
        pygame.mixer.music.load('AstronGame-main\musicas\Hopeful Feeling.mp3')
        pygame.mixer.music.play()

    pygame.mouse.set_visible(False)

    game_loop = True
    
    while game_loop:

        screen.blit(bg, (0,0))

        '''score_list = list(str(score))
        for i in range(len(score_list),0):
            score_i = pygame.image.load(f"AstronGame-main/Sprites/Numeros/N{i}.png")

        screen.blit(score_i,(1000,100))'''

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

        
        # Tracking imigo -> player

        # Inimigo
        if lvl.clear:
            if timer >= 60:
                if len(enemy_group) < 5:  
                    enemy_group.add(Enemy(random.randint(100,1000),random.randint(50,600),speed))

        # Colisão inimgo/bala
        for enemy in enemy_group:
            for bullet in bullet_group:
                if pygame.sprite.collide_rect(enemy,bullet):
                    enemy.hp -= 1
                    if enemy.hp <= 0:
                        enemy_group.remove(enemy)
                        bullet_group.remove(bullet)
                        score += 10
                        print(score)
                        if random.randint(1,3) == 1:
                            food_group.add(Food(enemy.rect.x,enemy.rect.y))
                        

        # Colisão imigo/player
        for enemy in enemy_group:
            for player in player_group:
                    if pygame.sprite.collide_rect(enemy,player):
                        enemy_group.remove(enemy)
                        player.hp -= 1
                        hp_group.remove(hp_group.sprites()[-1])

        # Colisão player/food
        for food in food_group:
            for player in player_group:
                if pygame.sprite.collide_rect(food,player):
                    food_group.remove(food)
                    player.stamina += 25
                    if player.stamina >= 50:
                        player.stamina = 50


        # timer segundos
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial

        if tempo_decorrido >= 1.0:
            p1.stamina -= 1
            print(p1.stamina)
            stam_group.remove(stam_group.sprites()[-1])
            tempo_inicial = time.time()

        
        if p1.stamina == 0:
            game_loop = False
        if p1.hp == 0:
            game_loop = False
        # Update the screen

        player_group.draw(screen)
        player_group.update()
        bullet_group.update()
        enemy_group.draw(screen)
        enemy_group.update()
        food_group.draw(screen)
        hp_group.draw(screen)
        stam_group.draw(screen)

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()
        

        # Set the FPS
        clock = pygame.time.Clock()

        # Update timer
        timer += 1
        
        
        clock.tick(60)

