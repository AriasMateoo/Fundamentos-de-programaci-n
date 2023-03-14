Algoritmo ejercicio_1
	//area de documentacion
	//enunciado:leer velociad en metros sobre segundos y encontrar su aceleracion
	//version:1.0
	//desarrollado por:Mateo Arias
	//fecha:23/02/23
	
	//area definicion de variables
	Definir v_inicial,v_final,tiempo,aceleracion Como Entero //varaible de entrada que almacena la velocidad final, la velocidad inicial y la acaleracion
	//area de entradas
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
