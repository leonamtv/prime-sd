#include <pthread.h>
#include <iostream>
#include <chrono>

#define NUM_THREADS 4
#define TEMPO_EXEC_SEG 30

void * calcula_primos ( void * args  );
int main ( );

typedef struct {
    int min;
    int max;
} argumento;

pthread_mutex_t mutex;
unsigned long max = 1048576;

void * calcula_primos ( void * args ) {
    argumento * arg = ( argumento * ) args;
    int aux = arg->min;
    while ( aux <= arg->max ) {
        int div = aux - 1;
        int divisors = 0;
        while ( div > 1 ) {
            if ( aux % div == 0 && div > 1 ) {
                ++divisors;
	    }
            --div;
        }
        if ( divisors == 0 ) {
            pthread_mutex_lock( &mutex );
            std::cout << aux << std::endl;
            pthread_mutex_unlock( &mutex );
        }
        ++aux;
    }
    free(args);
    pthread_exit ( NULL );
    return 0;
}

int main () {
    pthread_t* id_control_threads = ( pthread_t * ) malloc ( sizeof ( pthread_t* ) * NUM_THREADS );
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    for ( int i = 0; i < NUM_THREADS; i++ ) {
        argumento *arg_paralelo;
        arg_paralelo      = ( argumento * ) malloc ( sizeof ( argumento ));
        arg_paralelo->min = i * (int) max / NUM_THREADS + 1;
        arg_paralelo->max = (i + 1) * (int) max / NUM_THREADS;
        if ( pthread_create ( &id_control_threads[i], NULL, calcula_primos, ( void * ) arg_paralelo )) {
            puts("Erro na criacao de threads.");
        }
    }
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    while ( std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() <= TEMPO_EXEC_SEG ) {
        end = std::chrono::steady_clock::now();
    }
    if ( std::chrono::duration_cast<std::chrono::seconds>(end - begin) >= std::chrono::seconds{TEMPO_EXEC_SEG} )
        return 0;
    for ( int i = 0; i < NUM_THREADS; i++ ) {
        if ( pthread_join ( id_control_threads[i], NULL )) {
            puts ( "Erro de sincronizacao das threads. " );
            return -1;
        }
    }
    return 0;
}
