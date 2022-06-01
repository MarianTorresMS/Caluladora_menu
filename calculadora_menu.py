# Calculadora basica con menu

from math import log

# input 
bandera = False 
X = float (input("Dame el valor del numero X:"))
Y = float (input("Dmane e lvalor de numero Y:"))

print ("Dame la opcion que deseas realizar : \n")

# se despliega el menu para seleccionar la opcion qu deseas realizar

print("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Logaritmo")

opcion= int(input("Dame la opcion: "))

# processing
if (opcion==1):
    Z=X+Y
    print(X," + ",Y)
elif (opcion ==2):
    Z=X-Y
    print(X," - ",Y)
elif (opcion==3):
    Z=X*Y
    print(X, "*",Y)
elif(opcion ==4):
    Z=X/Y
    print(X,"/",Y)    
elif(opcion==4 and Y==0):
    print("El denominador es iual a cero y")
    print("No se pude realizar la division")
    bandera = True
elif (opcion==5):
    Z= pow(X,Y) 
    print(X,"^",Y)
elif (opcion==6 and X>0):
    Z=log(X)
    print("Logaritmo de ",X)
elif(opcion==6 and X<=0):
    print("No se puede calcular el logaritmo")
    bandera=True
else:
    print("opcion no valida")   

# se escribe el resultado con otra condicion
if(opcion<7 and bandera==False):
    print("Resultado = ",Z)

#FIN



