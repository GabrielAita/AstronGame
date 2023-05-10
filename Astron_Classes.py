import pygame
from pygame.locals import *
from sys import exit
import math
import random

screenRes =(1152,648)
screen = pygame.display.set_mode(screenRes, 0 ,32)

idle = pygame.image.load('AstronGame-main\Anime\idle\img0.png').convert_alpha()
idle = pygame.transform.scale(idle, (50,50))

class Player(pygame.sprite.Sprite):

    #Construtor
    def __init__(self, name, damage,posX,posY):
        super().__init__()
        self.image = idle
        self.rect = self.image.get_rect()
        self.rect.center = [posX,posY]

        self.name = name
        self.hp = 5
        self.stamina = 100
        self.damage = damage
        self.positionX = posX
        self.positionY = posY
        self.alive = True
    
    #Metodos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 5
            self.positionX -= 5
        if keys[pygame.K_d] and self.rect.x < screenRes[0] - 50:
            self.rect.x += 5
            self.positionX += 5
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 5
            self.positionY -= 5
        if keys[pygame.K_s] and self.rect.y < screenRes[1] - 50:
            self.rect.y += 5 
            self.positionY += 5        

    def __str__(self):
        if self.alive:
            return "Ta vivo"
        else:
            return "Foi de comes e bebes"

    def dead(self):
        self.alive = False

    def hit(self,Enemy):
        self.hp =- Enemy.damage
        if self.hp <= 0:
            self.dead()
    
    def atack(self, Enemy):
        Enemy.hit(self)

class Enemy:

    #Construtor
    def __init__(self, hp, damage):
        self.size = 10
        self.hp = hp
        self.damage = damage
        self.alive = True
    
    #Metodos
    def dead(self):
        self.alive = False
        print("Inimigo morto")

    def hit(self, Player):
        self.hp -= Player.damage
        if self.hp <= 0:
            self.dead()
    
    def atack(self, Player):
        Player.hit(self)
    
    def draw(self):
        pygame.draw.circle(screen,(0,0,0),(random.randint(0,screenRes[0]),random.randint(0,screenRes[1])),10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, Player,speed):
        super().__init__()
        self.image = pygame.image.load("AstronGame-main\Sprites\Icon_Game\Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [Player.positionX,Player.positionY]

        self.size = 3
        self.speed = speed
        self.player = Player
        self.position = [Player.positionX,Player.positionY]

    def update(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def fired(self):
       NotImplemented
    
    def hitE(self, Enemy):
        Enemy.hp -= self.Player.damage

    def draw(self):
        pygame.draw.circle(screen,(0,0,0),self.position,10)

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AstronGame-main\Sprites\Icon_Game\crosshair.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
