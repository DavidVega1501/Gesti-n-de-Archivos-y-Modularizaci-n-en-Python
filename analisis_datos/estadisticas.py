# estadisticas.py
def media(datos):
    """Esta funcion calcula la media aritmetica de un lista con valores numericos

    Args:
        datos (Lista): Lista de numeros

    Returns:
        Float: Flotante de la media aritmetica
    """
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    """_summary_

    Args:
        datos (_type_): _description_

    Returns:
        _type_: _description_
    """
    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
        return datos_sorted[mid]