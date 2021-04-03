import random
import time
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
	bfCombinations = []
	btCombinations = []
	bfTimeArr = []
	btTimeArr = []

	def __init__(self, numRest):
		self.setAnswer()
		self.setRestrictions(numRest)

		root = tk.Tk()
		self.app = Application(self, master=root)
		self.app.mainloop()

	def startTest(self, numRest, numRep):
		self.bfTimeArr = []
		self.btTimeArr = []

		for i in range(numRep):
			self.setAnswer()					#setea la respuesta
			answer = self.answer				#lista con la respuesta	
			self.setRestrictions(numRest)		#numero de restricciones
			restrictions = self.restrictions	#obtiene la restricciones
			self.app.showAnswer(answer)						#Actualiza las respuestas en la interfaz
			self.app.showRestrictions(restrictions)			#Actualiza las restricciones en la interfaz

			startTime = time.time()
			self.bruteForceSolution()
			finalTime = time.time() - startTime
			self.bfTimeArr += [finalTime]

		averge = self.average(self.bfTimeArr)
		self.app.setBfTime(averge)	
		self.createOutput()

	def average(self, arr):
		total = len(arr)
		sum = 0
		for i in arr:
			sum += i
		return sum/total

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
		self.bfCombinations = []

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
						self.app.updateBfAnswer(res)
						self.bfCombinations += [res]

						if(res == self.answer):
							return res

	def createOutput(self):
		outputStr = "############## Algoritmo de Fuerza bruta ##############\n"
		outputStr += "Cantidad de combinaciones: " + str(len(self.bfCombinations)) + "\n"
		# for i in self.bfCombinations:
		# 	outputStr += str(i) + "\n"
		
		outputStr += str(self.bfTimeArr)
		self.app.updateOutput(outputStr)

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