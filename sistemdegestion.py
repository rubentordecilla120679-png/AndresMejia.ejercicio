
inventario = []
def registrar_componente():

    print("REGISTRAR")

    id_componente = input("Ingrese el ID del componente: ")

    repetido = False

    for componente in inventario:
        if componente["id"] == id_componente:
            repetido = True

    if repetido:
        print("Error El ID ya existe")
    else:

        nombre = input("Ingrese el nombre: ")
        categoria = input("Ingrese la categoria: ")

        while True:
            try:
                stock = int(input("Ingrese el stock: "))

                if stock >= 0:
                    break
                else:
                    print("El stock no puede ser negativo.")

            except ValueError:
                print("Ingrese un numero entero valido.")

        while True:
            try:
                precio = float(input("Ingrese el precio unitario: "))

                if precio >= 0:
                    break
                else:
                    print("El precio no puede ser negativo.")

            except ValueError:
                print("Ingrese un precio valido.")

        componente = {
            "id": id_componente,
            "nombre": nombre,
            "categoria": categoria,
            "stock": stock,
            "precio_unitario": precio
        }
        inventario.append(componente)

        print("Componente registrado correctamente.")

def mostrar_inventario():

    print("\n--- INVENTARIO COMPLETO ---")

    if len(inventario) == 0:
        print("El inventario esta vacio.")

    else:

        for componente in inventario:

            print("-------------------------")
            print("ID:", componente["id"])
            print("Nombre:", componente["nombre"])
            print("Categoria:", componente["categoria"])
            print("Stock:", componente["stock"])
            print("Precio:", componente["precio_unitario"])

def filtrar_categoria():

    print("\n--- FILTRAR POR CATEGORIA ---")

    categoria_buscar = input("Ingrese la categoria: ")

    encontrado = False

    for componente in inventario:

        if componente["categoria"].lower() == categoria_buscar.lower():

            print("-------------------------")
            print("ID:", componente["id"])
            print("Nombre:", componente["nombre"])
            print("Categoria:", componente["categoria"])
            print("Stock:", componente["stock"])
            print("Precio:", componente["precio_unitario"])

            encontrado = True

    if encontrado == False:
        print("No hay componentes en esa categoria.")


def actualizar_stock():

    print("ACTUALIZAR STOCK")

    id_buscar = input("Ingrese el ID del componente: ")

    encontrado = False

    for componente in inventario:

        if componente["id"] == id_buscar:

            encontrado = True

            print("Componente:", componente["nombre"])
            print("Stock actual:", componente["stock"])

            print("1. Agregar unidades")
            print("2. Retirar unidades")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":

                try:
                    cantidad = int(input("Cuantas unidades desea agregar: "))

                    if cantidad > 0:

                        componente["stock"] = componente["stock"] + cantidad

                        print("Stock actualizado correctamente.")
                        print("Nuevo stock:", componente["stock"])

                    else:
                        print("La cantidad debe ser mayor que cero.")

                except ValueError:
                    print("Ingrese un numero entero valido.")

            elif opcion == "2":

                try:
                    cantidad = int(input("Cuantas unidades desea retirar: "))

                    if cantidad > 0:

                        if cantidad <= componente["stock"]:

                            componente["stock"] = componente["stock"] - cantidad

                            print("Stock actualizado correctamente.")
                            print("Nuevo stock:", componente["stock"])

                        else:
                            print("Error: No hay suficiente stock.")

                    else:
                        print("La cantidad debe ser mayor que cero.")

                except ValueError:
                    print("Ingrese un numero entero valido.")

            else:
                print("Opcion no valida.")

    if encontrado == False:
        print("No se encontro un componente con ese ID.")



def menu():

    while True:

        print("\n================================")
        print(" LABORATORIO DE ROBOTICA")
        print(" SISTEMA DE INVENTARIO")
        print("================================")

        print("1. Registrar componente")
        print("2. Mostrar inventario")
        print("3. Filtrar por categoria")
        print("4. Actualizar stock")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            registrar_componente()

        elif opcion == "2":

            mostrar_inventario()

        elif opcion == "3":

            filtrar_categoria()

        elif opcion == "4":

            actualizar_stock()

        elif opcion == "5":

            print("Gracias por utilizar el sistema.")
            break

        else:

            print("Opcion incorrecta. Intente nuevamente.")

menu()
