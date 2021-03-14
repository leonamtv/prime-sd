#!/usr/bin/env python3

import os
import json

output_path = './output'

latest = max([ os.path.join( output_path, d ) for d in os.listdir('./output') if os.path.isdir ( os.path.join( output_path, d ))], key=os.path.getmtime )

path_to_index_file = os.path.join ( latest, 'index.json')
tempo_total_sec = 0

data = {}


with open ( path_to_index_file, 'r' ) as json_file :
    data = json.load ( json_file )

csv_dump = 'index,tipo,tentativa,tempo,threads,num_primes\n'
csv_index = 0

for entry in data :
    for item in data[entry] :
        tempo_total_sec += item['tempo']
        csv_dump += f"{str(csv_index)},\"{entry}\",{str(item['tentativa'])},{str(item['tempo'])},{ 0 if entry == 'sequential' else item['threads'] },{str ( item ['num_primes'] )}\n"
        csv_index += 1

csv_file = open ( 'data/organized_data.csv', 'w' )
csv_file.write(csv_dump)
csv_file.close()

print(f'> Tempo total {tempo_total_sec}s')