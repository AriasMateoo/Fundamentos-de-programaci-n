#ejercicio 5.5

total = 0.0
v_canEst = 0
nota = 0.0
total = 0.0
print("introduzca las notas para hallar la media de estas, y escriba -99 para terminar")

	
nota = float(input())
while nota!=-99:
		total = total+nota
		v_canEst = v_canEst+1
		nota = float(input())
media = total/v_canEst
print("La media es:",media)

