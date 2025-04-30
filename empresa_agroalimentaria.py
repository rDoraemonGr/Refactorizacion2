# Se plantea desarrollar un programa que permita la gestión de una empresa agroalimentaria que trabaja con tres tipos de productos:
# •	Productos frescos
# •	Productos refrigerados
# •	Productos congelados 
# Todos los productos llevan esta información común: fecha de caducidad y número de lote. 
# A su vez, cada tipo de producto lleva alguna información específica.
# •	Los productos frescos deben llevar la fecha de envasado y el país de origen.
# •	Los productos refrigerados deben llevar el código del organismo de supervisión alimentaria.
# •	Los productos congelados deben llevar la temperatura de congelación recomendada.
# Realiza un menú que pregunte qué tipo de producto se quiere crear y guárdalos en listas independientes para cada tipo.

# Sobrescribe la función __str__ para que se imprima la información de cada clase
# Añade las propiedades peso y medidas
# Implementa un método calcular_coste_envio:
# Cualquier producto costará enviarlo una cantidad relacionada con su peso: 3 euros por kilo
# Los productos congelados llevan un extra de 5 euros de transporte
# Los productos refrigerados llevan un extra de 2 euros de transporte
# Añade al menú la posibilidad de eliminar un producto. Para ello primero imprime una lista numerada y pregunta al usuario cuál quiere borrar.
# Añade al menú la opción de obtener el coste de envío de cualquier producto.


class Producto:
    def __init__(self, fecha_caducidad, numero_lote, peso, medida):
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
        self.peso = peso
        self.medida = medida

    def __str__(self): 
        return f"Caducidad: {self.fecha_caducidad} | Lote: {self.numero_lote} | Peso: {self.peso} kg | Medida: {self.medida}"

class Frescos(Producto):
    def __init__(self, fecha_caducidad, numero_lote, fecha_envasado, pais_origen):
        super().__init__(fecha_caducidad, numero_lote)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def __str__(self):  # Imprimimos los datos mas detalladamente
        return f"{super().__str__()} | Envasado: {self.fecha_envasado} | Origen: {self.pais_origen}"

    def calcular_coste_envio(self):  # Implemento método de calcular coste de envio
        return self.peso * 3
    
class Refrigerados(Producto):
    def __init__(self, fecha_caducidad, numero_lote, codigo_organismo_supervision):
        super().__init__(fecha_caducidad, numero_lote)
        self.codigo_organismo_supervision = codigo_organismo_supervision  
    
    def __str__(self):  # Imprimimos los datos mas detalladamente
        return f"{super().__str__()} | Código supervisión: {self.codigo_organismo_supervision}"
    
    def calcular_coste_envio(self):  # Implemento método de calcular coste de envio
        return super().calcular_coste_envio() + 2
    
class Congelados(Producto):
    def __init__(self, fecha_caducidad, numero_lote, temperatura_recomendada):
        super().__init__(fecha_caducidad, numero_lote)
        self.temperatura_recomendada = temperatura_recomendada

    def __str__(self):  # Imprimimos los datos mas detalladamente
        return f"{super().__str__()} | Temp. recomendada: {self.temperatura_recomendada}°C"
    
    def calcular_coste_envio(self):  # Implemento método de calcular coste de envio
        return super().calcular_coste_envio() + 5

def main():
    productos_frescos = []
    productos_refrigerados = []
    productos_congelados = []
    lista_productos_general = []

    while True:
        print("Gestión de Productos")
        print("1. Agregar producto fresco")
        print("2. Agregar producto refrigerado")
        print("3. Agregar producto congelado")
        print("4. Mostrar productos frescos")
        print("5. Mostrar productos refrigerados")
        print("6. Mostrar productos congelados")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fecha_caducidad = input("Fecha de caducidad: ")
            numero_lote = input("Número de lote: ")
            fecha_envasado = input("Fecha de envasado: ")
            pais_origen = input("País de origen: ")
            productos_frescos.append(Frescos(fecha_caducidad, numero_lote, fecha_envasado, pais_origen))

        elif opcion == "2":
            fecha_caducidad = input("Fecha de caducidad: ")
            numero_lote = input("Número de lote: ")
            codigo_organismo = input("Código de organismo de supervisión: ")
            productos_refrigerados.append(Refrigerados(fecha_caducidad, numero_lote, codigo_organismo))

        elif opcion == "3":
            fecha_caducidad = input("Fecha de caducidad: ")
            numero_lote = input("Número de lote: ")
            temperatura = input("Temperatura recomendada: ")
            productos_congelados.append(Congelados(fecha_caducidad, numero_lote, temperatura))

        elif opcion == "4":
            print("--- Productos Frescos ---")
            if productos_frescos:
                for p in productos_frescos:
                    print(f"Fecha de caducidad: {p.fecha_caducidad} - Número de lote: {p.numero_lote} - "
                          f"Fecha de envasado: {p.fecha_envasado} - País de origen: {p.pais_origen}")
            else:
                print("No hay productos frescos registrados.")

        elif opcion == "5":
            print("--- Productos Refrigerados ---")
            if productos_refrigerados:
                for p in productos_refrigerados:
                    print(f"Fecha de caducidad: {p.fecha_caducidad} - Número de lote: {p.numero_lote} - "
                          f"Código de supervisión: {p.codigo_organismo_supervision}")
            else:
                print("No hay productos refrigerados registrados.")

        elif opcion == "6":
            print("--- Productos Congelados ---")
            if productos_congelados:
                for p in productos_congelados:
                    print(f"Fecha de caducidad: {p.fecha_caducidad} - Número de lote: {p.numero_lote} - "
                          f"Temperatura recomendada: {p.temperatura_recomendada}°C")
            else:
                print("No hay productos congelados registrados.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intentalo de nuevo.")
main()
