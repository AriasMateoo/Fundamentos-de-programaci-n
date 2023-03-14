Algoritmo ejercicio_3
	// area de documentacion
	// enunciado:leer velociad en metros sobre segundos y tiempo en segundos para hallar la aceleracion y el tiempo
	// version:1.0
	// desarrollado por:Mateo Arias
	// fecha:23/02/23
	// area definicion de variables	
	Definir v_inicial,tiempo,v_final Como Entero
	// area de entradas
	Escribir 'cual es la velocidad inicial'
	Leer v_inicial
	Escribir 'cual es la velocidad final'
	Leer v_final
	Escribir 'tiempo'
	Leer tiempo
	// area de procesos
	aceleracion <- v_inicial+v_final/tiempo
	distancia <- v_inicial*tiempo+0.5*aceleracion*tiempo^2
	// area de salidas
	Escribir 'la aceleracion es de:',aceleracion
	Escribir 'la distancia es:',distancia
FinAlgoritmo
