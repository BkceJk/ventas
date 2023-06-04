# Definir los precios de los productos
menu = {
    "Hamburguesa": 4600,
    "Papas fritas": 2000,
    "Refresco": 1000,
    "Helado": 2500
}

# Definir las promociones disponibles
promociones = {
    "menu1": {
        "items": ["Hamburguesa", "Papas fritas", "Refresco"],
        "descuento": 10
    },
    "menu2": {
        "items": ["Hamburguesa", "Papas fritas", "Helado"],
        "descuento": 15
    },
    "menu3": {
        "items": ["Hamburguesa", "Refresco", "Helado"],
        "descuento": 20
    }
}

def calcular_total(orden):
    total = 0
    for item in orden:
        if item in menu:
            total += menu[item]
        else:
            print(f"No se reconoce el producto '{item}'.")
    return total

def aplicar_descuento(total, promocion):
    if promocion in promociones:
        descuento = promociones[promocion]["descuento"]
        total -= total * (descuento / 100)
        print(f"Descuento aplicado: {descuento}%")
    else:
        print("La promoción ingresada no existe.")
    return total

# Ejemplo de uso
orden = ["Hamburguesa", "Refresco"]
total = calcular_total(orden)

def solicitar_metodo_pago():
    print("Métodos de pago disponibles:")
    print("1. Tarjeta de débito")
    print("2. Tarjeta de crédito")
    print("3. Efectivo")
    opcion = input("Seleccione un método de pago (1-3): ")

    if opcion == "1":
        return "Tarjeta de débito", "Inserte su tarjeta de débito."
    elif opcion == "2":
        return "Tarjeta de crédito", "Inserte su tarjeta de crédito."
    elif opcion == "3":
        return "Efectivo", "Tenga el monto exacto de efectivo listo."
    else:
        print("Opción inválida. Intenta nuevamente.")
        return solicitar_metodo_pago()

metodo_pago, indicacion = solicitar_metodo_pago()

print("Indicación:", indicacion)
print("Se ordenó:", ", ".join(orden))
print("El total es:", total)
print("Método de pago:", metodo_pago)
print("Gracias por su compra, vuelva pronto")