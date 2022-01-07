'''
Exercícios Teóricos | Capítulo 9


1) O que é uma definição recursiva?

Função recursiva é aquela que invoca a si mesma.

Mecanismo útil e poderoso que permite a uma função chamar a si mesma direta ou indiretamente, ou seja,
uma função é dita recursiva se ela contém pelo menos uma chamada explícita ou implícita a si própria.

_ decompor um problema em subproblemas;
_ um ou mais dos subproblemas poderem ser resolvidos diretamente (casos de base)
_ um ou mais dos subproblemas serem semelhantes ao problema inicial casos recursivos)
_ os problemas semelhantes deverem ser tais que nos façam aproximar dos casos de base;
_ um processo de desenrolar, seguido por um de enrolar.


2) Que tipos de recursividade conhece?

Os exemplos mais clássicos de recursão é o algoritmo que calcula o fatorial e o a escala de Fibonacci.


3) Quando se deve recorrer à recursividade?

Dado um problema, ou o conseguimos resolver diretamente caso de base), ou o dividimos em subproblemas, alguns deles
semelhantes, aos quais aplicamos a mesma metodologia.

Quando um objeto se define em função dele próprio;
Quando um processo se decompõe em subprocessos semelhantes;


4) Como se pode transformar um programa recursivo?

Pode-se tentar fazer a transformação de modo manual: a ideia central passa pela introdução
de um mecanismo de pilha, que será usada para guardar os diferentes contextos das chamadas recursivas (fase de enrolar),
para mais tarde os podermos ir aí buscar e efetuar os cálculos do fatorial.
Ou seja, para remover a recursividade precisamos implementar um mecanismo de pilha.

Ou então, pelo módulo functools.


5) Em que consiste a técnica da memorização?

Consiste em guardar os cálculos já efetuados e, de cada vez que precisarmos de calcular um valor, consultarmos
primeiro a nossa memória antes de efetuar explicitamente os cálculos. O acesso à memória deve ser eficiente,
sob pena de se perder no acesso o que se ganha por não se ter de (re)fazer os cáculos.
Recorrer a um dicionário: a chave será n e o valor fib(n), por exemplo.

'''