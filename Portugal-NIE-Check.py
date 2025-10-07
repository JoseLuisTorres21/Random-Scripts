

def nie_check(nie):
    # Primero verificamos que el NIE es válido.
    if len(nie) != 9 or not nie.isdigit():
        print("El NIE introducido es erroneo, debe contener 9 dígitos numéricos.")
        return False
    
    
    # Paso 1 y 2
    suma = 0
    for i in range(1,9,1):
        peso = 10 - i
        result = int(nie[i-1]) * peso
        suma += result 
    
    # Paso 3, 4 y 5
    resto = suma % 11

    if resto in [0, 1]:
        Digito_control = 0
    else:
        Digito_control = 11 - (suma % 11)

    if Digito_control == int(nie[8]):
        print ("El NIE es válido.")
         
    else:   
        print ("El NIE no es válido.")
    

print("""██████╗  ██████╗ ██████╗ ████████╗██╗   ██╗ ██████╗  █████╗ ██╗         
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██║   ██║██╔════╝ ██╔══██╗██║         
██████╔╝██║   ██║██████╔╝   ██║   ██║   ██║██║  ███╗███████║██║         
██╔═══╝ ██║   ██║██╔══██╗   ██║   ██║   ██║██║   ██║██╔══██║██║         
██║     ╚██████╔╝██║  ██║   ██║   ╚██████╔╝╚██████╔╝██║  ██║███████╗    
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝    
                                                                        
███╗   ██╗██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗       
████╗  ██║██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝       
██╔██╗ ██║██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝        
██║╚██╗██║██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗        
██║ ╚████║██║██║         ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗       
╚═╝  ╚═══╝╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝       
                                                                        
Indica Algoritmo para más información respecto al algoritmo de validación.    """)


while True:
    # Ejemplo de uso
    nie = input("Introduce el NIE (9 dígitos numéricos): ")
    if nie.lower() == 'exit':
        break
    if nie == 'Algoritmo':
        print ("""
 1. Se multiplica el primer dígito por 9, el segundo por 8, el tercero por 7, y así sucesivamente hasta multiplicar el octavo dígito por 2.
 2. Se suman todos los resultados de estas multiplicaciones.
 3. Se calcula el resto de la división de esta suma entre 11.
 4. Si el resto es 0 ó 1, el dígito de control debe ser 0.
 5. Si el resto es otro número, el dígito de control se calcula restando ese número a 11.
               
               """)
    nie_check(nie)      