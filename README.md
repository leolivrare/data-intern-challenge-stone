# Desafio de Data Stone
### [Enunciado do Desafio](https://gist.github.com/Pelielo/e4d84c76c43cd8fc913c4cd101194b82)

## Como rodar o projeto:
### Rodar com Dockerfile:
Para executar o projeto utilizando o Dockerfile, basta ter o [Docker](https://www.docker.com/) instalado na sua máquina e executar os seguintes comandos:  

#### Para construir a imagem do Docker:  
<code>docker build -t challenge-app</code>  
#### Para executar a imagem do Docker:  
<code>docker run challenge-app</code>

### Rodar localmente:
Para executar o projeto localmente, voce deve ter todas as bibliotecas utilizadas no projeto instaladas na sua máquina e a versão adequada do python.
#### Versão do python: 3.7.6
#### Bibliotecas Utilizadas:
##### [Pandas 1.0.1](https://pandas.pydata.org/):  
<code>pip install pandas</code>
##### [Psycopg2 2.8.5](https://pypi.org/project/psycopg2/): Se os pré requisitos estiverem instalados, basta executar:  
<code>pip install psycopg2</code>
##### [Jupyter 1.0.0](https://jupyter.org/):
<code>pip install jupyterlab</code>
##### [Matplotlib 3.1.3](https://matplotlib.org/3.1.1/index.html):
<code>pip install matplotlib</code>
##### [Plotly 4.9.0](https://plotly.com/):
<code>pip install plotly</code>
##### [Cufflinks 0.17.3](https://github.com/santosjorge/cufflinks):
<code>pip install cufflinks</code>
#### Com as bibliotecas instaladas, basta executar a main do projeto:  
<code>python main.py</code>
#### Para executar os scripts para gerar os gráficos, voce deve executar o jupyter com o comando:
<code>jupyter notebook</code>


## Primeira Parte
#### Código da Solução: [first_part.py](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/first_part.py)
### Primeiro Desafio
#### Solução está na função [get_customers_average_age(db)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/first_part.py)
|Objetivo|Resultado|
|------|--------|
|Obter a idade média dos clientes no banco de dados.|A idade média obtida foi de 35 anos|
****
### Segundo Desafio
#### Solução está na função [get_card_family_limit_analisys(db)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/first_part.py)

|Objetivo|Resultados|
|------|--------|
|Relacionar o limite de crédito do cartão à sua familia.|![Resultado ex2](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/imagens/card_family_analysis.png)|
### Visualização dos Resultados
![Img ex2](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/imagens/max_min.png)
#### Comentários sobre os Resultados:

Como pode ser visto na tabela de resultados, o ranking de familia de cartões está diretamente ligado ao limite de crédito de cada cartão. Vamos então analisar o limite de cada familia de cartão.

|Gold|Platinum|Premium|
|----|----|----|
|Pode-se notar que, com os dados utilizados, o menor limite de crédito para essa família de cartão é de R$2.000,00 e o maior limite de crédito é de R$50.000,00. Além disso, pode-se notar no gráfico que o maior limite de crédito da família Gold é inferior ao menor limite da família Platinum, ou seja, o intervalo de limite da família Gold não se sobrepõe ao da família Platinum. Portanto, se um cartão possuí um limite menor que R$50.000,00, o mesmo é da família Gold.|Nota-se que o menor limite de um cartão Platinum registrado no banco de dados é de R$51.000,00, que é logo acima do limite máximo dos Golds, ou seja, possivelmente quando um cartão Gold supera o limite de R$50.000,00 de crédito, o mesmo sobe no ranking para Platinum, caso o limite não extrapole o máximo dos Platinum. Por outro lado, o maior limite registrado no banco de dados para um cartão Platinum foi de R$200.000,00, o qual é superior ao menor limite de um cartão Premium, como se pode notar no gráfico. Portanto, existe uma sobreposição de valores no intervalo de limite de crédito da família Platinum com o intervalo da família Premium. Logo, quando um cartão possui de R$108.000,00 a R$200.000,00 de limite de crédito, não conseguimos afirmar com certeza a qual família o cartão pertence. Somente quando o limite supera o valor de R$200.000,00 que, nos nossos dados, o cartão pertence à família Premium.|O que podemos concluir dos cartões Premium é que o menor limite registrado no banco de dados é de R$108.000,00. Portanto, existe uma sobreposição dos intervalos de limite de crédito entre a família Platinum e a Premium. Porém, quando um cartão ultrapassa os R$200.000,00 de limite de crédito, podemos concluir que o mesmo possui uma grande chance de ser da família Premium.
****
### Terceiro Desafio
#### Solução está nas funções [get_highest_value_fraud_id(db)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/first_part.py)

|Objetivo|Resultado|
|------|--------|
|Encontrar qual o ID da transação fraudulenta de maior valor|A fraude de maior valor possui o ID: CTID20567160|
#### As fraudes de maior valor:
#### Solução na função: [get_most_expensive_frauds(db)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/first_part.py)
|Fraud ID|Card Number|Date               |Value (R$)|Segment|Fraud Flag|
|--------|-----------|-------------------|-----|-------|----------|
|CTID20567160|3295-6390-4452-7199|2016-10-08         |49155|SEG16  |True      |
|CTID15034243|4562-2665-7578-1931|2016-02-14         |48845|SEG19  |True      |
|CTID95884307|2017-7197-7814-9950|2016-11-07         |48588|SEG16  |True      |
|CTID54759604|8262-8743-6406-7105|2016-09-07         |48567|SEG20  |True      |
|CTID55429304|9030-1667-6058-6173|2016-03-03         |48514|SEG15  |True      |

****
## Segunda Parte
### Código da Solução: [second_part.py](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
|Objetivo|
|--------|
|Analisar se as transações fraudulentas estão associadas, ou não, com algum dado do banco de dados|

### Resultados
#### Análise sobre o valor médio das transações:
##### Solução na função [analyse_mean(df_frauds_trans)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
 Media das transações sem fraude: **R$24736.15**                                         
 Valor médio das fraudes: **R$26808.88**     
 As fraudes possuem, em média, valor **7.73%** mais alto do que as transações normais.
 
#### Análise sobre o desvio padrão das transações:
##### Solução na função [analyse_std(df_frauds_trans)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
O desvio padrão das transações é **R$14378.64**  
O desvio padrão das fraudes é **R$13574.31**  
O desvio padrão das fraudes é menor que o das transações.  

#### Análise sobre os valores máximos e mínimos:
##### Solução na função [analyse_max_min(df_frauds_trans)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
Valor minimo das transações não fraudulentas: **R$103**  
Valor minimo das fraudes: **R$683**  
Valor maximo das transações não fraudulentas: **R$49995**  
Valor maximo das fraudes: **R$49155**  

#### Análise sobre a mediana dos valores das transações:
##### Solução na função [analyse_median(df_frauds_trans)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
A mediana das transações não fraudulentas é: **R$24631.0**  
A mediana das fraudes é **R$29746.0**  
A mediana das fraudes é **17.20%** mais alto que as transações normais.  

#### Taxa de fraudes por segmentos
##### Solução na função [get_fraud_rate_segments(df_frauds_trans)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
|Segment|Transactions|Frauds|Fraud Rate (%)     |
|-------|------------|------|-------------------|
|SEG11  |659.0       |15.0  |2.27 |
|SEG12  |695.0       |6.0   |0.86 |
|SEG13  |679.0       |4.0   |0.58 |
|SEG14  |623.0       |6.0   |0.96 |
|SEG15  |683.0       |6.0   |0.87 |
|SEG16  |667.0       |8.0   |1.19 |
|SEG17  |651.0       |8.0   |1.22 |
|SEG18  |682.0       |4.0   |0.58 |
|SEG19  |658.0       |3.0   |0.45 |
|SEG20  |668.0       |6.0   |0.89 |
|SEG21  |633.0       |10.0  |1.57 |
|SEG22  |632.0       |9.0   |1.42 |
|SEG23  |708.0       |12.0  |1.69 |
|SEG24  |669.0       |8.0   |1.19 |
|SEG25  |693.0       |4.0   |0.57 |

#### Taxa de fraudes por mes
##### Solução na função [get_fraud_rate_month(df_frauds_trans)](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part.py)
|Month|Transactions|Frauds|Fraud Rate (%)     |
|-----|------------|------|-------------------|
|1    |828.0       |9.0   |1.08 |
|2    |775.0       |10.0  |1.29 |
|3    |868.0       |9.0   |1.03 |
|4    |807.0       |9.0   |1.11 |
|5    |868.0       |7.0   |0.80 |
|6    |838.0       |10.0  |1.19 |
|7    |840.0       |7.0   |0.83 |
|8    |840.0       |9.0   |1.07 |
|9    |803.0       |14.0  |1.74 |
|10   |870.0       |8.0   |0.91 |
|11   |859.0       |7.0   |0.81 |
|12   |804.0       |10.0  |1.24 |


### Visualização dos Resultados
#### Código da Solução: [second_part_visualization.py](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/second_part_visualization.ipynb)
![Resultado part2](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/imagens/fraud_rate_per_seg.png)

![PART2](https://github.com/leolivrare/data-intern-challenge-stone/blob/master/imagens/fraud_rate_per_month.png)

### Comentários sobre os resultados:
Vamos analisar os resultados obtidos por partes.
#### Análise dos valores das transações:
Pode-se notar que os valores das transações fraudulentas são, em média, 7.73% mais altos do que das transações normais. Além disso, vemos que o valor máximo das transações fraudulentas é até menor que o máximo das transações normais, o que indica que não existe um valor que extrapola muito a média, o que poderia comprometer o valor obtido na média. Com isso, temos um valor mais fiel da mesma. Portanto, temos que os valores das fraudes são, em média, maiores que transações normais.
Por outro lado, temos um resultado bastante interessante acerca da mediana dos valores das transações. A mediana dos valores das transações fraudulentas é 17.2% maior do que a mediana dos valores das transações normais. Isso indica, e reforça, que as transações fraudulentas possuem um valor mais alto em relação às transações normais. Isso nos revela que transações de alto valor possuem maior chance de serem fraudes. Porém, vale ressaltar que não são apenas transações de alto valor que são fraudes.
Além disso, vale ressaltar que o desvio padrão das transações fraudulentas é menor que o das transações normais. Ou seja, o conjunto de dados dos valores das fraudes é mais uniforme, o que indica uma menor dispersão nos valores. Porém, vale deixar claro que temos um número bem menor de fraudes do que transações normais, o que pode justificar essa diferença no valor do desvio padrão.
#### Análise da taxa de fraude por seguimento:
Pode-se notar no gráfico de taxa de fraude por seguimento, que existe uma grande diferença em relação à taxa de fraude entre os seguimentos. Dessa forma, vemos que o seguimento 11 é o que possui a maior taxa de fraudes, logo, é o segumento mais vulnerável à fraude.
Ademais, vemos que os seguimentos 11, 23 e 21 são os com maior taxa de fraude, portanto, são os mais vulneráveis. Por outro lado, os seguimentos 19, 18, 25 e 13 são os com menor taxa de fraude, sendo assim os menos vulneráveis. A diferença entre o seguimento mais vulnerável e o menos vulnerável é tão grande, que o mais vulnerável (SEG 11) possui uma taxa de fraude 5 vezes maior que o menos vulnerável (SEG 19), ficando claro que existem seguimentos mais vulneráveis que outros, os quais precisam de uma maior estrutura anti-fraude para uma maior segurança.
#### Análise da taxa de fraude por mes:
Através do gráfico de taxa de fraudes por mes, pode-se notar uma variação menor na taxa de fraudes em relação à análise por seguimentos. Porém, mesmo com uma menor variação, ainda temos diferenças significantes entre os meses. Com isso, vemos que o mes de novembro se destaca quanto à sua taxa de fraudes. Nota-se que a taxa de fraude desse mes é mais de duas vezes maior que a do mes de maio. Isso pode ocorrer devido a alguma data comemorativa, como a BlackFriday, nesse mes. Porém, para podermos afirmar que esse mes sempre possui uma taxa maior que os outros, deve ser feita análises com dados de outros anos e ver se forma um padrão. Portanto, apenas com esses dados, podemos ver que pode existir uma relação entre as datas e as transações fraudulentas, principalmente com as datas comemorativas.
