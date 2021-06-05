import pygame, sys,os,time
from pygame.locals import *
import dimensoes, fundo, eventos, textos, sons, objetos, cutscene
from moviepy.editor import VideoFileClip, preview

class Main():
	def __init__(self):
		#definicao tela
		pygame.init()
		pygame.display.set_caption("O Mito da Caverna")
		self.screen,self.w, self.h = dimensoes.Verificar()
		clock = pygame.time.Clock()

		#carrega objeto
		self.player, self.posicao_player = objetos.Player(self.screen)
		self.amigo = objetos.Amigo(self.screen)
		self.mochila = objetos.Mochila(self.screen)
		self.madeira = objetos.Madeira(self.screen)
		#carrega fundo
		self.bg = pygame.image.load('imagens/fundo.png')
		self.w , self.h  = fundo.Verifica(self.w,self.h)
		self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
	
		#estado do movimento do player
		self.move_player_right = False
		self.move_player_left = False
		self.contador = 0
		self.contador2 = 0
		self.dia = 1
		#carrega trilha sonara
		sons.tocar()

		#Configuracoes de textos
		pygame.font.init()
		self.fonte = pygame.font.get_default_font()
		self.fontesys = pygame.font.SysFont(self.fonte,20)
		#objetos
		#fogueira
		self.isqueiro = False
		self.fogo = False
		self.faltaisqueiro = False
		#cutscene
		self.cutscene = False
		self.contadorCut = 0
		self.semfogueira = True
		self.contadorCut2 = 0
		#cereal
		self.cereal = False
		self.faltacereal = False
		#personagem varivel
		self.vida = 10
		self.fome = 10
		self.cede = 10
		self.frio = 10
		#dia2 
		self.acertos = 0
		#
		self.qualEscolha = 0
		self.contadorTeste = 0
		while True:
			#mostra na tela o fundo ,amigo e a mochila
			self.screen.fill((0,0,0))
			self.screen.blit(self.bg,(0,0))
			self.screen.blit(self.amigo,(600,100))
			self.screen.blit(self.mochila,(1000,350))
			self.screen.blit(self.madeira,(550,300))
			textos.Personagem(self.screen, self.vida, self.fome, self.cede, self.frio)

			#movimenta player
			if self.move_player_right:
				self.posicao_player[0] += 10
				self.contador +=1
			if self.move_player_left:
				self.posicao_player[0] -= 10
				self.contador2 +=1

			#verifica colisao com as paredes
			if self.posicao_player[0] >= self.w-300:
				self.posicao_player[0] = self.posicao_player[0]-50
			if self.posicao_player[0] <= -200:
				self.posicao_player[0] = self.posicao_player[0]+50

			#verifica dia e textos	
			if self.dia == 1:
				textos.diaUm(self.screen,self.fontesys)
			elif self.dia == 1.1:
				textos.diaUmEtapadois(self.screen, self.fontesys)

			if self.faltaisqueiro and self.dia == 1:
				textos.faltaIsqueiro(self.screen,self.fontesys)

			if self.faltacereal and self.dia == 1.1:
				textos.faltaCereal(self.screen,self.fontesys)

			if self.fogo:
				self.madeira = pygame.image.load('imagens/fogueira.png')
				self.madeira.set_colorkey((0,0,0))
				self.madeira.convert_alpha(self.screen)

			if self.fogo == False and self.dia == 2  and self.semfogueira:
				self.frio -= 3
				self.semfogueira = False
			
			if self.dia == 2:
				self.player,self.contadorCut,self.dia, self.cutscene ,self.bg= cutscene.Dia1para2(self.screen, self.player,self.bg,self.posicao_player, self.cutscene,self.dia, self.w,self.h, self.contadorCut)
				textos.Cutscene1(self.screen)
			if self.dia == 2.1:
				textos.DiaDois(self.screen,self.fontesys)
			
			if self.dia == 3:
				self.player, self.contadorCut2, self.dia, self.cutscene, self.bg = cutscene.Dia2para3(self.screen, self.player, self.bg, self.posicao_player,self.cutscene, self.dia,self.w,self.h,self.contadorCut2)
				textos.Cutscene2(self.screen)
				self.madeira = pygame.image.load('imagens/madeira.png')
				self.madeira.set_colorkey((0,0,0))
				self.madeira.convert_alpha(self.screen)

			if self.dia == 3.1:
				textos.DiaTres(self.screen,self.fontesys)

			if self.dia == 3.2:
				textos.DiaTresUm(self.screen,self.fontesys)

			if self.dia == 3.3:
				textos.DiaTresDois(self.screen,self.fontesys)

			if self.dia == 3.4:
				textos.DiaTresTres(self.screen, self.fontesys)

			if self.qualEscolha == 1.1:
				if self.fome < 5:
					textos.VamosMorrer(self.screen,self.fontesys)
				if self.fome >= 5:
					textos.VamosViver(self.screen, self.fontesys)
				self.dia = 3.5
				self.qualEscolha = 0
			if self.qualEscolha == 1.2:
				if self.fome < 5:
					textos.VamosMorrer(self.screen, self.fontesys)
				if self.fome >=5:
					textos.VamosViver(self.screen, self.fontesys)
				self.dia = 3.5
				self.qualEscolha = 0

			if self.qualEscolha == 2.1:
				textos.FilhoDaMae(self.screen, self.fontesys)
				self.dia = 3.5
				self.qualEscolha = 0
			if self.qualEscolha == 2.2:
				textos.FilhoDa(self.screen,self.fontesys)
				self.dia = 3.5
				self.qualEscolha = 0
			if self.qualEscolha == 3.1:
				textos.ComidaAcabando(self.screen, self.fontesys)
				self.dia = 3.5
				self.qualEscolha = 0
			if self.qualEscolha == 3.2:
				textos.ComidaTem(self.screen, self.fontesys)
				self.dia = 3.5
				self.qualEscolha = 0
			if self.dia == 3.5:
				textos.DiaTresCinco(self.screen, self.fontesys)

			if self.dia == 4 and self.vida >= 0 and self.vida <= 2:
				self.bg = pygame.image.load('imagens/fundopreto.png')
				self.bg = pygame.transform.scale(self.bg,(self.w,self.h))
				self.screen.blit(self.bg, (0,0))
				self.player = pygame.image.load('imagens/playermorto1.png')
				self.amigo = pygame.image.load('imagens/playermorto2.png')
				self.screen.blit(self.player,(300,100))
				self.screen.blit(self.amigo,(600,100))
				self.cutscene = True
				textos.PMorreu(self.screen)
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
			if self.dia == 4 and self.vida >= 3 and self.vida <6:
				self.bg = pygame.image.load('imagens/fundopreto.png')
				self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
				self.screen.blit(self.bg, (0,0))
				self.amigo = pygame.image.load('imagens/playermorto2.png')
				self.player = pygame.image.load('imagens/player1.png')
				self.screen.blit(self.amigo, (600,100))
				self.screen.blit(self.player, (300,100))
				self.cutscene = True
				textos.AmigoMorreu(self.screen)
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
				
			if self.dia == 4 and self.vida >= 6:
				self.bg = pygame.image.load('imagens/fundopreto.png')
				self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
				self.screen.blit(self.bg, (0,0))
				self.player = pygame.image.load('imagens/player1.png')
				self.amigo = pygame.image.load('imagens/amigo.png')
				self.screen.blit(self.player,(300,100))
				self.screen.blit(self.amigo, (600,100))
				self.cutscene = True
				textos.Sobrevivem(self.screen)
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
			#verifica eventos do teclado
			if self.cutscene == False:
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					if event.type == KEYDOWN:
						if event.key == K_d:
							self.move_player_right = True
							self.update()

						if event.key == K_a:
							self.move_player_left = True
							self.update2()
						#easter egg
						if event.key == K_h:
							if self.posicao_player[0] >= -120 and self.posicao_player[0] <=-50:
								clip = VideoFileClip('videos/video.mp4')
								clip.preview()
								self.screen,self.w,self.h = pygame.display.set_mode((1366,780)), 1366,780

						#eventos de interacao
						if self.dia == 1 or  self.dia == 1.1:
							self.dia, self.isqueiro, self.fogo, self.faltaisqueiro,self.fome,self.cereal,self.faltacereal,self.vida = eventos.DiaUm(event.key,self.dia, self.posicao_player[0],self.isqueiro,self.fogo,self.faltaisqueiro,self.fome,self.cereal, self.faltacereal,self.vida)
						if self.dia == 2.1:
							self.dia,self.acertos,self.fome, self.vida = eventos.DiaDois(event.key,self.dia, self.posicao_player[0],self.fome,self.vida)
						if self.dia == 3.2:
							self.dia, self.qualEscolha = eventos.DiaTresDois(event.key, self.qualEscolha,self.dia)
						if self.dia == 3.3:
							self.dia, self.qualEscolha = eventos.DiaTresTres(event.key, self.qualEscolha,self.dia)
						if self.dia == 3.4:
							self.dia, self.qualEscolha = eventos.DiaTresQuatro(event.key, self.qualEscolha, self.dia)
						if self.dia == 3.5:
							self.dia = eventos.DiaTresCinco(event.key, self.dia)
						if self.dia == 3.1:
							self.dia = eventos.DiaTres(event.key, self.dia)
					
						time.sleep(0.05)

					if event.type == KEYUP:
						if event.key == K_d:
							self.move_player_right = False
							self.player = pygame.image.load('imagens/player1.png')
							self.contador = 0
						if event.key == K_a:
							self.move_player_left = False
							self.player = pygame.image.load('imagens/player1left.png')
			
			if self.move_player_right:
				self.update()
			if self.move_player_left:
				self.update2()
			if self.move_player_right == False and self.move_player_left == False and self.cutscene == False:
				self.screen.blit(pygame.image.load('imagens/player1.png'),self.posicao_player)

			pygame.display.flip()
			clock.tick(60)

	def update2(self):
		if self.contador2 == 1:
			self.player = pygame.image.load('imagens/player2left.png')
		if self.contador2 == 2:
			self.player = pygame.image.load('imagens/player1left.png')
		if self.contador2 >= 3:
			self.contador2 = 0
		self.screen.blit(self.player,self.posicao_player)

	def update(self):
		if self.contador == 1:
			self.player = pygame.image.load('imagens/player2.png')
		if self.contador == 2:
			self.player = pygame.image.load('imagens/player1.png')
		if self.contador >=3:
			self.contador =0
		self.screen.blit(self.player,self.posicao_player)

