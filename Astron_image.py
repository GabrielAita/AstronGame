import pygame
from Astron_game_over import screen

pygame.init()

screenRes = (screen.get_width(),screen.get_height())

tamLetra = (96,96)
tamSeta = (64,64)

# Alfabeto
seta_cima = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Icon_GameOver\Seta.png').convert_alpha(),tamSeta)
seta_baixo = pygame.transform.flip(seta_cima,False,True)

A = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LA.png').convert_alpha(),tamLetra)
B = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LB.png').convert_alpha(),tamLetra)
C = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LC.png').convert_alpha(),tamLetra)
D = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LD.png').convert_alpha(),tamLetra)
E = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LE.png').convert_alpha(),tamLetra)
F = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LF.png').convert_alpha(),tamLetra)
G = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LG.png').convert_alpha(),tamLetra)
H = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LH.png').convert_alpha(),tamLetra)
I = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LI.png').convert_alpha(),tamLetra)
J = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LJ.png').convert_alpha(),tamLetra)
K = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LK.png').convert_alpha(),tamLetra)
L = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LL.png').convert_alpha(),tamLetra)
M = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LM.png').convert_alpha(),tamLetra)
N = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LN.png').convert_alpha(),tamLetra)
O = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LO.png').convert_alpha(),tamLetra)
P = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LP.png').convert_alpha(),tamLetra)
Q = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LQ.png').convert_alpha(),tamLetra)
R = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LR.png').convert_alpha(),tamLetra)
S = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LS.png').convert_alpha(),tamLetra)
T = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LT.png').convert_alpha(),tamLetra)
U = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LU.png').convert_alpha(),tamLetra)
V = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LV.png').convert_alpha(),tamLetra)
W = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LW.png').convert_alpha(),tamLetra)
X = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LX.png').convert_alpha(),tamLetra)
Y = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LY.png').convert_alpha(),tamLetra)
Z = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Letras\LZ.png').convert_alpha(),tamLetra)

alfabeto = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

BG_GO = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Icon_GameOver\BG_GAME_OVER.png').convert_alpha(),(screenRes[0]/2,screenRes[1]))

CONTINUAR = pygame.transform.scale(pygame.image.load('AstronGame-main\Sprites\Icon_GameOver\CONTINUAR.png').convert_alpha(),(256,128))





