print("BIENVENIDO AL SISTEMA DE REGISTRO DE NOMBRES FAVORITOS " )
print("DIGITE 1 PARA GUARDAR EL NOMBRE EN LA LISTA")
print("DIGITE 2 PARA VERIFICAR SI EL NOMBRE ESTA EN LA LISTA")
print("DIGITE 3 PARA ELIMINAR EL NOMBRE QUE ESTA EN LA LISTA")
print("DIGITE 4 SI LO QUE DESEA ES SALIR DEL SISTEMA")

lista = []

respuesta = int((input()))

def guardarnombre(gn):
    lista.append(nombre)




def nombreverificacion(nv):
    if nombre in lista:
        print("SU NOMBRE  ESTA EN LA LISTA  "  +nombre)



    
def eliminarnombre(elimnarn):
     
     lista.append(nombre)
     lista.remove(nombre)
    
    
    
    
boleano = True
while boleano == True:  
    print("Digite un nombre")
    nombre = input()
    boleano = boleano + 1 
           
     


if respuesta == 1:
    guardarnombre(nombre)
    print("su nombre    "  +nombre + "se ha guardado correctamente" )

if respuesta == 2:
    nombreverificacion(nombre)
    print("EL NOMBRE " +nombre +"que digito existe en la lista")



if respuesta == 3:
    eliminarnombre(nombre)
    print("El nombre favorito " + nombre+ "que usted digito fue eliminado")

elif respuesta == 4:
    print("USTED HA SALIDO DEL SISTEMA DE REGISTRO DE NOMBRES") 