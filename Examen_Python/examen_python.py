class Libro:
    lista_titulos = []

    def __init__(self, titulo, autor, editorial, precio, ano_publicacion):
        self.__titulo = titulo.strip()
        self.__autor = autor.strip()
        self.__editorial = editorial.strip()
        self.__precio = precio
        self.__ano_publicacion = ano_publicacion
        self.lista_titulos.append(titulo)

    def get_precio(self):
        return self.__precio
    
    def get_titulo(self):
        return self.__titulo
    
    def mostrar_informacion(self):
        cadena = "*****************\n"
        cadena += "Título: " + self.__titulo + "\n"
        cadena += "Autor: " + self.__autor + "\n"
        cadena += "Editorial: " + self.__editorial + "\n"
        cadena += "Año: " + str(self.__ano_publicacion) + "\n"
        cadena += "Precio " + str(self.__precio)

        return cadena

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 101 or porcentaje > 0:
            self.__precio = self.__precio - (self.__precio * (porcentaje / 100))

    def comparar_precio(self, libro):
        if(self.__precio > libro.get_precio()):
            return "El libro " + self.__titulo + " es más caro."
        else:
            return "El libro " + libro.get_titulo() + " es más caro."
        

class LibroElectronico(Libro):
    def __init__(self, titulo, autor, editorial, precio, ano_publicacion, formato):
        super().__init__(titulo, autor, editorial, precio, ano_publicacion)

        try:
            if formato.lower() in ["pdf", "epub", "mobi"]:
                self.__formato = formato
        except Exception:
            print("Formato incorrecto")
        
    def descargar(self):
        return "El libro " + self.get_titulo() + " se ha descargado en formato " + self.__formato
    
    def mostrar_informacion_electronica(self):
        cadena = super().mostrar_informacion() + "\n"
        cadena += "Formato: " + self.__formato

        return cadena
    
    def cambiar_formato(self, formato):
        if formato.lower() in ["pdf", "epub", "mobi"]:
            self.__formato = formato
        else: 
            raise Exception
        

libro_1 = Libro("Un mundo feliz", "Aldous Huxley", "Plaza & Janés", 19.90, 1932)
libro_2 = Libro("Canción de fuego y hielo", "George R.R. Martin", "Gigamesh", 30, 1996)
libro_electronico = LibroElectronico("El Hobbit", "J.R.R. Tolkien", "Minotaurio", 4.95, 1937, "ePub")

print(libro_1.mostrar_informacion())
print(libro_2.mostrar_informacion())
print(libro_electronico.mostrar_informacion_electronica())
print(libro_electronico.descargar())

libro_2.aplicar_descuento(30)
print(libro_2.mostrar_informacion())

print(libro_1.comparar_precio(libro_2))

libro_electronico.cambiar_formato("pdf")
print(libro_electronico.mostrar_informacion_electronica())

print(Libro.lista_titulos)