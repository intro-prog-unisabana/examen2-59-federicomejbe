# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    name  = input("Ingrese el nombre del archivo: ")
    # TODO: Abrir el archivo y leer el numero de lecturas n
    with open (name, 'r') as f:
        n = int(f.readline())
    # TODO: Crear el monitor usando temp_monitor.init(n)
    monitor = temp_monitor.init(n)
    # TODO: Leer las n temperaturas y agregarlas con temp_monitor.add_reading()
    with open (name, 'r') as f:
        f.readline()
        for _ in range(n):
            temp =float(f.readline())
            monitor = temp_monitor.add_reading(monitor, temp)
    # TODO: Imprimir la racha creciente mas larga
    #       usando temp_monitor.longest_rising_streak()
    print("Racha mas creciente mas larga: ", )
    print("Racha creciente mas larga:", temp_monitor.longest_rising_streak(monitor))
    pass


if __name__ == "__main__":
    main()
