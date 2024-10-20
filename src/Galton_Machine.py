# Nota tqdm solo lo usaré para darle una barra de carga y time para determinar el tiempo que queremos que tarde la carga
from tqdm import tqdm
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# Definión de función para simular la máquina de Galton
# Se utiuliza utilizaran los parametros de cantidad de canicas (bolitas, pelotas), los niveles(cantidada de deciones que tomará) 
# y un extra de tiempo (esto para darle una vista extra de una barra de carga)
#cada bolita llevará un retardó de 0.0001 segundos
def balls_simulator(balls_number, nivel_number, delay=0.0001):
    results = [] # Contendrá los resultados de las deciones de las bolitas
    
    start_time = time.time()  # Variable del crónometro, aui iniaria el conteo de tiempo de la barra de carga

    # Simulamos las bolitas en la barra de carga usando tqdm
    # La funcion de carga puede ser modificada y eliminada si es nceseario 
    for _ in tqdm(range(balls_number), desc = "Calculadno Resultado, epere un momento porfavor :v......"):
        decisions = np.zeros(nivel_number)

        # Inicio de proceso de decisiones para saber en cual barra (Celda) caerá la bolita
        # Usamos random para decidir si la bolita va a la izquierda (-1) o derecha (+1)
        for ball in range(nivel_number):
            decisions[ball] = random.choice([-1, 1])

        # Sumamos todas las decisiones para determinar la posición final
        final_position = np.sum(decisions)

        # Agregamos a la lista popr medio de app.end 
        results.append(final_position)
        
        # Hacemos una pausa para que la simulación sea más lenta
        # Esta determinado por delay, si quiere cambiar el tiempo de espera necesita ir a la definion de balls_simulator
        # y modificar el parametro de delay, recuerde que cada entero equivale a un 1 segundo
        time.sleep(delay)
    
    # Mostramos el tiempo total que ha transcurrido
    tiempo_total = time.time() - start_time
    print(f"\nSimulación completada en {tiempo_total:.2f} segundos.")
    
    # resultado final
    return results

# Defición de función para graficar los resultados
def galton_grafic(results, number_cells):
    # Configuramos el tamaño del gráfico y el fondo oscuro
    plt.figure(figsize=(10, 6), facecolor='#2E2E2E')  # Fondo de toda la figura
    
    # Graficamos con barras en gris oscuro y bordes blancos
    plt.hist(results, bins=number_cells, edgecolor='white', color='#4F4F4F')
    
    # Cambiamos el color de fondo de la gráfica
    plt.gca().set_facecolor('#1C1C1C')  # Fondo del área de la gráfica
    
    # Personalizamos el título y las etiquetas con colores claros
    plt.title('Máquina de Galton - Resultados', fontsize=16, fontweight='bold', color='white')
    plt.xlabel('Contenedores', fontsize=12, color='white')
    plt.ylabel('Número de Bolitas', fontsize=12, color='white')
    
    # Cambiamos el color de los ejes y los valores de las etiquetas
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')
    
    # Cambiamos el color de las líneas de los ejes para que combinen con el fondo oscuro
    plt.gca().spines['bottom'].set_color('white')
    plt.gca().spines['left'].set_color('white')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['right'].set_color('none')
    
    # Mostramos la gráfica con el estilo elegante y moderno
    plt.show()

# Parámetros que se utilizarán para la simulación
balls_number = 3000  # Número de canicas
nivel_number = 12    # Niveles de obstáculos (o decisiones)
cells_number = nivel_number+ 1  # El número de contenedores será niveles + 1

# Simulamos los resultados usando una mezcla de numpy y random
final_results = balls_simulator(balls_number, nivel_number)

# Graficamos los resultados
galton_grafic(final_results, cells_number)
