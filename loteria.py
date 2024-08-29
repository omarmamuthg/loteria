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

def reanudar_partida_pregunta():
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
def reanudar_partida_sin_pregunta():
    cartas()


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
    menu()
    select = input("Seleccione una opción: ")
    if select == "1":  # Iniciar partida
        cartas()
        while True:
            dar = input("¿Desea sacar otra carta? (S/N): ").upper()
            if dar =="S":
                cartas()
            elif dar =="N":
                resumen_cartas()
                while True:
                    reanudar=input("Deseas reanudar la partida?? (S/N): ").upper()
                    if reanudar == "S":
                        break
                    elif reanudar== "N":
                        resumen_cartas()
                        ganador = input("Ingrese el nombre del ganador: ")
                        lstGanadores.append(ganador)
                        listagrande_elegidas.append(barajas_elegidas)
                        for agregar_D_nuevo_a_baraja in barajas_elegidas:
                            listbaraja.append(agregar_D_nuevo_a_baraja)
                        lista_c_2_listas[ganador]=barajas_elegidas
                        break
                    else:
                        print("La opcion no es valida, introduce una opcion valida")
                        continue
                if reanudar =="S":
                    cartas()
                    continue
                #elif reanudar == "N":
                    #print(lista_c_2_listas)
                    #*****************************************************************************************************************************
                break
            else:
                print("La opcion ingresada no es valida.")
        # with open("Loteria.csv", "w", newline="") as archivo_barajas:
        #     escribir_archivo = csv.writer(archivo_barajas)
        #     escribir_archivo.writerow(("Ganadores", "Cartas de partida"))
        #     escribir_archivo.writerows([id,datos] for id,datos in lista_c_2_listas.items())
        #     #escribir_archivo.writerows([id for id in lista_c_2_listas,datos for datos in lista_c_2_listas.values()])



    elif select == "2":  # Resumen de partidas
        longitud=len(lstGanadores)
        for resumen in range(longitud):
            print(f"\n{resumen + 1}° PARTIDA")
            print(f"El Ganador: {lstGanadores[resumen]}\n")
            for resumen2 in listagrande_elegidas[resumen]:
                print(f"*{resumen2}*")
        # while True:
        #     import_excel=input("Exportar a excel? Si(S) | No(N) -> ").upper() 
            '''
            if import_excel == "S":
                if os.path.exists(archivo_barajas): 
                    with open("Hermanos.csv", "r", newline="") as archivo_barajas :
                        leer_datos= csv.reader(archivo_barajas)
                        next(leer_datos)
                        for clave in diccionario:
                            lista.append([str(clave), diccionario[clave][0], diccionario[clave][1], diccionario[clave][2]])
        for lector in leer_datos:
            diccionario[int(lector[0])]=(lector[1],lector[2],lector[3])
                else:
                    print("El archivo no existe!")
                    


            elif import_excel == "N":
                break
            else:
            print("Elige otra opcion !")
            '''
    elif select == "3":
        print("FIN DEL JUEGO, ESPERO Y TE HAYAS DIVERTIDO!!")
        break
    else:
        print("Ingrese una opción válida")
























