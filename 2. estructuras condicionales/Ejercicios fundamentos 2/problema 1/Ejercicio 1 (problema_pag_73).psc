Algoritmo problema_pag_73
	// Declaraci�n de variables
	Definir nombre Como Caracter
	Definir horasTrabajadas Como Entero
	Definir impuesto Como Real
	Definir salarioNeto Como Real
	Definir salarioBruto Como Real
	// Entrada de datos
	Escribir 'Ingrese el nombre del trabajador: '
	Leer nombre
	Escribir 'Ingrese el n�mero de horas trabajadas: '
	Leer horasTrabajadas
	// C�lculo del salario bruto
	salarioBruto <- horasTrabajadas*10000
	// C�lculo del impuesto a pagar
	impuesto <- salarioBruto*0.25
	// C�lculo del salario neto
	salarioNeto <- salarioBruto-impuesto
	// Salida de datos
	Escribir 'El salario bruto de ',nombre,' es: ',salarioBruto
	Escribir 'El impuesto a pagar es: ',impuesto
	Escribir 'El salario neto de ',nombre,' es: ',salarioNeto
FinAlgoritmo
