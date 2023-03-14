Algoritmo ejercicio_6
	// area de documentacion
	// enunciado:leer velociad en metros sobre segundos y tiempo en segundos para hallar la aceleracion y el tiempo
	// version:1.0
	// desarrollado por:Mateo Arias
	// fecha:23/02/23
	// area definicion de variables	
	// Definicion de variables
	Definir Nombre Como Caracter
	Definir Numero_Horas,Valor_Hora,Salario_Base,Salario_Final Como Entero
	Definir Salario_Tasas Como Real
	// Declaracion de variables
	Nombre <- i
	Numero_Horas <- h
	Valor_Hora <- n
	Tasas <- 0.25
	// Entradas y Procesos
	Escribir 'Digite Nombre de Usuario: '
	Leer Nombre
	Escribir 'cual fue el numero de horas trabajadas: '
	Leer Numero_Horas
	Escribir 'cual es el valor de las horas trabajadas: '
	Leer Valor_Hora
	Salario_Base <- (Valor_Hora*Numero_Horas)
	Escribir 'El Salario Base es de: ',Salario_Base
	Salario_Tasas <- (Salario_Base*Tasas)
	Escribir 'El salario con la aplicacion de Tasas de Interes es de: ',Salario_Tasas
	Salario_Final <- (Salario_Base-Salario_Tasas)
	// Salidas
	Escribir Nombre,' Su Salario Final fue de: ',Salario_Final
FinAlgoritmo
