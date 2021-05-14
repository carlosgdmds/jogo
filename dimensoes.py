import pygame
from pygame.locals import *
def Verificar():
	info = pygame.display.Info()
	w= info.current_w
	h= info.current_h
	screen = pygame.display.set_mode((w, h))
	return screen, w, h
