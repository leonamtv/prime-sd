#include <iostream>
#include <chrono>

unsigned long long int control = 0;
int tempo_exec_sec = 40;

void verifica_primo ();
int main (int argc, char* argv[]);

void verifica_primo ( ) {
    control ++;
    int aux = control, div = aux - 1, divisors = 0;
    while ( div > 1 ) {
        if ( aux % div == 0 && div > 1 ) 
            ++divisors;
        div--;
    }
    if ( divisors == 0 )
        std::cout << aux << std::endl;
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
    if ( std::chrono::duration_cast<std::chrono::seconds>(end - begin) >= std::chrono::seconds{tempo_exec_sec} )
        return 0;
    return 0;
}
