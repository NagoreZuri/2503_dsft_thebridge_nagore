import pprint

# primera función de VISUALIZAR CATÁLOGO DE LIBROS
def imprimir_libros(libros):
        pprint.pprint(libros)

#buscar libro por título

def buscar_libro(libros):
    titulo_buscar = input("Introduce el título del libro: ")
    #print(titulo)
    for libro in libros:
        titulo = libro['Titulo']
        #print(titulo)
        if titulo == titulo_buscar:
            print("Libro encontrado")
            print(titulo)
            break
        # else:
            otra_busqueda = input("Libro no encontrado. ¿Quieres probar con otro titulo? Responde si o no")
            if otra_busqueda == "si":
                buscar_libro(libros)
            else:
                break


# Añadir libro: solicitar el título y autor y añadirlo a la lista

def meter_libro(libros):
    titulo = input("Introduce el titulo del libro:").lower()
    autor = input("Introduce el nombre del autor")
    libros.append({"Titulo": titulo, "Autor": autor, "Alquilado": False})
    libro_nuevo = titulo + " de " + autor
    print("El nuevo libro añadido es:", libro_nuevo)
    return


#Eliminar un libro: slicitando el título Solamente

def eliminar_libro(libros):
    titulo = input("Introduce el titulo del libro:").lower()
    for libro in libros:
        libro_lower = str(libro["Titulo"])
        if libro_lower.lower() == titulo: #con esto accedemos a la clave titulo y comparamos cn el titulo que pone el usuario
            libros.remove(libro) #eliminamos el libro completo
    print("El libro eliminado es", titulo)
    return


# Alquilar libro solicitando título

def alquilar_libro(libros):
    titulo = input("Introduce el titulo el libro que quieres alquilar").lower()
    for libro in libros:
        if libro["Alquilado"] == False:
            libro["Alquilado"] = True
            print("Perfecto, ya está alquilado")
            break
        else:
            otro_titulo = input("Este libro ya está alquilado. ¿Quieres probar con otro? responde si o no")
            if otro_titulo == "si":
                alquilar_libro(libros)
            else:
                break
            


#devolver un libro 

def devolver_libro(libros):
    titulo = input("Introduce el titulo el libro que quieres devolver").title()
    for libro in libros:
        if libro["Alquilado"] == True:
            libro["Alquilado"] = False
            print("Perfecto, ya está devuelto")
            break
        else:
            otro_titulo = input("Este libro ya está devuelto. ¿Quieres probar con otro? responde si o no")
            if otro_titulo == "si":
                devolver_libro(libros)
            else:
                break





libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]




# ejemplo para UN MENU DEL PROFESOR


while True:
    opcion = input("Elige una opción: Visualizar/ Buscar/ Añadir/ Eliminar/ Alquilar/ Devolver/ Salir:  ").lower()
    match opcion:
        case "visualizar":
            imprimir_libros(libros)
        case "buscar":
            buscar_libro(libros)
        case "añadir":
            meter_libro(libros)
        case "eliminar":
            eliminar_libro(libros)
        case "alquilar":
            alquilar_libro(libros)
        case "devolver":
            devolver_libro(libros)
        case "salir":
            break