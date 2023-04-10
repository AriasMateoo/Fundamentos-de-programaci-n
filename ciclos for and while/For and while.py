#calculo analisis del primer parcial de FP
v_sumNotPriPar = 0.0
v_canEst = 0
c_ValExaTeo = 0.40
c_valExaPra = 0.60
v_defPriPar = 0.0
v_conCic = 1
v_proNotPripar = 0.0
ASDEH= 0
ACEH= 0
# leer cantidad de estudiantes
v_canEst = int (input("digite cantidad de estudiantes :"))

for v_conCic in range (v_canEst):
 v_nomEst = input ("Nombre del estudiante:")
 v_genEst = input ("Genero del estudiante:")
 v_notExaTeo = float(input("Digite nota examente teorico: "))
 v_notExaPra = float(input("Digite nota examen practico: "))
#calculo de la nota definitiva
v_notDefpriPar = v_notExaTeo * c_ValExaTeo + v_notExaTeo * c_valExaPra
print ("Su nota del primer parcial es : ", v_notDefpriPar)
#calcula la suma de las notas de los estudiantes para calcular el promedio
v_sumNotPriPar = v_sumNotPriPar  + v_notDefpriPar 
#calcular el promedio del grupo de las notas del primer parcial
v_proNotPripar = v_sumNotPriPar / v_canEst
print ("El promedio del grupo del primer parcial es: ", v_proNotPripar)
#calcula el promedio del grupo por genero
input (v_canEst)
for v_conCic in range (v_canEst):
 input (v_nomEst, v_genEst)
 input (v_notExaTeo, v_notExaPra)
 NDPPE= v_notExaTeo * 0.60 + v_notExaPra * 0.40
 ASDE= ASDE+NDPPE
 if (v_genEst== "F"):
  ASDEM= ASDEM + NDPPE
 ACEM= ACEM + 1
print ("El promedio general del genero femenino es:", ACEM)
if (v_genEst=="M"):
  ASDEH= ASDEH + NDPPE 
  ACEH= ACEH + 1
print ("El promedio general del genero masculino es:", ACEH)





  

