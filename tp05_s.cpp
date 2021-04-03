#include <iostream>
#include <chrono>
#include <cmath>

unsigned long long int control = 1;
unsigned long long number_of_primes = 0;
int primes[50000000];

int tempo_exec_sec = 40;

void verifica_primo ();
int main (int argc, char* argv[]);

void verifica_primo ( ) {
    control ++;
    int aux = control, div = (int) sqrt( aux ), divisors = 0;
    while ( div > 1 ) {
        if ( aux % div == 0 && div > 1 ) 
            ++divisors;
        div--;
    }
    if ( divisors == 0 ) {
        primes[number_of_primes] = aux;
        number_of_primes ++;
    }
}

int main (int argc, char* argv[] ) {
    
    switch ( argc ) {
        case 1:
            break;
        case 2:
            tempo_exec_sec = std::atoi ( argv[1] );
            break;
    }

    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    while ( std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() <= tempo_exec_sec ) {
        verifica_primo();
        end = std::chrono::steady_clock::now();
    }
    if ( std::chrono::duration_cast<std::chrono::seconds>(end - begin) >= std::chrono::seconds{tempo_exec_sec} ) {
        std::cout << number_of_primes << std::endl;
        return 0;
    }
    return 0;
}
