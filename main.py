import random
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
	print(keys)

	
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
					print(res)
					if(res == solution):
						return res					

	"""Retorna una lista de restricciones.

        Args:
                n: Cantidad de restricciones
                sol: Solucion del juego

        Returns:
                list: Lista de restricciones
        """
def setRestrictions(n,sol):
        restricciones = []
        categorias = ['Sospechosos','Arma','Motivo','Lugar']
        contador1=0
        while(contador1<n):
                restriccion=[]
                contador2=0
                categoria1=0
                categoria2=0
                while(contador2<2):
                        numRandom = random.randint(0,3)
                        size = len(cards[categorias[numRandom]])
                        cartaActual = cards[categorias[numRandom]][randomIndex(size)]
                        if(contador2==0):
                                categoria1=numRandom
                                restriccion+=[cartaActual]
                                contador2+=1
                        else:
                                categoria2=numRandom
                                if(cartaActual!=restriccion[0]):    
                                        restriccion+=[cartaActual]
                                        contador2+=1
                prueba = [sol[categoria1],sol[categoria2]]
                if(restriccion!=prueba):
                        restricciones+=[restriccion]
                        contador1+=1
        return restricciones
