from Nodos import listaSimple


def menu():
    opcion =''
    lis=listaSimple()
    while opcion != '7':
        print("-------------Menu-------------")
        print("1. Abrir archivo")
        print("2. Mostrar grafica")
        print("4. Ingresar Celula")
        print("5. Celdas para sobrevivir")
        print("6. Crear XML")
        print("7. Salir")

        opcion=input("Ingrese una de las opciones: ")
        if opcion== '1':
            print("carga de archivo")


menu()
                 


