# Geração de primos

Esse repositório contém o código para um trabalho da disciplina de Sistemas Distribuídos no CEFET-MG Timóteo. O código aqui presente, gera números primos indefinidamente (respeitando os limites do tamanho das variáveis) por **N** segundos de duas formas diferentes: uma abordagem sequencial e outra concorrente.

A geração concorrente acontece da seguinte forma:

1. Uma variável inteira armazena um número inicial.
2. Cada thread incrementa esse valor e verifica se o valor incrementado é primo (utilizando **mutex** para travar as partes críticas). Cada uma das threads executam um loop infinito.
3. Se o número for primo, ele é impresso no **stdout**.
4. Esse processo é executado por **N** segundos.

A geração concorrente acontece da seguinte forma:

1. Uma variável inteira armazena um número inicial.
2. Enquanto **N** segundos não se passarem, incrementamos o valor e verificamos se este é primo.
3. Se for primo, ele é impresso no **stdout**.

## Estratégia de análise de desempenho

* Gerar números primos sequencialmente por 5, 10, 20, 30, 40, 50 e 60 segundos, testando múltiplas vezes cada um dos tempos para que possamos tirar a média dos valores obtidos e diminuir a incerteza.
* Gerar números primos concorrentemente por 5, 10, 20, 30, 40, 50 e 60 segundos com 2, 4 e 8 threads, testando múltiplas vezes cada um dos tempos para que possamos tirar a média dos valores obtidos e diminuir a incerteza.
* Plotar tudo em um gráfico e analisar.

## Autores

[Leonam Teixeira de Vasconcelos](https://github.com/leonamtv)

[André Marcelino de Souza Neves](https://github.com/AndreNeves97)
