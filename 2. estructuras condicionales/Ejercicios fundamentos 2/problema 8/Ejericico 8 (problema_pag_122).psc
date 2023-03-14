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
	// Verificamos si la ecuación tiene solución
	Si Disc<0 Entonces
		Escribir 'La ecuación no tiene solución.'
	SiNo
		// Calculamos las raíces
		RaizDisc <- raiz_cuadradaDisc
		x1 <- (-B+RaizDisc)/(2*A)
		x2 <- (-B-RaizDisc)/(2*A)
		// Mostramos las raíces
		Escribir 'Las raíces son:'
		Escribir 'x1 =',x1
		Escribir 'x2 =',x2
	FinSi
FinAlgoritmo
