#include <pthread.h>
#include <iostream>
#include <chrono>
#include <cmath>

unsigned long long int control = 2;
unsigned long long number_of_primes = 0;
int num_threads = 4, tempo_exec_sec = 40;

void * verifica_primo ( void * args  );
int main ( int argc, char* argv[] );

pthread_mutex_t mutex_a;
pthread_mutex_t mutex_b;

void * verifica_primo ( void * args ) {
    while ( true ) {
        int aux = control;
        pthread_mutex_lock( &mutex_b );
        control ++;
        pthread_mutex_unlock( &mutex_b );
        int div = (int) sqrt( aux );
        int divisors = 0;
        while ( div > 1 ) {
            if ( aux % div == 0 && div > 1 ) 
                ++divisors;
            div--;
        }
        if ( divisors == 0 ) {
            pthread_mutex_lock( &mutex_a );
            number_of_primes ++;
            pthread_mutex_unlock( &mutex_a );
        }
    }
    free(args);
    pthread_exit ( NULL );
    return 0;
}

int main ( int argc, char* argv[] ) {
    
    switch ( argc ) {
        case 1:
            break;
        case 2:
            num_threads = std::atoi ( argv[1] );
            break;
        case 3:
            num_threads = std::atoi ( argv[1] );
            tempo_exec_sec = std::atoi ( argv[2] );
            break;
    }

    pthread_t* id_control_threads = ( pthread_t * ) malloc ( sizeof ( pthread_t* ) * num_threads );
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    for ( int i = 0; i < num_threads; i++ ) {
        if ( pthread_create ( &id_control_threads[i], NULL, verifica_primo, NULL ))
            puts("Erro na criacao de threads.");
    }
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    while ( std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() <= tempo_exec_sec ) {
        end = std::chrono::steady_clock::now();
    }
    if ( std::chrono::duration_cast<std::chrono::seconds>(end - begin) >= std::chrono::seconds{tempo_exec_sec} ) {
        std::cout << number_of_primes << std::endl;
        return 0;
    }
    for ( int i = 0; i < num_threads; i++ ) {
        if ( pthread_join ( id_control_threads[i], NULL )) {
            puts ( "Erro de sincronizacao das threads. " );
            return -1;
        }
    }
    return 0;
}
