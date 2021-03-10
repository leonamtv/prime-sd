#include <iostream>
#include <chrono>

#define TEMPO_EXEC_SEG 40

unsigned long long int control = 0;

void verifica_primo ();
int main ();

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

int main () {
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    while ( std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() <= TEMPO_EXEC_SEG ) {
        verifica_primo();
        end = std::chrono::steady_clock::now();
    }
    if ( std::chrono::duration_cast<std::chrono::seconds>(end - begin) >= std::chrono::seconds{TEMPO_EXEC_SEG} )
        return 0;
    return 0;
}
