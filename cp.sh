#!/bin/bash
echo "Compilando tp05.cpp..."
rm bin/tp.out
g++ tp05.cpp -l pthread -o bin/tp.out