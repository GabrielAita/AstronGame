import pygame
from pygame.locals import *
from sys import exit
import math
import random

screenRes =(1152,648)
screen = pygame.display.set_mode(screenRes, 0 ,32)

tam_char = 50

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
        self.atual = 0
        self.image = self.sprites_idle[self.atual]
        self.rect = self.image.get_rect()

        self.rect.center = [posX,posY]

        self.name = name
        self.hp = 3
        self.stamina = 50
        self.damage = damage
        self.positionX = posX
        self.positionY = posY
        self.alive = True
    
    #Metodos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 5
            self.positionX = self.rect.x
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_right_down):
                self.atual = 0
            self.image = self.sprites_walking_left[int(self.atual)]
        if keys[pygame.K_d] and self.rect.x < screenRes[0] - tam_char:
            self.rect.x += 5
            self.positionX = self.rect.x
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_right_down):
                self.atual = 0
            self.image = self.sprites_walking_right_down[int(self.atual)]
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 5
            self.positionY = self.rect.y
            self.atual = self.atual + 1/10
            if self.atual >= len(self.sprites_walking_up):
                self.atual = 0
            self.image = self.sprites_walking_up[int(self.atual)]
        if keys[pygame.K_s] and self.rect.y < screenRes[1] - tam_char:
            self.rect.y += 5 
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

class Enemy(pygame.sprite.Sprite):

    #Construtor
    def __init__(self, posX, posY,speed):
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
        self.atual = 0
        self.image = self.sprites_idle[self.atual]
        self.rect = self.image.get_rect()

        self.rect.center = [posX,posY]

        self.hp = 3
        self.damage = 1
        self.speed = speed
    
    #Metodos
    def update(self):
        speed = 2
        self.rect.x += speed * self.speed[0]
        self.rect.y += speed * self.speed[1]

    

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
        self.image = pygame.transform.scale(pygame.image.load("comida.png"),(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = [posX,posY]

class Heart(pygame.sprite.Sprite):
    def __init__(self,Player,posX):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('coracao.png').convert_alpha(), (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = [posX,30]
        self.player = Player

class Raio(pygame.sprite.Sprite):
    def __init__(self,Player,posX,posY):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('stamina.png').convert_alpha(), (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = [posX,posY]
        self.player = Player


    


