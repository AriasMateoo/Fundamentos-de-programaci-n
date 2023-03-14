Algoritmo problema_pag_118
	//declaracion de variables
	Definir duracion,costo Como Real
	//area de entradas
	Escribir 'CALCULO DE COSTO DE LLAMADA'
	Escribir 'Introduzca la duracion de la llamada en minutos:'
	Leer duracion
	//area de procesos
	Si duracion<=3 Entonces
		costo <- 0.10
	SiNo
		costo <- 0.10+((duracion-3)*0.05)
	FinSi
	//area de salidas
	Escribir 'El costo de la llamada es de: ',costo,' pesos.'
FinAlgoritmo
