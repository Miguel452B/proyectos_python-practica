
print("Digite el primer numero")
numero1 = int(input())

print("Digite el segundo numero")
numero2 = int(input()) 

        
def sumar(n1suma,n2suma):
    sumadenumeros = n1suma+n2suma
    print("EL RESULTADO DE LA SUMA ES  ",str(sumadenumeros))



def resta(n1resta,n2resta):
    restadenumeros = n1resta-n2resta
    print("EL RESULTADO DE LA RESTA ES  ",str(restadenumeros))



def multiplicacion(n1multi,n2multi):
    multiplicaciondenumeros = n1multi*n2multi
    print("EL RESULTADO DE LA MULTIPLICACION ES  ",str(multiplicaciondenumeros))



def division(n1div,n2div):
    divisiondenumeros = n1div/n2div
    print("EL RESULTADO DE LA DIVISION ES  " ,str(divisiondenumeros))

menu = """
    BIENVENIDO AL SISTEMA DE OPERACIONES MATEMATICAS
    *********************
    * 1-SUMA            *
    *                   *
    *                   *             
    * 2-RESTA           *
    *                   *
    *                   *
    * 3-MULTIPLICACION  *
    *                   *
    *                   *
    * 4-DIVISION        *
    *********************                   
                                
  PORFAVOR SELECCIONE UNA OPCION  

  

"""
print(menu)


respuesta = int(input("ELIJA UNA OPCION"))

if respuesta == 1:
    sumar(numero1,numero2)
elif respuesta == 2:
    resta(numero1,numero2)

elif respuesta == 3:
    multiplicacion(numero1,numero2)  
elif respuesta == 4:
    division(numero1,numero2)

else:
   print("EL NUMERO QUE DIGITO NO ESTA ENTRE LAS OPCIONES DISPONIBLES")

     









 