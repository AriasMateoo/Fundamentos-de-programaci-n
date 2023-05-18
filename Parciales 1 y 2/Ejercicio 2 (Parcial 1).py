if __name__ == '__main__':
	# programa: fundamentos de programacion//
	# nombre del archivo: segundo ejercicio del parcial//
	# descripcion: programa que calcula el tiempo expresado en segundos  FinAlgoritmo//
	# autor: juan sebastian rodriguez castano y Mateo Arias //
	# fecha: 3/13/23//
	# version: 1.0//
	# Pedir al usuario un numero entero de segundos
	print("Ingrese un numero entero de segundos:")
	segundoss = float(input())
	# Convertir segundos a dias, horas, minutos y segundos
	dias = segundoss/86400
	segundoss = segundoss%86400
	horas = segundoss/3600
	segundoss = segundoss%3600
	minutos = segundoss/60
	segundoss = segundoss%60
	# Imprimir el resultado
	print("El equivalente es:",dias,"dias",horas,"horas:",minutos,"minutos ",segundoss,"segundos")

