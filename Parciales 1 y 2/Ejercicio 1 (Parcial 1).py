if __name__ == '__main__':
	# descripcion: programa que calcula la aceleracion, la velocidad final, la velocidad inicial, la distancia, el tiempo, la velocidad media y la velocidad instantanea
	# desarrollado por: Juan Sebastian rodriguez y Mateo Arias
	# version: 1.0
	# fecha: 13/03/23
	# area de entradas
	# variable que almacena el menu del programa
	print("Menu de opciones")
	# variable que almacena la opcion 1, sus procesos y resultados 
	print("1. Opcion 1 aceleracion")
	# variable que almacena la opcion 2, sus procesos y resultados
	print("2. Opcion 2 velocidad final")
	# variable que almacena la opcion 3, sus procesos y resultados
	print("3. Opcion 3 velocidad inicial")
	# variable que almacena la opcion 4, sus procesos y resultados
	print("4. opcion 4 tiempo")
	# variable que almacena la opcion 5, sus procesos y resultados
	print("5. opcion 5 distancia")
	# variable que almacena la opcion 6, sus procesos y resultados
	print("6. opcion 6 velocidad media")
	# variable que almacena la opcion 7, sus procesos y resultados
	print("7. opcion 7 velocidad instantanea")
	# area de procesos y salidas
	print("Seleccione una opcion:")
	opcionm = input()
	if opcionm==1:
		v_i = float()
		v_f = float()
		t = float()
		a = float()
		print("Ingrese la velocidad inicial: ")
		v_i = float(input())
		print("Ingrese la velocidad final: ")
		v_f = float(input())
		print("Ingrese el tiempo transcurrido: ")
		t = float(input())
		a = (v_f-v_i)/t
		print("La aceleracion es: ",a)
	if opcionm==2:
		vi = float()
		a = float()
		t = float()
		vf = float()
		print("Introduce la velocidad inicial:")
		vi = float(input())
		print("Introduce la aceleracion:")
		a = float(input())
		print("Introduce el tiempo transcurrido:")
		t = float(input())
		vf = vi+a*t
		print("La velocidad final es:",vf)
	if opcionm==3:
		v_f = float()
		a = float()
		t = float()
		v_i = float()
		print("Introduce la velocidad final:")
		v_f = float(input())
		print("Introduce la aceleracion:")
		a = float(input())
		print("Introduce el tiempo transcurrido:")
		t = float(input())
		v_i = (v_f-a*t)
		print("La velocidad inicial es: ",v_i)
	if opcionm==4:
		print("Ingrese la distancia recorrida en metros:")
		distancia = float(input())
		print("Ingrese la velocidad en metros por segundo:")
		velocidad = float(input())
		tiempo = distancia/velocidad
		print("El tiempo del MRU es de:",tiempo,"segundos")
	if opcionm==5:
		print("Ingrese la velocidad:")
		velocidad = float(input())
		print("Ingrese el tiempo:")
		tiempo = float(input())
		distancia = velocidad*tiempo
		print("La distancia recorrida es:",distancia)
	if opcionm==6:
		distancia = float()
		tiempo = float()
		velocidad = float()
		# Solicitar al usuario la distancia y el tiempo
		print("Ingrese la distancia total recorrida: ")
		distancia = float(input())
		print("Ingrese el tiempo total empleado: ")
		tiempo = float(input())
		# Calcular la velocidad media
		velocidad = distancia/tiempo
		# Mostrar el resultado al usuario
		print("La velocidad media es: ",velocidad," km/h")
	if opcionm==7:
		print("Ingrese la posicion inicial:")
		posicioninicial = float(input())
		print("Ingrese la posicion final:")
		posicionfinal = float(input())
		print("Ingrese el tiempo inicial:")
		tiempoinicial = float(input())
		print("Ingrese el tiempo final:")
		tiempofinal = float(input())
		cambioposicion = posicionfinal-posicioninicial
		cambiotiempo = tiempofinal-tiempoinicial
		velocidad = cambioposicion/cambiotiempo
		print("La velocidad instantanea es:",velocidad)

