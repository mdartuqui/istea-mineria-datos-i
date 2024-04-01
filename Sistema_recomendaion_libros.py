class Libro:
  def __init__(self, titulo, autor, genero, puntuacion):
    self.titulo =titulo
    self.autor = autor
    self.genero = genero
    self.puntuacion = puntuacion

#Creacion de los objetos de la clase libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

# Creacion de la lista_libros
lista_libros =[libro1,libro2,libro3,libro4,libro5,libro6,libro7,libro8,libro9,libro10]

#Creación de la Funcion agregar libro

def agregar_libro():
    titulo = input ("Ingrese el titulo del libro: ").lower()
    autor = input ("Ingrese el Nombre del Autor: ").title()
    genero = input ("Ingrese el genero del libro: ").title()
    puntuacion = float (input("Ingrese la puntuación del libro: "))
    libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(libro)
    print ("Libro agregado correctamente")

# Buscar libro por genero

def buscar_libro_por_genero ():
    genero_buscar = input("Ingrese el genero que desea buscar : ").lower()
    libros_en_genero= [libro for libro in lista_libros if libro.genero.lower()==genero_buscar]
    if libros_en_genero:
        print("Libros encontrados en el género", genero_buscar.capitalize(), ":")
        for libro in libros_en_genero:
            print(f"Título: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Género: {libro.genero}")
            print(f"Puntuación: {libro.puntuacion}")
            print()
    else:
        print("No se encontraron libros en el género", genero_buscar.capitalize())

#Recomendar Libro

def recomendar_libro():
    genero_interes = input("Ingrese el genero de interes : ")
    libros_en_genero =[libro for libro in lista_libros if libro.genero.lower()== genero_interes.lower()]
    if libros_en_genero:
        mejor_libro = max(libros_en_genero, key = lambda libro: libro.puntuacion)
        print (f"Te recomendamos {mejor_libro.titulo} en el genero '{genero_interes}'")
    else:
        print (f"Lo siento no hsy libros en ese genero")
    
    
    
# Bucle principal

while True:
    print ("\n Opciones:")
    print("1. Agregar libro:")
    print("2. Buscar libro por genero:")
    print("3. Recomendar Libro:")
    print("4. Salir")
    opcion = input("Selecciones la opción(1/2/3/4):")
    
    if opcion == '1':
        agregar_libro()
    elif opcion =='2':
        buscar_libro_por_genero()
    elif opcion == '3':
        recomendar_libro()
    elif opcion == '4':
        print("Hasta luego")
        break
    else:
        print("Opción invalida, por favor ingrese una opcion valida")
        



print("Lista de Libros:")
for i, libro in enumerate(lista_libros, start=1):
    print(f"Libro {i}:")
    print(f"Título: {libro.titulo}")
    print(f"Autor: {libro.autor}")
    print(f"Género: {libro.genero}")
    print(f"Puntuación: {libro.puntuacion}")
    print()