'''Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____'''

#a) A sequência segue um padrão de números ímpares começando por 1 e 
#incrementando de 2 em 2. Portanto, o próximo elemento é 9.

numero = 1
i = 0
while i  <= 3:
    i = i + 1
    numero = numero +2
print('A) o proximo elemento é o numero: ', numero)

#b) Esta sequência é uma progressão geométrica onde cada termo é o 
#dobro do anterior. O próximo elemento é 128.

numero = 2
i = 0
while i  <= 5:
    i = i + 1
    numero = numero *2
print('B) o proximo elemento é o numero: ', numero)


#c) Os termos desta sequência são quadrados perfeitos, ou seja, ( n^2 ), 
#onde ( n ) é um número inteiro começando de 0. O próximo elemento é 49.

numero = 0
i = 0
while i  <= 6:
    i = i + 1
    numero = i*i
print('C) o proximo elemento é o numero: ', numero)

#d) Semelhante à sequência c), esta sequência também é composta por quadrados perfeitos,
#mas apenas de números pares. O próximo elemento é 100.

numero = 4
numero_par= 0
i = 0
while i  <= 9:
    i = i + 1
    numero = i*i
    if numero % 2 == 0:
        numero_par = numero
  
print('D) o proximo elemento é o numero: ', numero_par)

#e) Sequência de Fibonacci, onde cada termo é a soma dos dois anteriores. 
#O próximo elemento é 13.

def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        next_number = sequencia[-1] + sequencia[-2]
        sequencia.append(next_number)
    return sequencia

numero = 8
resultado = fibonacci(numero)
print('E) o proximo elemento é o numero: ', resultado[7])

#f) A sequencia é após o número 2, ela incrementa de 1 em 1, exceto pelo salto de 2 para 10. 
#O próximo elemento após 19 é 20.

def numero_sequencia(sequencia):

    return sequencia[-1] + 1

sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_numero = numero_sequencia(sequencia_f)

print("F) O próximo elemento é o numero:" , proximo_numero)