#!/usr/bin/env python3

import os
import subprocess

tentativas = 10
tempos = [ 2, 5, 10, 20, 30, 40, 50, 60 ]
threads = [ 2, 4, 8 ]

output_path = './output/exec_10_03_2021'

for i in range ( tentativas ) :
    print(f"Colheita de dados sequenciais {i + 1}")
    for tempo in tempos  :
        print(f"> Executando sequencial por {str(tempo)} segundos ")
        process = subprocess.Popen ( f'./bin/tps.out { tempo }', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        response = process.stdout.readlines()
        response = [ entry.decode('utf-8') for entry in response ]
        file_dump = ''
        for entry in response :
            file_dump += entry
        if not os.path.isdir ( output_path ) :
            os.makedirs ( output_path )
        output_file = open( os.path.join ( output_path, f"output_{str(tempo)}s_{str(i+1)}_seq_cpp.txt" ), 'w')
        output_file.write(file_dump)
        output_file.close()

for i in range ( tentativas ) :
    print(f"Colheita de dados paralelos {i + 1}")
    for tempo in tempos :
        for thread in threads :
            print(f"> Executando paralelo por {str(tempo)} segundos com {str(thread)} threads")
            process = subprocess.Popen ( f'./bin/tp.out { thread } { tempo }', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            response = process.stdout.readlines()
            response = [ entry.decode('utf-8') for entry in response ]
            file_dump = ''
            for entry in response :
                file_dump += entry
            if not os.path.isdir ( output_path ) :
                os.makedirs ( output_path )
            output_file = open( os.path.join ( output_path, f"output_{str(tempo)}s_{str(thread)}th_{str(i+1)}_par_cpp.txt" ), 'w')
            output_file.write(file_dump)
            output_file.close()

print('Colheita de dados concluída')