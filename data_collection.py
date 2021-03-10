#!/usr/bin/env python3

import os
import json
import subprocess
from datetime import datetime

tentativas = 10
tempos = [ 1, 2, 5, 10, 20, 30, 40, 50, 60, 80 ]
threads = [ 2, 4, 8 ]

now = datetime.now()

output_path = f"./output/exec_{now.day}_{now.month}_{now.year}_{now.hour}_{now.minute}"

data = {
    "sequential" : [],
    "parallel" : []
}

for i in range ( tentativas ) :
    print(f"Colheita de dados sequenciais {i + 1}")
    for tempo in tempos  :
        print(f"> Executando sequencial por {str(tempo)} segundo(s) ")
        process = subprocess.Popen ( f'./bin/tps.out { tempo }', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        response = process.stdout.readlines()
        response = [ entry.decode('utf-8') for entry in response ]
        file_dump = ''
        for entry in response :
            file_dump += entry
        if not os.path.isdir ( output_path ) :
            os.makedirs ( output_path )
        file_name = os.path.join ( output_path, f"output_{str(tempo)}s_{str(i+1)}_seq_cpp.txt" )
        output_file = open( file_name, 'w')
        output_file.write(file_dump)
        output_file.close()
        data['sequential'].append({
            "tentativa" : ( i + 1 ),
            "tempo" : tempo,
            "file"  : file_name
        })

for i in range ( tentativas ) :
    print(f"Colheita de dados paralelos {i + 1}")
    for tempo in tempos :
        for thread in threads :
            print(f"> Executando paralelo por {str(tempo)} segundo(s) com {str(thread)} threads")
            process = subprocess.Popen ( f'./bin/tp.out { thread } { tempo }', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            response = process.stdout.readlines()
            response = [ entry.decode('utf-8') for entry in response ]
            file_dump = ''
            for entry in response :
                file_dump += entry
            if not os.path.isdir ( output_path ) :
                os.makedirs ( output_path )
            file_name = os.path.join ( output_path, f"output_{str(tempo)}s_{str(thread)}th_{str(i+1)}_par_cpp.txt" )
            output_file = open( file_name, 'w')
            output_file.write(file_dump)
            output_file.close()
            data['parallel'].append({
                "tentativa" : ( i + 1 ),
                "tempo"   : tempo,
                "threads" : thread,
                "file"    : file_name
            })

with open(os.path.join( output_path, "index.json" ), 'w') as fp :
    json.dump ( data, fp )  
    print('Escrita de arquivo de index concluída.')


print('Colheita de dados concluída.')