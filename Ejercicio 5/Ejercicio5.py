def es_bisiesto(year):
    """
    Función que recibe un año y devuelve True si es bisiesto y False si no lo es.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# Ejemplo de uso
year = 2023
if es_bisiesto(year):
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")

