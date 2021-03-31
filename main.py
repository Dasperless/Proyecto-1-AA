import random
global cards
cards = { 'Sospechosos': ['El/la mejor amigo(a)', 'El/la novio(a)', 'El/la vecino(a)', 'El mensajero', 'El extraño', 'El/la hermanastro(a)', 'El/la colega de trabajo'],
		  'Arma': ['Pistola', 'Cuchillo', 'Machete', 'Pala', 'Bate', 'Botella', 'Tubo','Cuerda'],
		  'Motivo': ['Venganza', 'Celos', 'Dinero', 'Accidente', 'Drogas', 'Robo'],
		  'Lugar': ['Sala', 'Comedor', 'Baño', 'Terraza', 'Cuarto', 'Garage', 'Patio', 'Balcón', 'Cocina']
	}

def randomIndex(size):
	"""Retorna un índice aleatorio.

	Args:
	    size (int): tamaño del arreglo.

	Returns:
	    int: Un índice aleatoreo.
	"""	
	return random.randint(0,size-1)

def setAnswer(cardsList):
	"""Establece la respuesta del juego de cartas

	Returns:
	    list: Retorna una lista con la respuesta.
	"""	
	answer = []
	for i in cardsList:
		size = len(cardsList[i])
		answer +=[cardsList[i][randomIndex(size)]]
	return answer

def bruteForceSolution(cardsList, solution):
	keys = list(cardsList.keys())

	for i in range(len(cardsList[keys[0]])):						
		res =[]
		for j in range(len(cardsList[keys[1]])): 
			for k in range(len(cardsList[keys[2]])):
				for l in range(len(cardsList[keys[3]])):
					sospechoso = cardsList[keys[0]][i]
					arma = cardsList[keys[1]][j]
					motivo = cardsList[keys[2]][k]
					lugar =cardsList[keys[3]][l]
					res = [sospechoso,arma,motivo,lugar]
					# print(res)
					if(res == solution):
						return res
					
def setRestrictions(n):
	restricciones = []
	answer = setAnswer()
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
			size = len(cards[categorias[numRandom]])
			cartaActual = cards[categorias[numRandom]][randomIndex(size)]
			
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
		prueba = [answer[categoria1],answer[categoria2]]
		if(restriccion != prueba):
			restricciones += [restriccion]
		else:
			n-=1                                     
global answer
answer = setAnswer(cards)
