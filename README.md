# Modelo Populacional de Colônia de Bactérias

## 1. Introdução

O objetivo deste trabalho é demonstrar como os resultados de um modelo populacional baseado em agentes (Agent-Based Model - ABM) variam conforme os parâmetros de entrada. O modelo populacional escolhido foi o de uma colônia de bactérias, onde cada bactéria se move aleatoriamente em um plano bidimensional e se reproduz quando está a uma distância mínima de outra bactéria. Este modelo foi implementado em Python utilizando o framework Mesa, que facilita a criação de simulações baseadas em agentes.

O modelo considera parâmetros como o número inicial de bactérias, a velocidade de movimento das bactérias, as dimensões do plano cartesiano e a distância mínima necessária para que a reprodução ocorra. O modelo foi projetado para analisar o impacto desses parâmetros no comportamento da colônia, especialmente no que diz respeito ao crescimento da população de bactérias ao longo do tempo.

## 2. Metodologia

### Agentes

O modelo é composto por agentes que representam as bactérias. Cada bactéria possui as seguintes características:
- **Posição**: As bactérias são inicialmente distribuídas aleatoriamente em um plano cartesiano bidimensional.
- **Movimento**: As bactérias se movem aleatoriamente em direção a qualquer ponto do plano com uma velocidade constante. A distância percorrida em cada movimento é fixada pelo parâmetro de "velocidade".
- **Reprodução**: Quando a distância entre uma bactéria e qualquer outra é menor que a distância mínima estabelecida, ocorre a reprodução. Uma nova bactéria é criada em uma posição aleatória no plano.

### Espaço

O espaço onde as bactérias se movimentam é um plano cartesiano bidimensional, cujas dimensões são parametrizáveis. As bactérias não podem se mover para fora dos limites desse plano.

### Ações dos Agentes

A cada passo da simulação, as bactérias realizam as seguintes ações:
1. **Movimento**: Cada bactéria se move aleatoriamente, respeitando os limites do espaço.
2. **Reprodução**: As bactérias verificam se a distância até a outra bactéria é inferior à distância mínima definida. Se for o caso, uma nova bactéria é criada.

### Algoritmos Utilizados

- **Cálculo de Distâncias**: As bactérias verificam a distância entre si usando o cálculo da norma Euclidiana entre as posições no plano cartesiano.
- **Reprodução Determinística**: A reprodução das bactérias ocorre de forma determinística, ou seja, sempre que a distância mínima entre duas bactérias é atingida.

## 3. Resultados

O modelo foi executado para diferentes valores de dois parâmetros principais: a população inicial \( p \) e a velocidade \( v \) das bactérias. Os seguintes valores foram testados:
- \( p \) variando entre [2, 3, 4].
- \( v \) variando entre [0.4, 1, 1.5, 3].

Cada uma das simulações foi executada com 15 passos (steps), pois, conforme o número de bactérias aumentava na colônia, era exigido cada vez mais tempo computacional para iterar sobre todos os agentes. Os resultados esperados incluem a observação do crescimento populacional das bactérias ao longo do tempo. Além disso, o comportamento das bactérias foi analisado em relação às variações na velocidade e na população inicial. Espera-se que com o aumento da velocidade, as bactérias se movimentem mais rapidamente e interajam com maior frequência, o que pode resultar em um aumento mais rápido da população. Já com o aumento da população inicial, a competição por espaço e a possibilidade de reprodução também aumentam.

## 4. Conclusão

Este modelo de colônia de bactérias foi implementado para simular o comportamento populacional de bactérias em um plano bidimensional. Os parâmetros de entrada, como a população inicial e a velocidade de movimento das bactérias, foram analisados para observar como influenciam o crescimento da população. O modelo, embora simples, fornece uma visão interessante sobre o comportamento de sistemas populacionais baseados em agentes.

### Limitações e Melhorias Futuras

O modelo desenvolvido possui algumas limitações que podem ser aprimoradas:
1. **Probabilidade de Reprodução**: Atualmente, a reprodução ocorre de forma determinística. Uma possível melhoria seria introduzir uma probabilidade para a reprodução, tornando o processo mais realista.
2. **Mortalidade das Bactérias**: O modelo atual não considera a morte das bactérias, o que pode ser introduzido para simular dinâmicas de competição e sobrevivência.
3. **Posicionamento das Novas Bactérias**: A criação das novas bactérias poderia ser feita de forma que elas se posicionem próximas à bactéria original, simulando um comportamento mais natural de propagação.

Com essas melhorias, o modelo pode se aproximar mais de simulações biológicas realistas, considerando variáveis adicionais como a mortalidade e a propagação espacial das bactérias.

