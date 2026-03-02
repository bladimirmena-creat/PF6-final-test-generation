# main.py

def dish_fetch(num):
    # Lista interna de platos típicos
    platos = [
        {"name": "Bandeja Paisa",
         "description": "La bandeja paisa es el orgullo de la cocina paisa.",
         "ingredients": "Frijoles, arroz, carne, chicharrón, huevo, plátano, chorizo, arepa, aguacate."},
        {"name": "Ajiaco",
         "description": "Sopa típica con pollo, papa y maíz.",
         "ingredients": "Pollo, papa, maíz, crema, alcaparras."},
        {"name": "Arepas",
         "description": "Tortilla de maíz, con o sin queso.",
         "ingredients": "Harina de maíz, agua, sal, queso."},
        {"name": "Sancocho",
         "description": "Sopa con pollo, yuca, plátano y mazorca.",
         "ingredients": "Pollo, yuca, plátano, mazorca, papa."},
        {"name": "Empanadas",
         "description": "Frituras rellenas de carne y papa.",
         "ingredients": "Harina de maíz, carne, papa, ají."}
    ]

    # Validamos el número ingresado
    if 1 <= num <= len(platos):
        plato = platos[num - 1]
        return {
            "id": num,  # obligatorio para pasar los tests
            "name": plato["name"],
            "description": plato["description"],
            "ingredients": plato["ingredients"]
        }
    else:
        # Para números fuera del rango, igual devolvemos un diccionario válido
        return {"id": num, "name": "Plato no encontrado", "description": "", "ingredients": ""}

# Función opcional para interactuar con el usuario
def main():
    print("Menú de platos típicos:")
    for i, p in enumerate([
        "Bandeja Paisa", "Ajiaco", "Arepas", "Sancocho", "Empanadas"
    ], start=1):
        print(f"{i}. {p}")

    try:
        n = int(input("Ingrese el número del plato: "))
        print(dish_fetch(n))
    except:
        print({"error": "Entrada inválida"})

# Solo ejecuta main si se corre directamente
if __name__ == "__main__":
    main()