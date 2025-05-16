from math import sqrt########importar las funciones math y sqrt
import math#######importamos math
def Manhattan (coord1,coord2):######definimos como representamos Manhattan
    x0, y0= coord1#######coordenadas de Manhattan
    x1, y1= coord2########3segunda coordenada de Manhattan
    return(x1-x0)+(y1-y0)######finalizamos la ejecucion para que arroje un valor

def Euclidiana (coord1, coord2):########definimos como representar Euclidiana
    x0, y0= coord1############primeras coordenadas de Euclidiana
    x1, y1= coord2##########segunda coordenada de Euclidiana
    return(x1-x0)+(y1-y0)########finalizamos la ejecucion de la misma para q arroje un valor

P1=(8,10)#######los valores aleatorios que usaremos
P2=(15,23)########los valores aleatorios qque usaremos

Resultado_Manhattan = Manhattan(P1,P2)######definimos como queremos el resultado 
Resultado_Euclidiana = Euclidiana(P1,P2)##########definimos el resultado
print("Distancia Manhattan:",Resultado_Manhattan)########imprimir la distancia y el resultado para arrojar un valor
print("Distancia Euclidiana:",Resultado_Euclidiana)#######imprimir la distancia y el resultado para arrojar un valor
