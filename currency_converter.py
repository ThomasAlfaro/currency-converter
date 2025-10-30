"""
Conversor simple de divisas utilizando API.
Autor: Thomas Alfaro
Descripción del proyecto: Este programa permite convertir un monto entre distintas monedas,
obteniendo las tasas actualizadas desde una API externa.
"""

import requests

API_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies"
DESTINOS = ['usd', 'eur', 'ars', 'mxn', 'jpy', 'gbp']

def monto_valido(monto):
    """
    Verifica si el monto ingresado por el usuario es válido y mayor a 0.
    Devuelve True en caso de ser así o False en caso de no serlo.
    """
    validez = True
    if type(monto) == int or type(monto) == float:
        if monto<=0:
            print("El monto debe ser mayor a 0.")
            validez = False
    else:
        print("El valor ingresado no es numérico. Por favor intentelo de nuevo.")
        validez = False
    return validez

def divisa_valido(divisa_origen):
    """
    Verifica si la divisa ingresada es válida. 
    Comprueba si tiene tres letras y esta en la lista de DESTINOS.
    Devuelve True en caso de ser asi, o False en caso contrario.
    """
    divisa_origen = divisa_origen.strip().lower()
    validez = True
    if len(divisa_origen) != 3:
        print("Error: El tipo de divisa no es valido.")
        validez = False
    elif divisa_origen not in DESTINOS:
        print("Error: La divisa ingresada no está en la base de datos.")
        validez = False
    return validez

def obtener_datos(divisa_origen):
    """
    Obtiene los datos de las divisas desde la API y devuelve un diccionario
    con las tasas de conversión de cada una.
    """
    datos = None
    url = f"{API_URL}/{divisa_origen.lower()}.json"
    response = requests.get(url)
    if response.status_code == 200:
        try: 
            data = response.json()
            if divisa_origen.lower() in data:
                datos = data[divisa_origen.lower()]
        except Exception:
            print("Error al cargar la API")
    else:
        print("No se pudo conectar con la API.")
    return datos

def convertir_y_mostrar(monto, divisa_origen, divisas):
    """
    Imprime por pantalla la lista con las divisas y sus respectivas conversiones.
    """
    resultado = []
    for destino in DESTINOS:
        if destino in divisas:
            tasa = divisas[destino]
            convertido = monto * tasa
            resultado.append((destino.upper(), tasa, convertido))

    print(f"\nConversión de {monto:,.8f} {divisa_origen}")
    print(" (tasas actualizadas diariamente desde Github)")
    print("-"*52)
    print(f"{'Moneda':<8} {'Tasa':>12} {'Monto':>16}")
    print("-"*52)

    for moneda, tasa, monto_convertido in resultado:
        print(f"{moneda:<8} {tasa:>12.4f} {monto_convertido:>16,.2f}")

    print("-"*52)

def main():
    """
    Función principal del programa.
    Solicita al usuario un monto y una divisa, valida los datos ingresados,
    obtiene las tasas de conversión desde la API y muestra los resultados.
    """
    monto = 0.0
    monto_usuario = False
    divisa_usuario = False
    ingreso_divisa = ""
    divisas = None
    

    while not monto_usuario:
        ingreso_monto = input("Ingrese el monto: ").strip()
        try:
            monto = float(ingreso_monto)
            if monto_valido(monto) == True:
                monto_usuario = True
        except ValueError:
            print("Error: El monto ingresado no es valido.")

    
    while not divisa_usuario:
        ingreso_divisa = input("Ingrese divisa: ").strip()
        if divisa_valido(ingreso_divisa) == True:
            divisa_usuario = True
        
    
    if  monto_usuario == True and divisa_usuario == True:
        divisas = obtener_datos(ingreso_divisa)
        convertir_y_mostrar(monto, ingreso_divisa, divisas)

if __name__ == "__main__":
    main()