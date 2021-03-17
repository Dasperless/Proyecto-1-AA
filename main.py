import random
cards = { 'Sospechosos': ['El/la mejor amigo(a)', 'El/la novio(a)', 'El/la vecino(a)', 'El mensajero', 'El extraño', 'El/la hermanastro(a)', 'El/la colega de trabajo'],
		  'Arma': ['Pistola', 'Cuchillo', 'Machete', 'Pala', 'Bate', 'Botella', 'Tubo','Cuerda'],
		  'Motivo': ['Venganza', 'Celos', 'Dinero', 'Accidente', 'Drogas', 'Robo'],
		  'Lugar': ['Sala', 'Comedor', 'Baño', 'Terraza', 'Cuarto', 'Garage', 'Patio', 'Balcón', 'Cocina']
		}

def randomIndex(size):
	return random.randint(0,size-1)

def setAnswer():
	answer = []
	for i in cards:
		size = len(cards[i])
		answer +=[cards[i][randomIndex(size)]]
	return answer
