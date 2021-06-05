import pygame
from pygame.locals import *

def Start():
	pygame.init()
	screen = pygame.display.set_mode((1366,768))
	#pygame.display.set_caption('teste')
	clock = pygame.time.Clock()
	morcego  = pygame.image.load('imagens/morcego.png')
	morcego1 = pygame.image.load('imagens/morcego.png')
	posicao_morcego =[1366,20]
	posicao_morcego2 = [1366, 400]
	acertos = 0
	morcegos = 0
	rodando = True
	while rodando:
		screen.fill((0,0,0))
		screen.blit(morcego, posicao_morcego)
		screen.blit(morcego1,posicao_morcego2)

		mouse_x, mouse_y = pygame.mouse.get_pos()
		if posicao_morcego[0] >= 0:
			posicao_morcego[0]  -=7
		if posicao_morcego[0] < 0:
			posicao_morcego[0] = 1366

		if posicao_morcego2[0] >=0:
			posicao_morcego2[0] -=6
		if posicao_morcego2[0] < 0:
			posicao_morcego2[0] = 1366

		if morcegos >=10:
			rodando = False

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if mouse_x >= posicao_morcego[0] + 20  and mouse_x <= posicao_morcego[0] + 250:
						if mouse_y>= posicao_morcego[1] +20 and mouse_y <= posicao_morcego[1]+220:
							acertos +=1
							morcegos +=1
							posicao_morcego[0] = 1366
					if mouse_x >= posicao_morcego2[0] +20 and mouse_x <= posicao_morcego2[0] + 250:
						if mouse_y >= posicao_morcego2[1] +20 and mouse_y <= posicao_morcego2[1]+220:
							acertos +=1
							morcegos +=1
							posicao_morcego2[0] =1366
		pygame.display.update()
		clock.tick(60)
	return acertos

if __name__=="__main__":
	Start()
