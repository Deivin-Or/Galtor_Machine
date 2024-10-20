from tqdm import tqdm
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# Función para simular la máquina de Galton usando tanto numpy como random

def balls_simulator(num_canicas, num_niveles, delay=0.0001):
    results = []
    
    start_time = time.time()  # Iniciamos el cronómetro
    
    # Simulamos las canicas, usando tqdm para mostrar una barra de progreso
    for _ in tqdm(range(num_canicas), desc="Simulando canicas"):
        decitions = np.zeros(num_niveles)
        # Usamos random para decidir si la canica va a la izquierda (-1) o derecha (+1)
        for i in range(num_niveles):
            decitions[i] = random.choice([-1, 1])
        # Sumamos todas las decisiones para determinar la posición final
        final_position = np.sum(decitions)
        results.append(final_position)
        
        # Hacemos una pausa para que la simulación sea más lenta
        time.sleep(delay)
    
    # Mostramos el tiempo total que ha transcurrido
    tiempo_total = time.time() - start_time
    print(f"\nSimulación completada en {tiempo_total:.2f} segundos.")
    
    return results

# Función para graficar el histograma
def galthos_grafic(resultados, num_contenedores):
    plt.hist(resultados, bins=num_contenedores, edgecolor='black')
    plt.title('Máquina de Galtor \n(Simulación Aproximada de resultados)')
    plt.xlabel('Barras')
    plt.ylabel('Número de Canicas')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000  # Número de canicas
num_niveles = 12    # Niveles de obstáculos (o decisiones)
num_contenedores = num_niveles + 1  # El número de contenedores será niveles + 1

# Simulamos los resultados usando una mezcla de numpy y random
resultados = balls_simulator(num_canicas, num_niveles)

# Graficamos los resultados
galthos_grafic(resultados, num_contenedores)
