import pygame
def Player(screen):
	player = pygame.image.load('imagens/player1.png')
	player.set_colorkey((0,0,0))
	player.convert_alpha(screen)
	posicao_player = [100,200]

	return player, posicao_player
def Amigo(screen):
	amigo = pygame.image.load('imagens/amigo.png')
	amigo.set_colorkey((0,0,0))
	amigo.convert_alpha(screen)
	return amigo

def Mochila(screen):
	mochila = pygame.image.load('imagens/mochila.png')
	mochila.set_colorkey((0,0,0))
	mochila.convert_alpha(screen)
	mochila = pygame.transform.scale(mochila,(150,150))
	return mochila

def Madeira(screen):
	madeira = pygame.image.load('imagens/madeira.png')
	madeira.set_colorkey((0,0,0))
	madeira.convert_alpha(screen)
	return madeira
