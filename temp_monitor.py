# temp_monitor.py
# Libreria de funciones para registrar lecturas de temperatura.
#
# Estructura del diccionario (monitor):
#   - 'max':      numero maximo de lecturas permitidas (int)
#   - 'readings': lista con las temperaturas de cada lectura (list)
#   - 'total':    suma total de todas las temperaturas (float)


def init(max_readings):
    """
    Crea y retorna un diccionario para almacenar hasta max_readings lecturas.
    """
    lecturas ={}
    lecturas ['max'] = max_readings
    lecturas ['readings'] = []  
    lecturas ['total'] = 0.0
    return lecturas 
    # TODO: Implementar
    pass


def add_reading(monitor, temp):
    """
    Agrega una nueva lectura con la temperatura especificada.
    Retorna el diccionario modificado.
    """

    lecturas = monitor ['readings']
    if len(lecturas) < monitor ['max']:
        lecturas.append(temp)
        monitor ['total'] += temp
    return monitor
    # TODO: Implementar
    pass


def count(monitor):
    """
    Retorna el numero de lecturas agregadas.
    """
    return len(monitor['readings'])
    # TODO: Implementar
    pass


def average_temp(monitor):
    """
    Retorna la temperatura promedio de todas las lecturas.
    """
    return monitor ['total'] // len(monitor['readings']) 

    # TODO: Implementar
    pass


def format_readings(monitor):
    """
    Retorna una representacion en cadena de las temperaturas.
    Formato: [t1, t2, t3, ..., tn]
    """
    temp = []
    for n in monitor ['readings']:
        temp.append(n)
        return (temp)
    
    # TODO: Implementar
    pass


def highest_temp(monitor):
    """
    Retorna la temperatura mas alta de cualquier lectura.
    """
    for n in monitor ['readings']:
        return max(monitor ['readings'])
    # TODO: Implementar
    pass


def coldest_window(monitor, k):
    """
    Retorna el promedio mas bajo de cualquier k lecturas consecutivas.
    """
    for k in range (3):
        prom = sum(monitor ['readings'][k:k+3]) // 3
        return min(prom)
    
    # TODO: Implementar
    pass


def longest_rising_streak(monitor):
    """
    Retorna la longitud maxima de una secuencia de lecturas consecutivas
    donde las temperaturas aumentan estrictamente.
    """
    for n in monitor ['readings']:
        if monitor ['readings'][n] < monitor ['readings'][n+1]:
            return n
        else:
            return 0
            
    # TODO: Implementar
    pass

    
def main():
    # crear un monitor para temperaturas de Bogota (12 horas, 6am-5pm)
    monitor = init(12)
    monitor = add_reading(monitor, 8.0)   # 6am
    monitor = add_reading(monitor, 9.5)   # 7am
    monitor = add_reading(monitor, 11.0)  # 8am
    monitor = add_reading(monitor, 13.5)  # 9am
    monitor = add_reading(monitor, 15.0)  # 10am
    monitor = add_reading(monitor, 17.5)  # 11am
    monitor = add_reading(monitor, 19.0)  # 12pm
    monitor = add_reading(monitor, 20.0)  # 1pm
    monitor = add_reading(monitor, 19.5)  # 2pm
    monitor = add_reading(monitor, 18.0)  # 3pm
    monitor = add_reading(monitor, 16.5)  # 4pm
    monitor = add_reading(monitor, 15.0)  # 5pm

    # imprimir estadisticas
    print("numero de lecturas =", count(monitor))               # 12
    print("temp promedio =", average_temp(monitor))             # 15.208...
    print("temp mas alta =", highest_temp(monitor))             # 20.0
    print("ventana mas fria (3) =", coldest_window(monitor, 3)) # 9.5
    print("racha creciente =", longest_rising_streak(monitor))  # 8

    # imprimir temperaturas
    print(format_readings(monitor))


if __name__ == "__main__":
    main()
