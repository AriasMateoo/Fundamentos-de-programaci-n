Algoritmo problema_pag_123
	// declaracion de variables
	Definir num1,num2,num3 Como Entero
	// area de entrada
	Escribir 'digite numero 1'
	Leer num1
	Escribir 'digite numero 2'
	Leer num2
	Escribir 'digite numero 3'
	Leer num3
	// area de procesos
	si num1=num2 y num2=num3 Entonces
		escribir "los tres numeros son iguales"
	FinSi
	Si num1>num2 Y num1>num3 Entonces
		mayor <- num1
	FinSi
	Si num2>num1 Y num2>num3 Entonces
		mayor <- num2
	FinSi
	Si num3>num2 Y num2>num1 Entonces
		mayor <- num3
	FinSi
	Escribir 'el numero mayor es:',mayor
FinAlgoritmo
