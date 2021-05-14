import pygame, sys,os,time
from pygame.locals import *
import dimensoes, fundo
import sons
import moviepy
from moviepy.editor import * 
import eventos
import textos

class Main():
	def __init__(self):
		#definicao tela
		pygame.init()
		pygame.display.set_caption("Tela principal")
		self.screen,self.w, self.h = dimensoes.Verificar()
		clock = pygame.time.Clock()

		#carrega player
		self.player = pygame.image.load('imagens/player1.png')
		self.player.set_colorkey((0,0,0))
		self.player.convert_alpha(self.screen)
		self.posicao_player = [100,200]

		#carrega amigo
		self.amigo = pygame.image.load('imagens/amigo.png')
		self.amigo.set_colorkey((0,0,0))
		self.amigo.convert_alpha(self.screen)
	
		#carrega fundo
		self.bg = pygame.image.load('imagens/fundo.png')
		self.w , self.h  = fundo.Verifica(self.w,self.h)
		self.bg = pygame.transform.scale(self.bg, (self.w, self.h))

		#carrega mochila
		self.mochila = pygame.image.load('imagens/mochila.png')
		self.mochila.set_colorkey((0,0,0))
		self.mochila.convert_alpha(self.screen)
		self.mochila = pygame.transform.scale(self.mochila,(150,150))
		
		#carrega madeira 
		self.madeira = pygame.image.load('imagens/madeira.png')
		self.madeira.set_colorkey((0,0,0))
		self.madeira.convert_alpha(self.screen)
	
		#estado do movimento do player
		self.move_player_right = False
		self.move_player_left = False
		self.contador = 0
		self.contador2 = 0
		sons.tocar()
		self.dia = 1

		#Configuracoes de textos
		pygame.font.init()
		self.fonte = pygame.font.get_default_font()
		self.fontesys = pygame.font.SysFont(self.fonte,20)
		#objetos
		self.isqueiro = False
		self.fogo = False
		self.faltaisqueiro = False

		while True:
			#mostra na tela o fundo ,amigo e a mochila
			self.screen.fill((0,0,0))
			self.screen.blit(self.bg,(0,0))
			self.screen.blit(self.amigo,(600,100))
			self.screen.blit(self.mochila,(1000,350))
			self.screen.blit(self.madeira,(550,300))

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
			elif self.dia == 2:
				textos.diaDois(self.screen, self.fontesys)
			if self.faltaisqueiro:
				textos.faltaIsqueiro(self.screen,self.fontesys)

			if self.fogo:
				self.madeira = pygame.image.load('imagens/fogueira.png')
				self.madeira.set_colorkey((0,0,0))
				self.madeira.convert_alpha(self.screen)

			if self.fogo:
				self.bg = pygame.image.load('imagens/fundopreto.png')
				self.bg = pygame.transform.scale(self.bg,(self.w,self.h))
				#self.player.set_colorkey((255,255,255))

			#verifica eventos do teclado
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
					self.dia, self.isqueiro, self.fogo, self.faltaisqueiro = eventos.Verifica(event.key,self.dia, self.posicao_player[0],self.isqueiro,self.fogo,self.faltaisqueiro)

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
			elif self.move_player_left:
				self.update2()
			else:
				self.screen.blit(pygame.image.load('imagens/player1.png'),self.posicao_player)

			pygame.display.update()
			clock.tick(60)

	def update2(self):
		if self.contador2 == 0:
			self.player = pygame.image.load('imagens/player1left.png')
		if self.contador2 == 1:
			self.player = pygame.image.load('imagens/player2left.png')
		if self.contador2 == 2:
			self.player = pygame.image.load('imagens/player1left.png')
		if self.contador2 >=3:
			self.contador2 = 0
		#time.sleep(0.02)
		self.screen.blit(self.player,self.posicao_player)

	def update(self):
		#animacao player
		if self.contador == 0:
			self.player = pygame.image.load('imagens/player1.png')
		if self.contador == 1:
			self.player = pygame.image.load('imagens/player2.png')
		if self.contador == 2:
			self.player = pygame.image.load('imagens/player1.png')
		if self.contador >=3:
			self.contador =0
		#time.sleep(0.02)
		self.screen.blit(self.player,self.posicao_player)
		
