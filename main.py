import pygame,sys
from pygame.locals import *
import jogo

class Main():
	def __init__(self):
		self.Rodando = True
		while self.Rodando:
			#carrega menu
			self.Menu()
		if self.Rodando != True:
			jogo.Main()

	def Menu(self):
		pygame.init()
		pygame.display.set_caption("Mito da caverna")
		self.info = pygame.display.Info()
	
		self.screen = pygame.display.set_mode((self.info.current_w,self.info.current_h))
		clock = pygame.time.Clock()

		while True:
			self.screen.fill((0,0,0))
			mouse_x,mouse_y = pygame.mouse.get_pos()
			botao_comecar = pygame.Rect(100,100,200,50)
			pygame.draw.rect(self.screen, (255,255,255,), botao_comecar)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						if mouse_x >= 100 and mouse_x <=300 and mouse_y >= 100 and mouse_y <= 150:
							self.Rodando = False
			if self.Rodando == False:
				break
			pygame.display.flip()
			clock.tick(60)

		return self.Rodando

if __name__ == "__main__":
	Main()

