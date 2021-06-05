from pygame.locals import *
import morcego
#dia um

def DiaUm(eventos, dia, posicao_player,isqueiro,fogo,faltaisqueiro,fome, cereal, faltacereal,vida):
	if eventos == K_q:
		if dia == 1.1 and cereal:
			fome -= 3
			vida -=3
			dia = 2
		if cereal == False:
			faltacereal = True
		if dia == 1:
			if posicao_player >= 400 and posicao_player <= 500 and isqueiro:
				dia = 1.1
				fogo = True
			if posicao_player >= 400 and posicao_player <= 500 and isqueiro == False:
				faltaisqueiro = True
				#print(faltaisqueiro)
 
	if eventos == K_w:
		if dia == 1.1 and cereal:
			fome -= 2
			vida -=2
			dia = 2
		if cereal == False:
			faltacereal = True

		if dia == 1:
			vida -= 3
			dia = 1.1

	if eventos == K_e:
		if dia == 1.1 and cereal:
			vida -= 4
			fome -= 4
			dia = 2
		if cereal == False:
			faltacereaal = True

	if eventos == K_r:
		if dia == 1.1 and cereal:
			dia = 2
			fome -= 1
			vida -= 1
		if cereal == False:
			faltacereal = True

	if eventos == K_f and dia == 1:
		if posicao_player >= 800 and posicao_player <= 840:
			isqueiro = True
			faltaisqueiro = False

	if eventos == K_f and dia == 1.1 and posicao_player >= 800 and posicao_player <= 840:
			#print("pegou as barras de cereal")
			cereal = True
			faltacereal = False
	#print(dia)
	return dia, isqueiro, fogo, faltaisqueiro, fome,cereal, faltacereal,vida
#dia dois
def DiaDois(eventos, dia, posicao_player,fome, vida):
	#print(posicao_player)
	acertos = 0
	if eventos == K_q:
		if posicao_player >= 800 :
			#print("Caçar morcego")
			acertos = morcego.Start()
			dia = 3
			fome +=2
			vida +=1
	if eventos == K_w:
		#print("Fazer nada")
		dia = 3
		fome -=2
		vida -=2

	return dia, acertos, fome,vida
def DiaTres(eventos, dia):
	if eventos == K_q:
		dia = 3.2
	if eventos == K_w:
		dia = 3.3
	if eventos == K_e:
		dia = 3.4
	return dia

def DiaTresDois(eventos,escolha,dia):
	if eventos == K_q:
		escolha = 1.1
	if eventos == K_w:
		escolha = 1.2
	return dia, escolha

def DiaTresTres(eventos, escolha,dia):
	if eventos == K_q:
		escolha = 2.1
	if eventos == K_w:
		escolha = 2.2
	return dia,escolha

def DiaTresQuatro(eventos, escolha,dia):
	if eventos == K_q:
		escolha = 3.1
	if eventos == K_w:
		escolha = 3.2
	return dia,escolha
def DiaTresCinco(eventos,dia):
	if eventos == K_q:
		dia = 4

	return dia
