#!/bin/bash
echo "Compilando tp05.cpp..."
g++ tp05.cpp -l pthread -o bin/tp.out
echo "Executando tp05.cpp..."
./bin/tp.out