##Exercício 3 (Questão 3)
#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#Passos
  #Definir 3 argumentos (3 números) para a função
  #Criar a função de Soma usando os argumentos definidos como parâmetros
  #Fazer a chamada da função


number1 = int(input("Escreva o primeiro número: "))
number2 = int(input("Escreva o segundo número: "))
number3 = int(input("Escreva o terceiro número: "))

def soma(number1, number2, number3):
  soma = number1+number2+number3
  print("A soma do seus números é:", soma)
  return print

soma(number1, number2, number3)

