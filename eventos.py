import pygame,time
from pygame.locals import *
import textos
pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte,20)


def Verifica(eventos, dia, posicao_player,isqueiro,fogo,faltaisqueiro):
	if eventos == K_q:
		if dia == 2:
			dia = 3

		if dia == 1:
			if posicao_player >= 400 and posicao_player <= 500 and isqueiro:
				dia = 2
				fogo = True
			if posicao_player >= 400 and posicao_player <= 500 and isqueiro == False:
				faltaisqueiro = True
				print(faltaisqueiro)
			print(posicao_player)

	if eventos == K_w:

		if dia == 2:
			dia = 3

		if dia == 1:
			dia =2

	if eventos == K_e:
		if dia == 2:
			dia = 3
	if eventos == K_r:
		if dia == 2:
			dia = 3 
	if eventos == K_f:
		if posicao_player >= 800 and posicao_player <= 840 and dia == 1:
			print("pegou isqueiro")
			isqueiro = True
			faltaisqueiro = False
			print(isqueiro)

	print(dia)
	return dia, isqueiro,fogo, faltaisqueiro
