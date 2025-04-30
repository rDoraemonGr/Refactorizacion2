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

def pedir_datos_basicos(): # Función para pedir los datos básicos
    fecha_caducidad = input("Fecha de caducidad: ")
    numero_lote = input("Número de lote: ")
    peso = float(input("Peso (kg): "))
    medida = input("Medidas (cm): ")
    return fecha_caducidad, numero_lote, peso, medida

def eliminar_producto(lista):  # Función de eliminación de producto
    if not lista:
        print("No hay productos para eliminar.")
        return
    for i, prod in enumerate(lista):
        print(f"{i + 1}. {prod}")
    try:
        pos = int(input("¿Qué producto desea eliminar? (número): ")) - 1
        if 0 <= pos < len(lista):
            eliminado = lista.pop(pos)
            print(f"Producto eliminado: {eliminado}")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida.")


def obtener_coste_envio(lista):  # Función para mostrar el coste de envio
    if not lista:
        print("No hay productos para calcular el envío.")
        return
    for i, prod in enumerate(lista):
        print(f"{i + 1}. {prod}")
    try:
        pos = int(input("Seleccione el producto: ")) - 1
        if 0 <= pos < len(lista):
            coste = lista[pos].calcular_coste_envio()
            print(f"Coste de envío: {coste:.2f} €")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def main():
    productos_frescos = []
    productos_refrigerados = []
    productos_congelados = []

    while True:
        print("Gestión de Productos")
        print("1. Agregar producto fresco")
        print("2. Agregar producto refrigerado")
        print("3. Agregar producto congelado")
        print("4. Mostrar productos frescos")
        print("5. Mostrar productos refrigerados")
        print("6. Mostrar productos congelados")
        print("7. Eliminar producto fresco")                # Opción para eliminar un tipo de producto
        print("8. Eliminar producto refrigerado")           # Opción para eliminar un tipo de producto
        print("9. Eliminar producto congelado")             # Opción para eliminar un tipo de producto
        print("10. Ver coste envío producto fresco")        # Opción para ver el coste de envío de un tipo de producto
        print("11. Ver coste envío producto refrigerado")   # Opción para ver el coste de envío de un tipo de producto
        print("12. Ver coste envío producto congelado")     # Opción para ver el coste de envío de un tipo de producto
        print("13. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = pedir_datos_basicos()
            fecha_env = input("Fecha de envasado: ")
            pais = input("País de origen: ")
            productos_frescos.append(Frescos(*datos, fecha_env, pais))

        elif opcion == "2":
            datos = pedir_datos_basicos()
            cod = input("Código de supervisión: ")
            productos_refrigerados.append(Refrigerados(*datos, cod))

        elif opcion == "3":
            datos = pedir_datos_basicos()
            temp = input("Temperatura recomendada: ")
            productos_congelados.append(Congelados(*datos, temp))

        elif opcion == "4":
            print("--- Productos Frescos ---")
            for p in productos_frescos:
                print(p)

        elif opcion == "5":
            print("--- Productos Refrigerados ---")
            for p in productos_refrigerados:
                print(p)

        elif opcion == "6":
            print("--- Productos Congelados ---")
            for p in productos_congelados:
                print(p)

        elif opcion == "7":
            eliminar_producto(productos_frescos)
        elif opcion == "8":
            eliminar_producto(productos_refrigerados)
        elif opcion == "9":
            eliminar_producto(productos_congelados)

        elif opcion == "10":
            obtener_coste_envio(productos_frescos)
        elif opcion == "11":
            obtener_coste_envio(productos_refrigerados)
        elif opcion == "12":
            obtener_coste_envio(productos_congelados)

        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intentalo de nuevo.")
main()