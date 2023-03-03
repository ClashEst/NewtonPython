import numpy as np
import os

xk=0
yk=0
zk=0

xk_a=0
yk_a=0
zk_a=0

s1= 's'
s2= 'S'

si1= str(s1)
si2= str(s2)

opci1=0
tole=0
Maxite=0

def ESystem1(x,y):
    matriz=[[x*x + x*y -10],[y + 3*x*y*y - 50]]
    A=np.array(matriz)
    return A


def ESystem2(x,y):
    matriz=[[x*x + y*y - 9],[ - np.exp(x) - 2*y - 3]]
    A=np.array(matriz)
    return A


def ESystem3(x,y,z):
    matriz=[[2*x*x - 4*x + y*y + 3*z*z + 6*z + 2],[ x*x + y*y - 2*y + 2*z*z - 5],[3*x*x - 12*x + y*y - 3*z*z + 8]]
    A=np.array(matriz)
    return A        


def ESystem4(x,y,z):
    matriz=[[x*x - 4*x + y*y],[ x*x - x - 12*y + 1],[3*x*x - 12*x + y*y - 3*z*z + 8]]
    A=np.array(matriz)
    return A


def Jacobiana1(x,y):
    matriz=[[2*x + y, x],[3*(y**2), 1 + 6*x*y]]
    A= np.array(matriz)
    A= np.linalg.inv(A)
    return A
    

def Jacobiana2(x,y):
    matriz=[[2*x, 2*y],[- np.exp(x), -2]]
    A= np.array(matriz)
    A= np.linalg.inv(A)
    return A


def Jacobiana3(x,y,z):
    matriz=[[4*x - 4, 2*y, 6*z + 6],[2*x, 2*y - 2, 4*z],[6*x - 12, 2*y, -6*z]]
    A= np.array(matriz)
    A= np.linalg.inv(A)
    return A


def Jacobiana4(x,y,z):
    matriz=[[2*x - 4, 2*y, 0],[2*x - 1, -12*y - 2, 0],[6*x - 12, 2*y, -6*z]]
    A= np.array(matriz)
    A= np.linalg.inv(A)
    return A
    


