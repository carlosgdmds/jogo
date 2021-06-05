import pygame
from time import sleep

def Dia1para2(screen, player, bg, posicao_player, cutscene, dia, w,h, contadorCut):
	player = pygame.image.load('imagens/player1Centado.png')
	screen.blit(player,posicao_player)
	sleep(0.5)
	cutscene = True
	bg = pygame.image.load('imagens/fundopreto.png')
	contadorCut +=1
	if contadorCut >= 10:
		dia = 2.1
		cutscene = False
		bg = pygame.image.load('imagens/fundo.png')
		bg = pygame.transform.scale(bg,(w,h))
	return player, contadorCut, dia, cutscene,bg

def Dia2para3(screen, player, bg, posicao_player, cutscene, dia, w,h, contadorCut):
	player = pygame.image.load('imagens/player1Centado.png')
	screen.blit(player,posicao_player)
	sleep(0.5)
	cutscene = True
	bg = pygame.image.load('imagens/fundopreto.png')
	contadorCut +=1
	if contadorCut >= 10:
		dia = 3.1
		cutscene = False
		bg = pygame.image.load('imagens/fundo.png')
		bg = pygame.transform.scale(bg,(w,h))
	return player, contadorCut, dia, cutscene,bg
