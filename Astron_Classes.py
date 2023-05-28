import pygame
from pygame.locals import *
from sys import exit
import math
from random import uniform,random
vec = pygame.math.Vector2

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screenRes = (screen.get_width(),screen.get_height())

tam_char = 70









class Player(pygame.sprite.Sprite):

    #Construtor
    def __init__(self, name, damage,posX,posY):
        super().__init__()
        self.sprites_idle = []
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\idle\img0.png'),(tam_char,tam_char)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\idle\img1.png'),(tam_char,tam_char)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\idle\img2.png'),(tam_char,tam_char)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\idle\img3.png'),(tam_char,tam_char)))
        self.sprites_walking_right_down = []
        self.sprites_walking_right_down.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img0.png'),(tam_char,tam_char)))
        self.sprites_walking_right_down.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img1.png'),(tam_char,tam_char)))
        self.sprites_walking_right_down.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img2.png'),(tam_char,tam_char)))
        self.sprites_walking_right_down.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img3.png'),(tam_char,tam_char)))
        self.sprites_walking_left = []
        self.sprites_walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img0.png'),(tam_char,tam_char)),True,False))
        self.sprites_walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img1.png'),(tam_char,tam_char)),True,False))
        self.sprites_walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img2.png'),(tam_char,tam_char)),True,False))
        self.sprites_walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_frente\img3.png'),(tam_char,tam_char)),True,False))
        self.sprites_walking_up = []
        self.sprites_walking_up.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_costa\img0.png'),(tam_char,tam_char)))
        self.sprites_walking_up.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_costa\img1.png'),(tam_char,tam_char)))
        self.sprites_walking_up.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_costa\img2.png'),(tam_char,tam_char)))
        self.sprites_walking_up.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Andando_costa\img3.png'),(tam_char,tam_char)))
        self.sprites_damage = []
        self.sprites_damage.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Dano\img0.png'),(tam_char,tam_char)))
        self.sprites_damage.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Dano\img1.png'),(tam_char,tam_char)))
        self.sprites_damage.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Dano\img2.png'),(tam_char,tam_char)))
        self.sprites_damage.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\Dano\img3.png'),(tam_char,tam_char)))
        self.atual = 0
        self.image = self.sprites_idle[self.atual]
        self.rect = self.image.get_rect()

        self.rect.center = [posX,posY]

        self.name = name
        self.hp = 3
        self.stamina = 25
        self.damage = damage
        self.positionX = posX
        self.positionY = posY
        self.alive = True
    
    #Metodos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 7
            self.positionX = self.rect.x
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_right_down):
                self.atual = 0
            self.image = self.sprites_walking_left[int(self.atual)]
        if keys[pygame.K_d] and self.rect.x < screenRes[0] - tam_char:
            self.rect.x += 7
            self.positionX = self.rect.x
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_right_down):
                self.atual = 0
            self.image = self.sprites_walking_right_down[int(self.atual)]
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 7
            self.positionY = self.rect.y
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_up):
                self.atual = 0
            self.image = self.sprites_walking_up[int(self.atual)]
        if keys[pygame.K_s] and self.rect.y < screenRes[1] - tam_char:
            self.rect.y += 7 
            self.positionY = self.rect.y
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_right_down):
                self.atual = 0
            self.image = self.sprites_walking_right_down[int(self.atual)]
        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_idle):
                self.atual = 0
            self.image = self.sprites_idle[int(self.atual)]
    def takingDamage(self):
        self.atual = self.atual + 1/10
        if self.atual >= len(self.sprites_damage):
            self.atual = 0
        self.image = self.sprites_damage[int(self.atual)]

    def imunityFrame(self,currentHP):
        self.hp == currentHP

class Enemy(pygame.sprite.Sprite):

    #Construtor
    def __init__(self, posX, posY,target):
        super().__init__()
        self.sprites_idle = []
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\inimigo\img0.png'),(tam_char,tam_char)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\inimigo\img1.png'),(tam_char,tam_char)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\inimigo\img2.png'),(tam_char,tam_char)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('AstronGame-main\Anime\inimigo\img3.png'),(tam_char,tam_char)))
        self.atual = 0
        self.image = self.sprites_idle[self.atual]
        self.rect = self.image.get_rect()

        self.spawn_pos = [posX,posY]

        self.rect.center = [posX,posY]

        self.target = [target.positionX,target.positionY]
        self.hp = 1
        self.damage = 1

        self.MOB_SIZE = 32
        self.MAX_SPEED = 8
        self.MAX_FORCE = 0.1
        self.APPROACH_RADIUS = 120
        self.pos = vec(posX,posY)
        self.vel = vec(self.MAX_SPEED, 0).rotate(uniform(0, 360))
    
    #Metodos

    def seek_with_approach(self, target):
        self.desired = (target - self.pos)
        dist = self.desired.length()
        self.desired.normalize_ip()
        if dist < self.APPROACH_RADIUS:
            self.desired *= dist / self.APPROACH_RADIUS * self.MAX_SPEED
        else:
            self.desired *= self.MAX_SPEED
        steer = (self.desired - self.vel)
        if steer.length() > self.MAX_FORCE:
            steer.scale_to_length(self.MAX_FORCE)
        return steer
    
    def update(self):
        self.acc = self.seek_with_approach((self.target[0],self.target[1]))
        self.vel += self.acc
        if self.vel.length() > self.MAX_SPEED:
            self.vel.scale_to_length(self.MAX_SPEED)
        self.pos += self.vel
        self.rect.center = self.pos

        self.atual = self.atual + 1/10
        if self.atual >= len(self.sprites_idle):
            self.atual = 0
        self.image = self.sprites_idle[int(self.atual)]

    def trackingPlayer(self,player):
        self.target = [player.positionX,player.positionY]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, Player,speed):
        super().__init__()
        self.image = pygame.image.load("AstronGame-main\Sprites\Icon_Game\Bullet.png")
        self.rect = self.image.get_rect()
        self.position = [Player.rect.x + 25,Player.rect.y + 25]
        self.rect.center = self.position

        self.lifespam = 51
        self.size = 3
        self.speed = speed
        self.player = Player

    def update(self):
        self.position[0] += self.speed[0] * 8
        self.position[1] += self.speed[1] * 8
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.lifespam -= 1
        self.image.set_alpha(self.lifespam*5) 

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AstronGame-main\Sprites\Icon_Game\crosshair.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Level:
    def __init__(self):
        self.clear = True

class Food(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("AstronGame-main\Sprites\Icon_Game\comida.png"),(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = [posX,posY]
        self.timetolive = 5

class Heart(pygame.sprite.Sprite):
    def __init__(self,Player,posX):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Icon_Game\coracao.png').convert_alpha(), (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = [posX,30]
        self.player = Player

class Raio(pygame.sprite.Sprite):
    def __init__(self,Player,posX,posY):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Icon_Game\stamina.png').convert_alpha(), (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = [posX,posY]
        self.player = Player


    


