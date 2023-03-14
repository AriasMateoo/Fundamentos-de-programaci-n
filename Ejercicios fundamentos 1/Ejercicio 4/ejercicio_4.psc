Algoritmo ejercicio_4
	//area de documentacion
	//enunciado:leer velociad en metros sobre segundo y hallar el tiempo
	//version:1.0
	//desarrollado por:Mateo Arias
	//fecha:23/02/23
	
	//declaracion de variables
	Definir v_final,v_inicial,aceleracion Como Entero//variable de entrada que almacena la velocidad inicial, la velocidad final y la aceleracion
	//area de entradas
	Escribir 'v_final en m/s'
	Leer v_final
	Escribir 'v_inicial'
	Leer v_inicial
	Escribir 'aceleracion'
	Leer aceleracion
	//area de procesos
	tiempo <- v_final-v_inicial
	tiempo <- tiempo/aceleracion
	//area de salidas
	Escribir 'el tiempo es : ',tiempo
FinAlgoritmo
