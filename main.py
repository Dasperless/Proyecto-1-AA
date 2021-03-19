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
                
                
        
