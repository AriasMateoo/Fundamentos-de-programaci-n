Algoritmo ecuacion_de_primergrado
	// descripcion:programa que lee una ecuacion lineal y la resuleve
	// version:1.0
	// desarrollado por:Mateo Arias
	// fecha:28/02/23
	
	// area de definicion de variables
	Definir a Como Real
	Definir b Como Real
	// area de entrada
	Escribir 'digite el valor de a'
	Leer a
	Escribir 'digite el valor de b'
	Leer b
	// area de Proceso 
	Si a<>0 Entonces
		x <- -1*b/a
		Escribir 'la solucion de la ecuacion es:',x
		Si b=0 Entonces
			// area de salidas
			Escribir 'la ecuacion no tiene solucion'
		FinSi
	SiNo
		Escribir 'solucion indeterminada'
	FinSi
FinAlgoritmo
