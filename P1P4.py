import json
import os

# Nombre del archivo JSON donde se almacenarán los datos
FILE_NAME = 'presupuesto.json'


# Función para cargar los artículos del presupuesto desde el archivo JSON
def cargar_articulos():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as archivo:
        return json.load(archivo)


# Función para guardar los artículos en el archivo JSON
def guardar_articulos(articulos):
    with open(FILE_NAME, 'w') as archivo:
        json.dump(articulos, archivo, indent=4)


# Función para agregar un nuevo artículo
def agregar_articulo():
    descripcion = input("Descripción del artículo: ")
    cantidad = float(input("Cantidad: "))
    categoria = input("Categoría: ")

    nuevo_articulo = {
        'descripcion': descripcion,
        'cantidad': cantidad,
        'categoria': categoria
    }

    # Cargar los artículos existentes
    articulos = cargar_articulos()
    articulos.append(nuevo_articulo)

    # Guardar los artículos actualizados
    guardar_articulos(articulos)
    print(f"Artículo '{descripcion}' agregado exitosamente.")


# Función para ver todos los artículos
def ver_articulos():
    articulos = cargar_articulos()

    if articulos:
        print("\n--- Listado de Artículos ---")
        for idx, articulo in enumerate(articulos, 1):
            print(
                f"{idx}. Descripción: {articulo['descripcion']}, Cantidad: {articulo['cantidad']}, Categoría: {articulo['categoria']}")
    else:
        print("No hay artículos registrados en el presupuesto.")


# Función para buscar artículos por descripción
def buscar_articulo():
    descripcion_busqueda = input("Ingrese la descripción del artículo a buscar: ").lower()
    articulos = cargar_articulos()

    resultados = [articulo for articulo in articulos if descripcion_busqueda in articulo['descripcion'].lower()]

    if resultados:
        print(f"\n--- Resultados de la búsqueda para '{descripcion_busqueda}' ---")
        for idx, articulo in enumerate(resultados, 1):
            print(
                f"{idx}. Descripción: {articulo['descripcion']}, Cantidad: {articulo['cantidad']}, Categoría: {articulo['categoria']}")
    else:
        print(f"No se encontraron artículos con la descripción '{descripcion_busqueda}'.")


# Función para editar un artículo
def editar_articulo():
    ver_articulos()
    articulos = cargar_articulos()

    idx = int(input("\nIngrese el número del artículo que desea editar: ")) - 1

    if 0 <= idx < len(articulos):
        print("\n--- Edición de Artículo ---")
        descripcion = input(f"Descripción actual ({articulos[idx]['descripcion']}): ") or articulos[idx]['descripcion']
        cantidad = input(f"Cantidad actual ({articulos[idx]['cantidad']}): ")
        categoria = input(f"Categoría actual ({articulos[idx]['categoria']}): ") or articulos[idx]['categoria']

        if cantidad:
            cantidad = float(cantidad)

        articulos[idx] = {
            'descripcion': descripcion,
            'cantidad': cantidad if cantidad else articulos[idx]['cantidad'],
            'categoria': categoria
        }

        guardar_articulos(articulos)
        print(f"Artículo '{descripcion}' actualizado exitosamente.")
    else:
        print("Índice no válido.")


# Función para eliminar un artículo
def eliminar_articulo():
    ver_articulos()
    articulos = cargar_articulos()

    idx = int(input("\nIngrese el número del artículo que desea eliminar: ")) - 1

    if 0 <= idx < len(articulos):
        articulo_eliminado = articulos.pop(idx)
        guardar_articulos(articulos)
        print(f"Artículo '{articulo_eliminado['descripcion']}' eliminado exitosamente.")
    else:
        print("Índice no válido.")


# Función del menú principal
def menu():
    while True:
        print("\n--- Sistema de Registro de Presupuesto ---")
        print("1. Agregar nuevo artículo")
        print("2. Ver todos los artículos")
        print("3. Buscar artículo por descripción")
        print("4. Editar artículo")
        print("5. Eliminar artículo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_articulo()
        elif opcion == '2':
            ver_articulos()
        elif opcion == '3':
            buscar_articulo()
        elif opcion == '4':
            editar_articulo()
        elif opcion == '5':
            eliminar_articulo()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()