# Geração de primos

Esse repositório contém o código para um trabalho da disciplina de Sistemas Distribuídos no CEFET-MG Timóteo. O código aqui presente, gera números primos indefinidamente (respeitando os limites do tamanho das variáveis) por **N** segundos de duas formas diferentes: uma abordagem sequencial e outra concorrente.

A geração concorrente acontece da seguinte forma:

1. Uma variável inteira armazena um número inicial.
2. Cada thread incrementa esse valor e verifica se o valor incrementado é primo (utilizando **mutex** para travar as partes críticas). Cada uma das threads executam um loop infinito.
3. Se o número for primo, uma variável de contagem de números primos é incrementada, também utilizando um **mutex** para garantir a consistência. Um segundo objeto **mutex** é utilizado para que não haja travamentos desnecessários nas outras threads que estejam utilizando um **lock** com o primeiro **mutex**. Nossos experimentos mostraram que dois **mutexes** permitem gerar mais primos do que apenas um.
4. Esse processo é executado por **N** segundos.
5. No final, a variável de contagem de primos é impressa no **stdout**.

A geração concorrente acontece da seguinte forma:

1. Uma variável inteira armazena um número inicial.
2. Enquanto **N** segundos não se passarem, incrementamos o valor e verificamos se este é primo.
3. Se o número for primo, uma variável de contagem de números primos é incrementada.
4. No final, a variável de contagem de primos é impressa no **stdout**.

## Estratégia de análise de desempenho

* Gerar números primos sequencialmente por 5, 10, 20, 30, 40, 50, 60, 80, 100, 120 e 140 segundos, testando 10 vezes cada um dos tempos para que possamos tirar a média dos valores obtidos e diminuir a incerteza.
* Gerar números primos concorrentemente por 5, 10, 20, 30, 40, 50, 60, 80, 100, 120 e 140 segundos com 2, 4 e 8 threads, testando 10 vezes cada um dos tempos para que possamos tirar a média dos valores obtidos e diminuir a incerteza.
* Plotar tudo em um gráfico e analisar.

## Coleta, preparação e visualização dos dados

Dois scripts foram feitos para isso: `data_collection.py` e `data_prep.py`.

### Coleta de dados

O script `data_collection.py` executa o software sequencial e paralelo várias vezes, com várias threads, por vários tempos pré definidos, armazena as saídas e salva em um arquivo json.

A configuração da execução está no trecho abaixo do arquivo [data_collection.py](https://github.com/leonamtv/prime-sd/blob/master/data_collection.py):

```python
tentativas = 10
tempos = [ 1, 2, 5, 10, 20, 30, 40, 50, 60, 80, 100, 120, 140 ]
threads = [ 2, 4, 8 ]
```

No caso acima, o script irá executar o software sequencial por 1, 2, 5, 10, 20, 30, 40, 50, 60, 80, 100, 120 e 140 segundos, por 10 vezes cada e o software sequencial por 1, 2, 5, 10, 20, 30, 40, 50, 60, 80, 100, 120 e 140 segundos, por 10 vezes cada, com 2, 4 e 8 threads. O json é gerado no formato abaixo:

```json
{
    "sequential": [
        ...
        {
            "tentativa": 10,
            "tempo": 100,
            "num_primes": 809283
        },
        {
            "tentativa": 10,
            "tempo": 120,
            "num_primes": 912152
        },
        {
            "tentativa": 10,
            "tempo": 140,
            "num_primes": 1004348
        }
    ],
    "parallel": [
        {
            "tentativa": 1,
            "tempo": 1,
            "threads": 2,
            "num_primes": 90355
        },
        {
            "tentativa": 1,
            "tempo": 1,
            "threads": 4,
            "num_primes": 100800
        },
        {
            "tentativa": 1,
            "tempo": 1,
            "threads": 8,
            "num_primes": 105833
        },
        ...
    ]
}
```

Esse json é armazenado em uma pasta chamada `output/exec_<dia>_<mes>_<ano>_<hora>_<minuto>` com o nome `index.json`.

### Preparação dos dados

O script `data_prep.py` verifica qual a pasta mais recente contida na pasta `output` lê e faz parsing do `index.json` contido nesta, e gera um **csv** com os dados estruturados, prontos para serem plotados. O arquivo gerado é armazenado na pasta `data` com o nome `organized_data.csv`. Os dados ficam aproximadamente nesse formato:

```csv
index,tipo,tentativa,tempo,threads,num_primes
0,"sequential",1,1,0,69836
1,"sequential",1,2,0,89857
2,"sequential",1,5,0,138798
3,"sequential",1,10,0,202830
4,"sequential",1,20,0,303747
5,"sequential",1,30,0,388620
6,"sequential",1,40,0,462671
7,"sequential",1,50,0,530729
8,"sequential",1,60,0,593656
9,"sequential",1,80,0,708913,
...
130,"parallel",1,1,2,90355
131,"parallel",1,1,4,100800
132,"parallel",1,1,8,105833
133,"parallel",1,2,2,116530
134,"parallel",1,2,4,131092
135,"parallel",1,2,8,131589
136,"parallel",1,5,2,172604
137,"parallel",1,5,4,190863
138,"parallel",1,5,8,199855
139,"parallel",1,10,2,251952
140,"parallel",1,10,4,275260
141,"parallel",1,10,8,290153
142,"parallel",1,20,2,378487
143,"parallel",1,20,4,416030
...
```

### Visualização

Utilizamos um **jupyter notebook** para visualizar os dados. Resolvemos ignorar o arquivo propositalmente, pois este era muito grande. Para guardar a referência ao código utilizado para visualização, exportamos o conteúdo do **notebook** para um arquivo **python** [neste link](https://github.com/leonamtv/prime-sd/blob/master/jupyter/aggregate_and_plot.py).

Esse **notebook** lê o conteúdo do arquivo **csv** gerado no passo anterior para um **pandas dataframe**, ordena os dados e agrupa os dados. Agrupamos as amostras por tentativa, calculando a média dos primos gerados, e plotamos o gráfico.

## Resultados

<p align='center'>
    <img src='fig/resultado_14_03_2021.png'>
</p>

## Autores

[Leonam Teixeira de Vasconcelos](https://github.com/leonamtv)

[André Marcelino de Souza Neves](https://github.com/AndreNeves97)
