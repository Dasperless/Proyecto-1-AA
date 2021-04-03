import random
import tkinter as tk
from gui import Application

class Main:
	cards = {'Sospechosos': ['El/la mejor amigo(a)', 'El/la novio(a)', 'El/la vecino(a)', 'El mensajero', 'El extraño', 'El/la hermanastro(a)', 'El/la colega de trabajo'],
					'Arma': ['Pistola', 'Cuchillo', 'Machete', 'Pala', 'Bate', 'Botella', 'Tubo', 'Cuerda'],
					'Motivo': ['Venganza', 'Celos', 'Dinero', 'Accidente', 'Drogas', 'Robo'],
					'Lugar': ['Sala', 'Comedor', 'Baño', 'Terraza', 'Cuarto', 'Garage', 'Patio', 'Balcón', 'Cocina']
			}
	answer = []
	restrictions = []
	bfOutput = ""
	def __init__(self, numRest):
		self.setAnswer()
		self.setRestrictions(numRest)

		root = tk.Tk()
		self.app = Application(self, master=root)
		self.app.mainloop()

	def randomIndex(self, size):
		return random.randint(0, size-1)

	def setAnswer(self):
		answer = []
		for i in self.cards:
			size = len(self.cards[i])
			answer += [self.cards[i][self.randomIndex(size)]]
		self.answer = answer

	def bruteForceSolution(self):
		keys = list(self.cards.keys())
		self.bfOutput = "################ Algoritmo de fuerza bruta ################\n"
		for i in range(len(self.cards[keys[0]])):
			res = []
			for j in range(len(self.cards[keys[1]])):
				for k in range(len(self.cards[keys[2]])):
					for l in range(len(self.cards[keys[3]])):
						sospechoso = self.cards[keys[0]][i]
						arma = self.cards[keys[1]][j]
						motivo = self.cards[keys[2]][k]
						lugar = self.cards[keys[3]][l]
						res = [sospechoso, arma, motivo, lugar]
						self.app.bfArray[0]['text']  = sospechoso
						self.app.bfArray[1]['text']  = arma
						self.app.bfArray[2]['text']  = motivo
						self.app.bfArray[3]['text']  = lugar
						self.bfOutput += str(res) + "\n"
						if(res == self.answer):
							return res

	def setRestrictions(self,n):
			self.restrictions= []
			categorias = ['Sospechosos','Arma','Motivo','Lugar']
			
			#Contador que indica el numero de parejas de restricciones
			for contador1 in range(n):
					restriccion = []
					
					categoria1 = 100 #Categorias simplemente para validar
					categoria2 = 0
					i=0

					#Ciclo para obtener el numero de restricciones
					while(i<2):
							numRandom = random.randint(0,3)
							size = len(self.cards[categorias[numRandom]])
							cartaActual = self.cards[categorias[numRandom]][self.randomIndex(size)]
							
							if(categoria1 != 100):
									if(numRandom == categoria1):
											continue
									else:
											restriccion += [cartaActual]
											i+=1
											categoria2 = numRandom
							else:       
									categoria1 = numRandom
									restriccion += [cartaActual]
									i+=1
					prueba = [self.answer[categoria1],self.answer[categoria2]]
					if(restriccion != prueba):
							self.restrictions += [restriccion]
					else:
							n-=1    
		
main = Main(1)
print(main.bruteForceSolution())