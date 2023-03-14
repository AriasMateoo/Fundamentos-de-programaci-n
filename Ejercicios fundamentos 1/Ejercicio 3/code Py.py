# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de documentacion
	# enunciado:leer velociad en metros sobre segundos y tiempo en segundos para hallar la aceleracion y el tiempo
	# version:1.0
	# desarrollado por:Mateo Arias
	# fecha:23/02/23
	# area definicion de variables 
	v_inicial = int()
	tiempo = int()
	v_final = int()
	# area de entradas
	print("cual es la velocidad inicial")
	v_inicial = int(input())
	print("cual es la velocidad final")
	v_final = int(input())
	print("tiempo")
	tiempo = int(input())
	# area de procesos
	aceleracion = v_inicial+v_final/tiempo
	distancia = v_inicial*tiempo+0.5*aceleracion*tiempo**2
	# area de salidas
	print("la aceleracion es de:",aceleracion)
	print("la distancia es:",distancia)

