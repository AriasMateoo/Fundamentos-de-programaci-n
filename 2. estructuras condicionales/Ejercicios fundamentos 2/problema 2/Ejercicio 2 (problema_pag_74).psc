Algoritmo problema_pag_74
	// Declaración de variables
	Definir numero Como Real
	Definir suma Como Real
	Definir contador Como Entero
	// Inicialización de variables
	suma <- 0.0
	contador <- 0
	// Entrada de datos
	Escribir 'Ingrese una serie de números positivos. Ingrese 0 para terminar.'
	Leer numero
	// Procesamiento de datos
	Mientras numero<>0 Hacer
		Si numero>0 Entonces
			suma <- suma+numero
			contador <- contador+1
		FinSi
		Leer numero
	FinMientras
	// Cálculo de la media
	Si contador>0 Entonces
		media <- suma/contador
		Escribir 'La media de la serie de números positivos es: ',media
	SiNo
		Escribir 'No se ingresaron números positivos.'
	FinSi
FinAlgoritmo
