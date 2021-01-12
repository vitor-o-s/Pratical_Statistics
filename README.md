# Estatística Prática

Para uma melhor leitura recomendo o download do repositório.

Os códigos presentem aqui são apenas uma forma de estudo, em situações para resolução de problema utilize bibliotecas como Numpy ou SciPy que possuem funções otimizadas. 

Caso deseje colaborar com o resumo abra um PR.

Estudos de estatística voltado para Ciência de Dados (fonte: Estatística Prática para Cientistas de Dados, O'REILLY)

Statistical studies applied to Data Science (source: Estatística Prática para Cientistas de Dados, O'REILLY)

## 1 - Análise Exploratoria de Dados

O objetivo deste capítulo é criar uma base que servirá para entender experimentos e algoritmos discutidos mais adiante. Caso deseje poderá se aprofundar nos tópicos, contudo o objetivo aqui é um guia simples e rápido.

### Introdução 

Dados podem vir de diversas fontes, podendo ser não estruturados (sensores, eventos, textos, imagens, etc) ou estruturados. O primeiro desafio pode ser transformar dados brutos em estruturados afim de gerar informação acionável.

Dados estruturados podem ser classificados como: numérico e categórico. Os dados numéricos podem ser subdivididos em  contínuo ou discreto. No caso dos dados categóricos estes podem assumir apenas um conjunto fixo de valores, há dois casos que merecem atenção: dados binários e dados ordinais.

* ***Contínuos:*** Podem assumir qualquer valor (intervalo, flutuação, numérico)

* ***Discretos:*** Assumem somente valores inteiros (inteiro, contagem)

* ***Categóricos:*** Podem assumir apenas um conjunto específico de valores representando um conjunto de possíveis categorias. (enumeração, nominal, fatores).

* ***Binários:*** Assumem apenas duas categorias de valores (0/1, falso/verdadeiro).

* ***Ordinais:*** Possuem uma ordem explícita (fator ordenado).

Saber qual o tipo de dado nos ajudará a saber como nosso software processará os cálculos de uma determinada variável.

Em ciências de dados é comum que usemos um objeto de dados retangulares, o que significa algo como uma planilha ou tabela de uma banco de dados. Basicamente são matrizes bidimensonais onde as colunas indicam uma característica (variável) e a linha um registro (caso). 

* ***Característica:*** Coluna na tabela (atributo, entrada, indicador, variável)

Existem outras formas de estruturas de dados (como por exemplo a estrutura de grafos ou redes), porém nesse resumo focaremos apenas nos retangulares usados para a modelagem preditiva.



### Localização

''começar em média''

### Variabilidade

### Distribuição de Dados

### Tipos de Dados

### Correlação 

### Lidando com 2 ou mais variáveis



## 2 - Distribuições de Dados e Amostras

### Amostra Aleatória e Viés de Amostra

### Viés de Seleção 

### Distribuição de Amostragem de uma Estatística 

### Bootstrap

### Intervalo de Confiança

### Tipos de Distribuição 

#### Distribuição Normal

#### Distribuição de Cauda Longa

#### Distribuição t de Student

#### Distribuição Binomial

#### Distribuição de Poisson

#### Distribuição Exponencial

#### Distribuição Weibull


## 3 - Experimentos Estatísticos e Teste de Significância  

### Teste A/B 

### Teste de Hipótese

Teste de hipóteses ou testes de significância tem o objetivo de ajudar a descobrir se uma chance aleatória poderia ser responsável por um efeito observado. É importante que se tenha uma hipótese para que não subestimemos o comportamento aleatório natural e para não interpretarmos eventos aleatórios como se tivessem padrões de alguma significância.

Durante um teste A/B bem projetado são coletados dados sobre cada tratamento, e qualquer diferença entre os grupos A e B devem ser devido a uma diferença real entre os tratamentos A e B, ou a possibilidade aleatória de atribuição de indivíduos. O teste de hipótese é um meio de avaliar se a aleatóriedade é uma explicação (ou não) para a diferença entre os grupos A e B.

#### Hipótese Nula

Partindo da ideia de que reagimos a comportamentos incomuns tentando interpretá-los como significativos e reais, buscaremos provas de que a diferença entre os grupos é maior do que a possibilidade poderia produzir aleatoriamente. Logos dizemos que os tratamentos são iguais e qualquer diferença entre os grupos é devido a aleatoriedade. Podemos chamar essa afirmação de hipótese nula. Esperamos poder provar que a hipótese nula está errada e portanto os resultados para os grupos A e B são mais diferentes do que o acaso podria produzir. 

Um modo de fazer isso é atráves de um procedimento de reamostragem e permutação, no qual embaralhamos os resultados dos grupos A e B e distribuímos repetidamente os dados em grupos de tamanhos semelhantes, então observamos com que frequência obtemos uma diferença tão extrema quanto a diferença observada. 

#### Hipótese Alternativa 

Os testes de hipótese envolvem, por natureza, não apenas, uma hipótese nula, mas também uma hipótese alternativa contrária. Veja:

* Nula = "nenhuma diferença entre as médias do grupo A e B". alternativa = "A é diferente de B"

Em conjunto, as hipóteses nulas e alternativa devem representar todas as possibilidades. A natureza da hipótese nula determina a estrutura do teste de hipótese.

#### Teste de Hipótese Unilateral e Bilateral

Se em um teste A/B buscamos testar algo como padrão (A)/ nova opção (B) é preciso que haja uma hipótese direcional (B é melhor que A, caso contrário você permanece com A), logo usaremos um teste de hipótese unilateral (unicaudal). Isto significa que a possibilidade extrema resulta apenas umas contagem de direção no sentido do valor p.

Caso queira se proteger do acaso em qualquer direção deverá aplicar um teste bidirecional (bicaudal). Ou seja, possibilidades extremas resultam em contagens em qualquer uma das direções no sentido do valor p.

### Reamostragem 

### Significância Estatística e Valores P

### Teste t 

### Testagem Múltipla

### Graus de Liberdade 



## 4 - Regressão e Previsão 

## 5 - Classificação

## 6 - Aprendizado de Máquina EStatístico

## 7 - Aprendizado Não Supervisionado 
