Algoritmo problema_pag_74
	// Declaraci�n de variables
	Definir numero Como Real
	Definir suma Como Real
	Definir contador Como Entero
	// Inicializaci�n de variables
	suma <- 0.0
	contador <- 0
	// Entrada de datos
	Escribir 'Ingrese una serie de n�meros positivos. Ingrese 0 para terminar.'
	Leer numero
	// Procesamiento de datos
	Mientras numero<>0 Hacer
		Si numero>0 Entonces
			suma <- suma+numero
			contador <- contador+1
		FinSi
		Leer numero
	FinMientras
	// C�lculo de la media
	Si contador>0 Entonces
		media <- suma/contador
		Escribir 'La media de la serie de n�meros positivos es: ',media
	SiNo
		Escribir 'No se ingresaron n�meros positivos.'
	FinSi
FinAlgoritmo
