#!/bin/bash
echo "Compilando tp05.cpp..."
rm -f bin/tp.out
g++ tp05.cpp -l pthread -o bin/tp.out