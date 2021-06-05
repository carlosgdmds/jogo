import jogo
import menu
class Main():
	def __init__(self):
		#carrega menu
		self.Rodando = True
		while self.Rodando:
			self.Rodando = menu.Start(self.Rodando)
		#carrega jogo
		if self.Rodando != True:
			jogo.Main()

if __name__ == "__main__":
	Main()

