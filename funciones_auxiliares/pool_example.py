from multiprocessing import Pool, cpu_count
import time
import numpy as np

def random_square(seed):
    np.random.seed(seed)
    random_num = np.random.randint(0, 10)
    return random_num**2

if __name__ == '__main__':
    inicio = time.time()
    results = []
    for i in range(10000000): 
        results.append(random_square(i))
    final = time.time()
    print(f'Secuencial: Tiempo de ejecución {final - inicio} s')

    n_cpu = cpu_count() # se determina el número de CPU's disponibles para utilizar
    inicio = time.time()
    results_p = []
    with Pool(processes=n_cpu) as p:
        results_p.append(p.map(random_square, range(10000000)))
    final = time.time()
    print(f'Paralelo: Tiempo de ejecución {final - inicio} s')