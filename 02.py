'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar
onde, informado um número, ele calcule a sequência de Fibonacci 
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibo_fun(numero):
    i = 0
    while True:
        fib_num = fibonacci(i)
        if fib_num == numero:
            return f"{numero} pertence à sequência de Fibonacci."
        elif fib_num > numero:
            return f"{numero} não pertence à sequência de Fibonacci."
        i += 1


numero = 3
print(fibo_fun(numero))

numero = 34
print(fibo_fun(numero))

numero = 35
print(fibo_fun(numero))

#O numero a ser calculado pode ser definidor na variavel 'numero'