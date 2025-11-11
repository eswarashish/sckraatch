import multiprocessing as mp
# gil i.e global interpretation lock makes one interpretter to only excute one thread at same time
# hence multiprocessing makes to unclock multiple interpretters with each single thread
# modern computers have multiple cores and a core can execute multiple threads
# parallelisation can be done using multiprocessing  or 
# multithreading ,, a process can hae multiple threads having shared resources, shhared memory space, executes concurerently
# so a single resource requiremnt for two threads can occur hence we use locks for thread synchronisaton
# so to gil makes only one thread to execute -> so no multithreading/ killing concurrency in threads
# one instruction at a time
# effects cpu-bound threads 

import time
import math
results_a = []

results_b = []

results_c = []

def make_calc_1(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number**3))

def make_calc_2(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number**4))

def make_calc_3(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number**5))

# without mp

# if __name__ =='__main__':
#     number_list = list(range(5000000))

#     start = time.time()
#     make_calc_1(numbers=number_list)
#     make_calc_2(numbers=number_list)
#     make_calc_3(numbers=number_list)
#     end = time.time()
#     print(end-start)

# with mp

if __name__ =='__main__':
    number_list = list(range(5000000))
    p1 = mp.Process(target=make_calc_1,args=(number_list,))# args is a tuple so comma in thhe (arg,)
    p2 = mp.Process(target=make_calc_2,args=(number_list,))# args is a tuple so comma in thhe (arg,)
    p3 = mp.Process(target=make_calc_3,args=(number_list,))# args is a tuple so comma in thhe (arg,)
    

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(end-start)