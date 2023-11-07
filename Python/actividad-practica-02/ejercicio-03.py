"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa 
que le indique al cajero el cambio que debe entregarle al cliente. Para eso 
se ingresan dos números enteros, correspondientes al total de la compra y al 
dinero recibido. Informar cuántos billetes de cada denominación deben ser 
entregados al cliente como vuelto, de tal forma que se minimice la cantidad 
de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, 
$5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. 
Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 
1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 
billetes de $1.

"""


def print_title(text: str, underline_char: str = "*"):
    """
    Imprime un título con una línea subrayada.

    Parameters:
    text (str): El texto del título.
    underline_char (str): El carácter utilizado para subrayar el título.
    """
    print(f"{text}\n{underline_char * (len(text) + 1)}")


def get_change(total_shop: int, total_paid: int):
    """
    Calcula el cambio necesario basándose en el total de la compra y
    la cantidad pagada, utilizando billetes de distintas denominaciones.

    Parameters:
    total_shop (int): El total de la compra.
    total_paid (int): La cantidad pagada por el cliente.

    Returns:
    dict: Un diccionario que indica cuántos billetes de cada denominación
          se deben devolver como cambio.
    """
    bill_denominations = [500, 100, 50, 20, 10, 5, 1]
    bills = {bill: 0 for bill in bill_denominations}

    change = total_paid - total_shop  # Calcula el cambio necesario
    if change < 0:
        # Elige lanzar un error si el dinero pagado es menor que el total de la compra
        raise ValueError(
            "El dinero entregado no es suficiente para cubrir el total de la compra.")

    for bill in bill_denominations:
        # Usa la función divmod para calcular el número de billetes de esta
        # denominación que se necesitan y cuánto cambio queda
        bills[bill], change = divmod(change, bill)

    return bills


def show_change_to_give(change: dict):
    """
    Imprime el cambio que se debe devolver basándose en un diccionario de billetes.

    Parameters:
    change (dict): Un diccionario que indica cuántos billetes de cada denominación
                   se deben devolver como cambio.
    """
    total = 0
    message = ""
    to_give = ""

    for key, value in change.items():
        if change[key] == 0:  # Ignora las denominaciones de billetes que no se deben devolver
            continue
        total += value * key  # Aumenta el total del cambio
        # Añade la información a la cadena que se imprimirá
        to_give += f"\n    {value} billete de {key}"

    if total == 0:
        # Imprime un mensaje si no existe cambio que devolver
        print("\nNo hay que devolver nada.")
        return

    # Inicia el mensaje a imprimir
    message = f"\nCambio a entregar ($ {total}): "
    message += to_give  # Añade el detalle del cambio
    print(message)


# Parte de ejecución del programa
print_title("Clean Caja")
total_shop = int(input("\nTotal de la compra: "))
total_paid = int(input("Total abonado: "))

# Calcula y muestra el cambio
money_to_return = get_change(total_shop, total_paid)
show_change_to_give(money_to_return)
