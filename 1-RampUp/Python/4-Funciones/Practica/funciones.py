# Escribe una función que convierta números del 1 al 7 en nombres de los dias de la semana. 
# La función constará de un único argumento numérico y una salida de tipo string

#EJERC_1 
def dias_semana(numeros):
    semana = {1 : "Lunes",
     2 : "Martes",
     3 : "Miercoles",
     4 : "Jueves",
     5 : "Viernes",
     6 : "Sabado", 
     7 : "Domingo" }
    return semana[numeros]


# EJER_2

# En el ejercicio 8 de flujos de control, creábamos una pirámide invertida de números desde el 5. 
# Crea una función que replique el comportamiento de la pirámide,
# y utiliza un único parámetro de entrada de la función para determinar el número de filas de la pirámide.
def piramide(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ") 
        print("\n")
  
  
        
  #EJER_3
        
#  Escribe una función que compare dos números. La función tiene dos argumentos y hay tres salidas posibles:
# que sean iguales, que el primero sea  mayor que el segundo, o que el segundo sea mayor que el primero


def comparac(i,j):
    if i == j:
        print("Los numeros", i, "y", j,"Son iguales")
    elif i > j:
        print("El número", i, "Es mayor qué", j)
    elif i < j:
        print("El número",i, "Es menor que", j)
        
        


   
    
    
    
#EJER_4

# Escribe una función que sea un contador de letras. En el primer argumento 
    # tienes que introducir un texto, y el segundo que sea una letra que contar.
    # La función tiene que devolver un entero con el número de veces que aparece esa letra, tanto mayúscula, como minúscula
    


def contador(texto, n):
    texto = texto.lower()
    for i in texto: #recorremos cada carácter en el texto
        texto == n #compara si el caracter q recorre será igual a la que representa la letra q pongamos al llamar a la funcion
    return int(texto.count(n)) #lo trasnformamos primero a entero y...
# metodo count que cuenta cuantas veces aparece la letra elegida en el text



#ejemplo clase
def ejerc_4(frase, letra):
    return frase.count(letra)

def limpieza_text(texto, dict_vocales={"á": "a",
                                       "é": "e",
                                       "í": "i",
                                       "ó": "o",
                                       "ú": "u"}):
    print("convirtiendo texto a minúsculas")
    texto = texto.lower()
    
    for clave in dict_vocales:
        print("Reemplazando", clave, "por", dict_vocales[clave])
        texto = texto.replace(clave, dict_vocales[clave])
    print("nuevo texto", texto)
    
    return texto

def ejer_4(texto,letra):
    texto = limpieza_text(texto)
    return texto.count(letra)




#EJER_5

# Escribe una función que tenga un único argumento, un string. La salida de la función tiene que ser 
# un diccionario con el conteo de todas las letras de ese string, 
# siendo la clave la letra y el valor el conteo.



def contador2(texto):
    conteo = {}  #abrimos una biblioteca vacía
    for letra in texto: #recorremos cada índice del texto que ponemos
        if letra not in conteo.keys(): #si la letra NO está en la biblioteca llamada conteo.keys(), 
            conteo[letra] = 1 #se incluirá esa letra con un valor 1, porque de momento, solo tenemos 1
        else:  #si aparece otra letra igual, ya que no puede haber dos claves iguales, se le añade al valor un +1
            conteo[letra] = conteo[letra] + 1
        
    return conteo



# EJER_6
# Escribir una función que añada o elimine elementos en una lista. La función necesita los siguientes argumentos:
# lista: la lista donde se añadirán o eliminarán los elementos
# comando: "add" o "remove"
# elemento: Por defecto es None.

# Tendrá como salida la lista

def lista_mutable(lista, comando, elemento = None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        lista.remove(elemento)
    return lista
    
    
    
# ejemplo clase
def modificar(lista, elem, remove = False):
    if remove == True:
        #lista.remove(elem)     usando el try except capturando el remove en el try, este no es necesario
        
        try:
            lista.remove(elem)
        except ValueError:
            print("El valor no está en la lista")
            
    else: 
        lista.append(elem)
        
        


# EJER_ 7
# Crea una función que reciba 
# un número arbitrario de palabras, 
# y devuelva una frase completa, separando las palabras con espacios.

def crear_frase(*palabras):#todas las palabras se reciben como una tupla
    frase = " ".join(palabras) #una variable nueva para añadir (con join) un espacio en cada palabra que añadamos
    print(frase)
    
    
    
#EJER_8

# Escribe un programa que obtenga el enésimo número de la [serie de Fibonacci]
# Tienes que crear una función recursiva con un único argumento.

def fib(n):
    if n < 2:  #si es menor que dos, o [0,1], se imprime el propio número
        return n
    else:
        return fib(n - 1) + fib(n -2) #en caso de ser mayor, se vuelvea llamar a la funcion haciend la peración
    
    #esto sirve para los árboles de decisión
    
    
    
# EJER_9


# Define en una única celda las siguientes funciones: Función que calcule el área de un cuadrado
# Función que calcule el área de un triángulo
# Función que calcule el área de un círculo


def cuadrado(lado):
    area = lado * lado
    return area

def triangulo(base, altura):
    area = (base * altura) /2
    return area

def circulo(radio):
    area = math.pi * radio**2
    return round(area, 2)

