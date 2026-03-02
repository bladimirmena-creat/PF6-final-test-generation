import requests
import json

response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
platos = json.loads(response.content)

def dish_fetch(num):
   
    if 0 < num <= len(platos):
        p = platos[num - 1]  
        return {
            "id": num,  
            "name": p.get("name", "Desconocido"),
            "description": p.get("description", "Sin descripción"),
            "ingredients": p.get("ingredients", "Sin ingredientes")
        }
    else:
        
        return {"id": num, "name": "Plato no encontrado", "description": "", "ingredients": ""}


def main():
    print("Platos disponibles:")
    for i, p in enumerate(platos, start=1):
        print(f"{i}. {p.get('name', 'Desconocido')}")
    
    try:
        n = int(input("Ingrese número del plato: "))
        print(dish_fetch(n)) 
    except:
        print({"error": "Entrada inválida"})

if __name__ == "__main__":
    main()