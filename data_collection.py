#!/usr/bin/env python3

import os
import json
import subprocess
from datetime import datetime, timedelta

tentativas = 10
tempos = [ 1, 2, 5, 10, 20, 30, 40, 50, 60, 80, 100, 120, 140 ]
threads = [ 2, 4, 8 ]

print('Calculando tempo total...')

tempo_total = tempo_paral = sum ( tempos )
tempo_seq = 0

tempo_paral *= len ( threads )
tempo_total = tempo_paral + tempo_seq
tempo_total *= tentativas

print(f'Tempo total: {tempo_total}s')

now = datetime.now()

delta = timedelta(seconds=tempo_total)
termino = now + delta

print(f'Irá acabar aproximadamente em {termino.day}/{termino.month}/{termino.year} às {termino.hour}:{termino.minute}:{termino.second}')

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
        data['sequential'].append({
            "tentativa" : ( i + 1 ),
            "tempo" : tempo,
            "num_primes"  : int(file_dump)
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
                file_dump += entry.rstrip('\n')
            data['parallel'].append({
                "tentativa" : ( i + 1 ),
                "tempo"   : tempo,
                "threads" : thread,
                "num_primes"  : int(file_dump)
            })

if not os.path.isdir ( output_path ) :
    os.makedirs ( output_path )

with open(os.path.join( output_path, "index.json" ), 'w') as fp :
    json.dump ( data, fp )  
    print('Escrita de arquivo de index concluída.')

now = datetime.now()
print(f'Colheita de dados concluída em {now.day}/{now.month}/{now.year} às {now.hour}:{now.minute}:{now.second}')