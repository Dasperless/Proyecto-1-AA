import random
import time
import tkinter as tk
from tkinter.constants import NONE
from gui import Application

class Main:
	cards = {'Sospechosos': ['El/la mejor amigo(a)', 'El/la novio(a)', 'El/la vecino(a)', 'El mensajero', 'El extraño', 'El/la hermanastro(a)', 'El/la colega de trabajo'],
					'Arma': ['Pistola', 'Cuchillo', 'Machete', 'Pala', 'Bate', 'Botella', 'Tubo', 'Cuerda'],
					'Motivo': ['Venganza', 'Celos', 'Dinero', 'Accidente', 'Drogas', 'Robo'],
					'Parte': ['Cabeza','Pecho', 'Abdomen', 'Espalda', 'Piernas', 'Brazos'],
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
			self.app.updateAnswer(answer)						#Actualiza las respuestas en la interfaz
			self.app.updateRestrictions(restrictions)			#Actualiza las restricciones en la interfaz

			#Se toma el tiempo del algoritmo de fuerza bruta.
			startTimeBf = time.time_ns()
			bruteForce = self.bruteForceSolution()
			finalTimeBf = time.time_ns() - startTimeBf
			self.bfTimeArr += [finalTimeBf]

			#Se toma el tiempo del algoritmo de backtracking.
			startTimeBt = time.time_ns()
			backtracking = self.backtrackingSolution(['','','','',''],0)
			finalTimeBt = time.time_ns() - startTimeBt
			self.btTimeArr += [finalTimeBt]

		#promedios
		bfaverge = self.average(self.bfTimeArr)
		btaverage = self.average(self.btTimeArr)

		#actualiza el label de la respuesta.
		self.app.updateBfAnswer(bruteForce)
		self.app.updateBtAnswer(backtracking)

		#actualiza los promedios en interfaz 
		self.app.setBfTime(bfaverge)
		self.app.setBtTime(btaverage)	

		self.createOutput() #Crea el output.

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

		for i in range(len(self.cards[keys[0]])):
			res = []
			for j in range(len(self.cards[keys[1]])):
				for k in range(len(self.cards[keys[2]])):
					for l in range(len(self.cards[keys[3]])):
						for m in range(len(self.cards[keys[4]])):
							sospechoso = self.cards[keys[0]][i]
							arma = self.cards[keys[1]][j]
							motivo = self.cards[keys[2]][k]
							parte = self.cards[keys[3]][l]
							lugar = self.cards[keys[4]][m]
							res = [sospechoso, arma, motivo, parte, lugar]	
							if(res == self.answer):
								return res

	def createOutput(self):
		outputStr = "############## Algoritmo de Fuerza bruta ##############\n"
		outputStr += str(self.bfTimeArr) + "\n"
		outputStr += "Promedio: " + str(self.average(self.bfTimeArr)) +"\n\n"

		outputStr += "############## Algoritmo de backtracking ##############\n"
		outputStr += str(self.btTimeArr) + "\n" +  str(self.average(self.btTimeArr)) + "\n"
		outputStr += "Promedio: " + str(self.average(self.btTimeArr)) +"\n\n"
		self.app.updateOutput(outputStr) 

	def setRestrictions(self,n):
			self.restrictions= []
			categorias = ['Sospechosos','Arma','Motivo','Parte','Lugar']
			
			#Contador que indica el numero de parejas de restricciones
			for contador1 in range(n):
					restriccion = []
					
					categoria1 = 100 #Categorias simplemente para validar
					categoria2 = 0
					i=0

					#Ciclo para obtener el numero de restricciones
					while(i<2):
							numRandom = random.randint(0,4)
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
	"""
	Comprueba en el array actual si existe alguna restriccion
	Input: Array con Restricciones
	Return: False: Si existe la restriccion
				True: Si no existe la restriccion
	"""					   						 
	def comprobarRes(self,array):
		for restriccion in self.restrictions:
			if(restriccion[0] in array and restriccion[1] in array and '' not in array):
				return False
		return True
		
	"""
	Busca la solucion al problema de cartas de manera recursiva y acorta camino con restricciones
	Input: Array en el cual se añade la solucion
	Return: Array con la solucion
	"""
	def backtrackingSolution(self,array,n):
		if(n == 5):						
			if(array == self.answer):
				return array
		else:
			keys = list(self.cards.keys())
			for c in range(len(self.cards[keys[n]])):				#Recorre las cartas
				array[n]=self.cards[keys[n]][c]						#Selecciona en la posicion n la carta.
				if(self.comprobarRes(array)):
					result = self.backtrackingSolution(array,n+1)
					if(result is not None):
						return result

main = Main(1)