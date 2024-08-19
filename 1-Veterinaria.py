class Veterinaria:

    #Creamos nuestra clase llamada Veterinaria

    def __init__(self, peso=0, nombre="", clase="", color="", edad=0, genero=""):
        self.Estado = "NO ATENDIDO"
        self.peso = peso
        self.tamano = self.determinar_tamano()
        self.Nombre = nombre
        self.Clase = clase  
        self.Color = color
        self.Edad = edad
        self.Genero = genero

        #Seguidamente definimos la funcion y agregamos los datos que vamos a usar dentro de nuestra clase


    def determinar_tamano(self):
        if self.peso <= 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"
    # usamos def para determinar el tamaño del perrito y usamos la funcion if para verifcar si el perro en grande o pequeño

    def cambiar_estado(self):
        self.Estado = "ATENDIDO"
        return self.Estado
    #usamos el def para definir que luego de ingresar el dato el estado del perro pase de No atendido a Atendido

    def entrada_datos(self):
        self.Nombre = input("Nombre del Perro: ")
        self.Clase = input("Ingrese qué raza es su mascota: ")
        self.Color = input("Ingrese el color de su mascota: ")
        self.Edad = int(input("Ingrese la edad de su mascota: "))
        self.peso = int(input("Ingrese el peso de su mascota en kg: "))
        self.Genero = input("Ingrese el género de su mascota: ")
        self.tamano = self.determinar_tamano()  
    #Definimos los datos de entrada que el usuario ingresara

    def muestra_datos(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Raza: {self.Clase}")
        print(f"Color: {self.Color}")
        print(f"Edad: {self.Edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.Genero}")
        print(f"Estado: {self.Estado}")
    #Luego definimos la funcion para que nos muestre los datos ingresados anterior mente

perro = Veterinaria()  
perro.entrada_datos() 
perro.cambiar_estado()  
perro.muestra_datos()  

#Creamos las intancias para poder llamar los metodos dentro de nuestra clase

#Alumno Daniel Luna smss102123
#pongo mi nombre y codigo en el codigo por si no sabe de quien es si descarga muchos archivos are lo mismo con los daemas