import requests
import json

def dish_fetch(num):
    # Conexión directa a la API usando el número ingresado
    url = requests.get (f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    
    plato = json.loads(url.content)
    return plato

def main():
    n = int(input("Ingrese el número del plato: "))
    resultado = dish_fetch(n)
    print(resultado)

if __name__ == "__main__":
    main()