import pygame,time

def diaUm(screen, fontesys):
	texto = "Fazer um Fogueira Clique Q"
	texto2 = "Nao fazer uma Fogueira Clique W"
	textotela = fontesys.render(texto,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	screen.blit(textotela,(50,10))
	screen.blit(textotela2,(50,40))

def diaDois(screen, fontesys):
	texto = "Racionar comida"
	texto1 = "1 barra por dia Clique Q"
	texto2 = "2 barras por dia Clique W"
	texto3 = "3 barras por dia Clique E"
	texto4 = "4 barras por dia Clique R"

	textotela = fontesys.render(texto ,1, (255,255,255))
	textotela1 = fontesys.render(texto1, 1 ,(255,255,255))
	textotela2 = fontesys.render(texto2, 1, (255,255,255))
	textotela3 = fontesys.render(texto3, 1, (255,255,255))
	textotela4 = fontesys.render(texto4, 1, (255,255,255))
	
	screen.blit(textotela,(50,10))
	screen.blit(textotela1,(50,40))
	screen.blit(textotela2,(50,70))
	screen.blit(textotela3,(50,100))
	screen.blit(textotela4,(50,130))


def faltaIsqueiro(screen,fontesys):
	texto = "======== FALTA O ISQUEIRO ======"
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (500,40))
