import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN


def Start(Rodando):
	pygame.init()
	pygame.display.set_caption("Mito da caverna")
	info = pygame.display.Info()
	screen = pygame.display.set_mode((info.current_w,info.current_h))
	clock = pygame.time.Clock()
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte,50)
	texto = "INICIAR"
	textotela = fontesys.render(texto,1,(255,255,255))

	while True:
		screen.fill((0,0,0))
		screen.blit(textotela,(600,100))
		mouse_x,mouse_y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if mouse_x >= 600 and mouse_x <=800 and mouse_y >= 100 and mouse_y <= 150:
						Rodando = False
		if Rodando == False:
			break
		pygame.display.flip()
		clock.tick(60)
	return Rodando
