#8 de mayo
 #funciones
def mostrar_mayor (v1, v2, v3):
    print("el valor mayor de los tres numeros es: ")
    if v1>v2 and v1>v3:
        print (v1)
    else: 
        if v2>v3:
            print(v2)
        else: 
            print(v3)

def mostrar_menor (v1, v2, v3):
    print("el valor menor de los tres numeros es:")
    if v1<v2 and v1<v3:
        print (v1)
    else: 
        if v2<v3:
            print(v2)  
        else:
            print(v3)


def cargar ():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrse el segundo valor: "))
    valor3=int(input("Ingrese el tercer valor: "))
    mostrar_mayor(valor1, valor2, valor3)
    mostrar_menor(valor1, valor2, valor3)


valores = ['valor1, valor2, valor3']
for valores in range (4):
    if valores [valores] > valores [valores+1]:
        aux=valores [valores]
        valores[valores]=valores[valores+1]
        valores[valores+1]=aux

print ("lista con el ultimo elemento ordenado")
print(valores)



#programa principal

cargar()

