Algoritmo ejercicio_2
	//area de documentacion
	//enunciado:leer velociad en kilometros por hora y convertirlas a metros sobre segundo para hallar la aceleracion
	//version:1.0
	//desarrollado por:Mateo Arias
	//fecha:23/02/23
	
	//area definicion de variables
	Definir v_inicial,v_final,tiempo,aceleracion Como Entero //variable de entrada que almacena la velocidad inicial, la velocidad final y la aceleracion
	//area de entrada
	Escribir 'v_final'
	Leer v_final
	Escribir 'v_inicial'
	Leer v_inicial
	Escribir 'tiempo'
	Leer tiempo
	//area de procesos
	aceleracion <- v_final-v_inicial
	aceleracion <- aceleracion/tiempo
	//area de salidas
	Escribir 'la aceleracion es : ',aceleracion
	
FinAlgoritmo