while True: 

    print("Clemente Galicia Mario Luis")
    print("Cipres Flores Luis Angel")
    print("Cristian Jair Espejel Cárdenas")
    print("Miramontes Ordoñez Luis Carlos ")

    


    while True:
        os.system("cls")
        print("Metodo de Newton")
        print("1.- f1(x,y)= x^2 + xy - 10 = 0")
        print("    f2(x,y)= y + 3x(y^2) - 50 = 0")

        print("2.- f1(x,y)= x^2 + y^2 - 9 = 0")
        print("    f2(x,y)= -e^x - 2y - 3 = 0")

        print("3.- f1(x,y,z)= 2x^2 - 4x + y^2 + 3z^2 + 6z + 2 = 0")
        print("    f2(x,y,z)= x^2 + y^2 - 2y + 2z^2 - 5 = 0")
        print("    f3(x,y,z)= 3x^2 - 12x + y^2 - 3z^2 + 8 = 0")

        print("4.- f1(x,y,z)= x^2 - 4x + y^2 = 0")
        print("    f2(x,y,z)= x^2 - x - 12y + 1 = 0")
        print("    f3(x,y,z)= 3x^2 - 12x + y^2 - 3z^2 + 8 = 0")

        opci1= int(input("Cual Sistema desea resolver por el Metodo de Newton?"))

        if(opci1 == 1): 

            os.system("cls")

            while True:
                
                print("Punto inicial?")
                xk= int(input("x= "))
                yk= int(input("y= "))
                tole= float(input("Indique tolerancia maxima "))
                Maxite= int(input("Numero de Iteraciones"))

                xk_b= xk
                yk_b= yk

                Ea=0
                ite=0

                while (ite<Maxite):
                    print(f"\n Iteracion {ite}")

                    xk_a= xk
                    yk_a= yk

                    Xa=np.array([[xk],[yk]])
                    Mja= Jacobiana1(xk,yk)
                    Ma= ESystem1(xk,yk)
                    
                    Xa_1= Xa - np.matmul(Mja,Ma)
                    print(Xa_1)
                    xk= Xa_1[0,0]
                    yk= Xa_1[1,0]

                    Ea= max(abs(xk - xk_a), abs(yk - yk_a))
                    print(f"Error absoluto {Ea}")
                    if(Ea<tole):
                        break

                    ite+=1
                
                print(f"\n El vector solución es deacuerdo al punto inicial es: ({xk_b} , {yk_b}) es: ")
                print(Xa_1)
                print(f"Error Absoluto: {Ea}")

                opci2= str(input("¿Cambiar el punto inicial? (S/N): "))

                if(opci2 != si1 and opci2 != si2):
                    break

        elif(opci1 == 2):

            os.system("cls")

            while True:
                
                print("Punto inicial")
                xk= int(input("x= "))
                yk= int(input("y= "))
                tole= float(input("Indique una tolerancia maxima "))
                Maxite= int(input("Numero de Iteraciones "))

                xk_b= xk
                yk_b= yk

                Ea=0
                ite=0

                while (ite<Maxite):
                    print(f"\n Iteracion {ite}")

                    xk_a= xk
                    yk_a= yk

                    Xa=np.array([[xk],[yk]])
                    Mja= Jacobiana2(xk,yk)
                    Ma= ESystem2(xk,yk)
                    
                    Xa_2= Xa - np.matmul(Mja,Ma)
                    print(Xa_2)
                    xk= Xa_2[0,0]
                    yk= Xa_2[1,0]

                    Ea= max(abs(xk - xk_a), abs(yk - yk_a))
                    print(f"Error absoluto {Ea}")
                    if(Ea<tole):
                        break

                    ite+=1
                
                print(f"\n Vector solucion deacuerdo al punto inicial obtenido({xk_b} , {yk_b}) es: ")
                print(Xa_2)
                print(f"Con un error absoluto de {Ea}")

                opci2= str(input("¿Cambiar el punto inicial? (S/N): "))

                if(opci2 != si1 and opci2 != si2):
                    break

        elif(opci1 == 3):
            os.system("cls")

            while True:
                
                print("Punto Inicial")
                xk= int(input("x= "))
                yk= int(input("y= "))
                zk= int(input("z= "))
                tole= float(input("Indique una tolerancia maxima "))
                Maxite= int(input("Numero de Iteraciones"))

                xk_b= xk
                yk_b= yk
                zk_b= zk
                
                Ea=0
                ite=0

                while (ite<Maxite):
                    print(f"\n Iteracion {ite}")

                    xk_a= xk
                    yk_a= yk
                    zk_a= zk

                    Xa=np.array([[xk],[yk],[zk]])
                    Mja= Jacobiana3(xk,yk,zk)
                    Ma= ESystem3(xk,yk,zk)
                    
                    Xa_3= Xa - np.matmul(Mja,Ma)
                    print(Xa_3)
                    xk= Xa_3[0,0]
                    yk= Xa_3[1,0]
                    zk= Xa_3[2,0]

                    Ea= max(abs(xk - xk_a), abs(yk - yk_a), abs(zk - zk_a))
                    print(f"Error absoluto {Ea}")
                    if(Ea<tole):
                        break

                    ite+=1
                
                print(f"\n Vector solución deacuerdo al punto inicial ({xk_b} , {yk_b} , {zk_b}) es: ")
                print(Xa_3)
                print(f"Con un error absoluto de {Ea}")

                opci2= str(input("¿Cambiar el punto inicial? (S/N): "))

                if(opci2 != si1 and opci2 != si2):
                    break

        elif(opci1 == 4):
            os.system("cls")

            while True:
                
                print("Punto Inicial")
                xk= int(input("x= "))
                yk= int(input("y= "))
                zk= int(input("z= "))
                tole= float(input("Indique una tolerancia maxima "))
                Maxite= int(input("Numero de iteraciones"))

                xk_b= xk
                yk_b= yk
                zk_b= zk
                
                Ea=0
                ite=0

                while (ite<Maxite):
                    print(f"\n Iteracion {ite}")

                    xk_a= xk
                    yk_a= yk
                    zk_a= zk

                    Xa=np.array([[xk],[yk],[zk]])
                    Mja= Jacobiana4(xk,yk,zk)
                    Ma= ESystem4(xk,yk,zk)
                    
                    Xa_4= Xa - np.matmul(Mja,Ma)
                    print(Xa_4)
                    xk= Xa_4[0,0]
                    yk= Xa_4[1,0]
                    zk= Xa_4[2,0]

                    Ea= max(abs(xk - xk_a), abs(yk - yk_a), abs(zk - zk_a))
                    print(f"Error absoluto {Ea}")
                    if(Ea<tole):
                        break

                    ite+=1
                
                print(f"\n Vector solución deacuerdo al punto inicial ({xk_b} , {yk_b} , {zk_b}) es: ")
                print(Xa_4)
                print(f"Con un error absoluto de {Ea}")

                opci2= str(input("¿Cambiar el punto inicial? (S/N): "))

                if(opci2 != si1 and opci2 != si2):
                    break

        else:
            print("Error en la opcion")
            opci3=str(input("¿quieres volver a elegir una opcion? (S/N): "))
            if(opci3 != si1 and opci3 != si2):
                break
    
        opci3=str(input("¿Resolver otro sistema de ecuaciones no lineales del menu? (S/N): "))
        if(opci3 != si1 and opci3 != si2):
            os.system("cls")
            break

           
print("Hasta Pronto!")