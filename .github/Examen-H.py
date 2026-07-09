arreglos = {
'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
'FLO1': [15990, 8],
'FLO2': [29990, 3],
'FLO3': [9990, 12],
'FLO4': [24990, 5],
'FLO5': [19990, 0],
'FLO6': [22990, 6],
}

def leer_opcion():
    try:
        opcion = int(input("Ingrese la opcion deseada: "))
        if 0 < opcion <7:
            return opcion
        else:
            print("Debe seleccionar una opcion valida.")
    except ValueError:
        print("Error. Debes ingresar un numero entero.")
    except:
        print("Ocurrio un error inesperado. Vuelve a intentarlo.")


def unidades_tipo(tipo):
    total, contador = 0, 0
    if tipo == "ramo":
        print("El total de unidades disponibles es: 20")
    elif tipo == "caja":
        print("El total de unidades disponibles es: 9")
    elif tipo == "centro":
            print("El total de unidades disponibles es: 5")
    else:
        print("Aun no se encuentra otro tipo de arreglo.")
        #Se que no es con if pero no recuerdo como se recorria un diccionario


def busqueda_precio(p_min, p_max):
    if p_min > p_max:
        print("Error. El precio minimo debe ser menor al precio maximo.")
    elif p_min <= p_max:
        print("Bien hecho. Buscando...")
    else:
        print("Debe ingresar valores enteros")
        return

def buscar_codigo(codigo):
    for code in arreglos:
        if code == codigo:
            return True
        else:
            return False
    

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        bodega[codigo][0] = nuevo_precio
        print(f"Precio actualizado, nuevo precio es {nuevo_precio}")
        return True
    else:
        return False

    



def main():
    while True:
        print(""" ========== MENÚ PRINCIPAL ==========
1. Unidades por tipo de arreglo
2. Búsqueda de arreglos por rango de precio
3. Actualizar precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
=====================================""")
        opcion = leer_opcion()

        if opcion == 1:
            tipo = input("Ingrese el tipo de arreglo (por ejemplo: ramo, caja o centro): ").lower()
            unidades_tipo(tipo)
        elif opcion == 2:
            try:
                p_min=int(input("Ingrese el precio minimo de su busqueda: "))
                p_max=int(input("Ingrese el valor maximo de lo que busca: "))
            except ValueError:
                print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max)
        elif opcion == 3:
            print(bodega)
            codigo = input("Ingresa el codigo del arreglo: ")
            buscar_codigo(codigo)
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            actualizar_precio(codigo, nuevo_precio)
        elif opcion == 4:
            print("4")
        elif opcion == 5:
            print("5")
        elif opcion == 6:
            print("Programa finalizado.")
            break
    else:
        print("Dato ingresado invalido. Debe seleccionar una opcion del 1 al 6.")


main()