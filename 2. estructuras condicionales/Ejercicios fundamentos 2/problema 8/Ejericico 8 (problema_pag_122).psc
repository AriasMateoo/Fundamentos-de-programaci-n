Algoritmo problema_pag_122
	// Pedimos los valores de los coeficientes
	Escribir 'Ingresa el valor de A:'
	Leer A
	Escribir 'Ingresa el valor de B:'
	Leer B
	Escribir 'Ingresa el valor de C:'
	Leer C
	// Calculamos el discriminante
	Disc <- B^2-4*A*C
	// Verificamos si la ecuaci�n tiene soluci�n
	Si Disc<0 Entonces
		Escribir 'La ecuaci�n no tiene soluci�n.'
	SiNo
		// Calculamos las ra�ces
		RaizDisc <- raiz_cuadradaDisc
		x1 <- (-B+RaizDisc)/(2*A)
		x2 <- (-B-RaizDisc)/(2*A)
		// Mostramos las ra�ces
		Escribir 'Las ra�ces son:'
		Escribir 'x1 =',x1
		Escribir 'x2 =',x2
	FinSi
FinAlgoritmo
