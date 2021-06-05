import pygame,time
#informacoes do personagem
def Personagem(screen, vida, fome, cede, frio):
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte,50)
	vida = "♥ "+str(vida)
	fome = str(fome)
	cede = str(cede)
	frio = "°C "+str(frio) 
	vidatela = fontesys.render(vida,1,(255,0,0))
	fometela = fontesys.render(fome,1,(255,255,0))
	cedetela = fontesys.render(cede,1,(0,0,255))
	friotela = fontesys.render(frio,1,(0,191,255))

	screen.blit(vidatela, (1200,40))
	screen.blit(fometela, (1200,80))
	screen.blit(cedetela, (1200,120))
	screen.blit(friotela, (1200,160))
#dia um
def diaUm(screen, fontesys):
	texto = "Fazer um Fogueira Clique Q"
	texto2 = "Nao fazer uma Fogueira Clique W"
	textotela = fontesys.render(texto,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	screen.blit(textotela,(50,10))
	screen.blit(textotela2,(50,40))

def diaUmEtapadois(screen, fontesys):

	texto = "Racionar comida 6 barras de cereal "
	texto1 = "0,5 barra por dia Clique Q"
	texto2 = "1 barras por dia Clique W"
	texto3 = "2 barras por dia Clique E"
	texto4 = "3 barras por dia Clique R"

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
	texto = "FALTA O ISQUEIRO "
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (500,40))

def faltaCereal(screen,fontesys):
	texto = "VOCÊ NAO PEGOU AS BARRAS DE CEREAIS"
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (500,40))
#dia 2
def DiaDois(screen, fontesys):
	texto = "A Morcegos por volta "
	texto1 = "Tentar caçar morcego Q"
	texto2 = "Passar para o dia seguinte W"
	textotela = fontesys.render(texto,1,(255,255,255))
	textotela1 = fontesys.render(texto1,1,(255,255,255))
	textotela2 = fontesys.render(texto2, 1, (255,255,255))
	
	screen.blit(textotela,  (50,10))
	screen.blit(textotela1, (50,40))
	screen.blit(textotela2, (50,70))
#dia 3
def DiaTres(screen, fontesys):
	texto = "converse com seu amigo"
	texto1 = "Falar sobre a morte    Q"
	texto2 = "Falar sobre um segredo W"
	texto3 = "Falar sobre a comida   E"

	textotela = fontesys.render(texto,1,(255,255,255))
	textotela1 = fontesys.render(texto1,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	textotela3 = fontesys.render(texto3,1,(255,255,255))
	
	screen.blit(textotela,(50,10))
	screen.blit(textotela1,(50,40))
	screen.blit(textotela2,(50,70))
	screen.blit(textotela3,(50,100))

def DiaTresUm(screen,fontesys):
	texto1 = "Eu acho que vamos morrer Q"
	texto2 = "Eu acho que vamor sobreviver W"
	textotela1 = fontesys.render(texto1,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	screen.blit(textotela1,(50,10))
	screen.blit(textotela2,(50,40))

def DiaTresDois(screen,fontesys):
	texto1 = "Eu fiquei com sua esposa Q"
	texto2 = "A sua filha nao é sua , eu sou o pai dela W"
	textotela1 = fontesys.render(texto1,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	screen.blit(textotela1,(50,10))
	screen.blit(textotela2,(50,40))

def DiaTresTres(screen,fontesys):
	texto1 = "A comida está acabando Q"
	texto2 = "Acho que tem comida suficiente para os proximos dias W"
	textotela1 = fontesys.render(texto1,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	screen.blit(textotela1,(50,10))
	screen.blit(textotela2,(50,40))

def VamosMorrer(screen, fontesys):
	texto = "Eu acho que vamos morrer"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela1,(1000,10))
def VamosViver(screen, fontesys):
	texto = "Eu acho que vamos viver"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela1,(1000,10))
def FilhoDaMae(screen, fontesys):
	texto ="Nao acredito que você fez isso seu filho da puta,"
	texto2 = "mas agora nao é hora de brigar"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	textotela2 = fontesys.render(texto2,1,(255,255,255))
	screen.blit(textotela1,(1000,10))
	screen.blit(textotela2,(1000,40))
def FilhoDa(screen, fontesys):
	texto = "Seu filho da puta eu vou te matar"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela1, (1000,10))

def ComidaAcabando(screen,fontesys):
	texto = "Sim eu acho que esta acabando"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela1,(1000,10))
def ComidaTem(screen,fontesys):
	texto = "Nao eu acho que  inda tem muita comida"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela1, (1000,10))
def DiaTresCinco(screen, fontesys):
	texto ="Seguir a proxima semana Q"
	textotela1 = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela1, (50,10))
#cutscenes textos
def Cutscene1(screen):
	texto = "Dia 2"
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte, 50)
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (600,40))

def Cutscene2(screen):
	texto = "Dia 3"
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys =pygame.font.SysFont(fonte,50)
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (600,40))
def PMorreu(screen):
	texto = "Voce e seu amigo morreram"
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte,50)
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (400,40))
def AmigoMorreu(screen):
	texto = "Seu amigo morreu"
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte,50)
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (400,40))
def Sobrevivem(screen):
	texto = "Você e seu amigo sobreviveram"
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte, 50)
	textotela = fontesys.render(texto,1,(255,255,255))
	screen.blit(textotela, (400,40))
