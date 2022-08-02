import math
import random
import time
import multiprocessing as mp

# función secuencial
def approximate_pi_sec(num_samples):
    start = time.time()
    num_inside = 0
    for _ in range(num_samples): 
        x,y = random.uniform(-1, 1), random.uniform(-1, 1)
        if math.hypot(x, y) <= 1:
            num_inside += 1
    print("Finished in: {:.2f}s".format(time.time()-start))
    return "pi ~= {}".format((4*num_inside)/num_samples)

# approximate_pi_sec levemente modificada
def approximate_pi(num_samples):
    pass


# windows
if __name__ == '__main__':

    # enable support for multiprocessing
    mp.freeze_support()

    # función paralela
    def parallel_approximate_pi(num_samples, n_cpu):
        start = time.time()
        print("Finished in: {:.2f}s".format(time.time()-start))
    
    n_samples= 10000
    n_cpu = 8

    pi_value_sec = approximate_pi_sec(n_samples)


    pi_value_par = parallel_approximate_pi(n_samples,n_cpu)

    print(pi_value_sec,pi_value_par)