# import openpyxl
# from openpyxl.styles import Font
import random
import csv
import os

def cartas():
    carta_al_azar = random.choice(listbaraja)
    print(f"*{carta_al_azar}*")
    listbaraja.remove(carta_al_azar)
    barajas_elegidas.append(carta_al_azar)
    print(f"El número de cartas restantes es: {len(listbaraja)}")

def resumen_cartas():
    print("\nResumen del juego")
    for carta in barajas_elegidas:
        print(f"**{carta}**")

def reanudar_partida():
    while True:
        reanudar=input("Deseas reanudar la partida?? (S/N)").upper()
        if reanudar == "S":
            cartas()
        elif reanudar== "N":
            ganador = input("Ingrese el nombre del ganador: ")
            lstGanadores.append(ganador)
            listagrande_elegidas.append(barajas_elegidas)
            for agregar_D_nuevo_a_baraja in barajas_elegidas:
                listbaraja.append(agregar_D_nuevo_a_baraja)
            break
        else:
            print("La opcion no es valida, introduce una opcion valida")
            continue

def menu():
    print("\n--LOTERÍA MEXICANA--\n")
    print("Menú de opciones")
    print("1. Iniciar partida")
    print("2. Resumen de partidas")
    print("3. Salir del juego")



listbaraja = ["El gallo", "El diablo", "La dama", "El catrín", "El paraguas",
              "La sirena", "La escalera", "La botella", "El barril", "El árbol",
              "El melón", "El valiente", "El gorrito", "La muerte", "La pera",
              "La bandera", "El bandolón", "El violoncello", "La garza", "El pájaro",
              "La mano", "La bota", "La luna", "El cotorro", "El borracho", "El negrito",
              "El corazón", "La sandía", "El tambor", "El camarón", "Las jaras",
              "El músico", "La araña", "El soldado", "La estrella", "El cazo", "El mundo",
              "El apache", "El nopal", "El alacrán", "La rosa", "La calavera", "La campana",
              "El cantadito", "El venado", "El sol", "La corona", "La chalupa", "El pino",
              "El pescado", "La palma", "La maceta", "El arpa", "La rana"]
lista_c_2_listas={}
listagrande_elegidas = []
lstGanadores = []


print(''' 
 _       _   _               
| |     | | | |                 
| | ___ | |_| |_ ___ _ __ _   _ 
| |/ _ \| __| __/ _ \ '__| | | |
| | (_) | |_| ||  __/ |  | |_| |
|_|\___/ \__|\__\___|_|   \__, |
                           __/ |
                          |___/ ''')

archivo_barajas = r"C:\Users\jahaz\OneDrive\Documentos\ejercicios visual\Loteria.csv"

while True:  # Menú principal
    barajas_elegidas = []
    break