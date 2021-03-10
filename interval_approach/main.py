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

thread_a = Thread( target = check_rand, args = ( 'A', 0, int ( max / 4 )))
thread_b = Thread( target = check_rand, args = ( 'B', int ( max / 4 ), int ( 2 * max / 4 )))
thread_c = Thread( target = check_rand, args = ( 'C', int ( 2 * max / 4 ), int ( 3 * max / 4 )))
thread_d = Thread( target = check_rand, args = ( 'D', int ( 3 * max / 4 ), max ) )

thread_a.start()
thread_b.start()
thread_c.start()
thread_d.start()

now = time()
after = time()
while ( after - now ) % 3600 < 30 :
    after = time()
_exit(1)
