

"""
 PONER EL TIPO DE DATO , EJEMPLO FLOAT(INPUT(""))

AL PEDIR DATOS AL USUARIO ANTES DE SOLO PEDIR CON LA FUNCION INPUT

DEFINIR EL TIPO DE DATO PARA ASI EVITAR PROBLEMAS

"""

salario = float(input("DIGITE SU SALARIO EN COLONES \n "))
gastosbasicos =  float(input("DIGITE CUANTO DINERO GASTA EN GASTOS BASICOS"+ "EJEMPLO, COMIDA , AGUA, LUZ, INTERNET, ETC \n "))
gastosvariables = float(input("DIGITE CUANTO DINERO GASTA EN GASTOS VARIABLES"+ "EJEMPLO, ROPA ,COMIDAEXPRES ,CINE,ETC \n ")) 
ahorro =  float(input("DIGITE CUANTO DINERO AHORRA AL MES \n "))


sumatotal = gastosbasicos+gastosvariables



if sumatotal<=salario:

    print("USTED ADMINISTRA BIEN EL DINERO \n ")

else:
                                                                                                        
    print("USTED NO ADMINISTRA BIEN SU DINERO  \n ")
    print("USTED DEBERIA GASTAR EN GASTOS BASICOS:      \n"         +str(salario * 0.50)) 
    print("USTED DEBERIA GASTAR EN GASTOS VARIABLES:        \n"     +str(salario* 0.40)) 
    print("USTED DEBERIA AHORRAR AL MES:        \n"                 +str(salario* 0.10)) 



"""
AL MOSTRAR DATOS O LOS RESULTADOS AL USUARIO IMPRIMIRLOS SIEMPRE CON STRING 

PARA HACER ESO APLICAMOS LA FUNCION str() PARA ASI CONVERTIR LOS DATOS EN STRING

"""

