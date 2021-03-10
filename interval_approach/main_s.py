from os import _exit
from time import time
from threading import Thread, Lock

lock = Lock()

max=1048576

def check_rand ( nome, min, max ) :
    aux = min
    while aux <= max :
        div = aux - 1
        divisors = 0
        while div > 1 :
            if aux % div == 0 and div not in ( 0, 1 ) :
                divisors += 1
            div -= 1
        if divisors == 0 :
            lock.acquire()
            print(aux)
            lock.release()
        aux += 1

thread_a = Thread( target = check_rand, args = ( 'A', 0, int ( max )))

thread_a.start()

now = time()
after = time()
while ( after - now ) % 3600 < 30 :
    after = time()
_exit(1)
