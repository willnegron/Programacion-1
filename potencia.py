import math
	
class Potenciacion:
		
	def Potencia():
		base = input('Introduce un numero entero para la Base: ')
		exponente = input('Introduce un numero entero para el Exponente: ')
		potencia = pow(base,exponente)
		print "La potencia de ",base, " elevado a ",exponente, " es: ",potencia
		
	Potencia()
