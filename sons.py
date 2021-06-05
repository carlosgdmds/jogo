import pygame

def tocar():
	pygame.mixer.init()
	musica = pygame.mixer.music.load('musicas/musica1.mp3')
	pygame.mixer.music.set_volume(0.1)
	pygame.mixer.music.play(-1)
