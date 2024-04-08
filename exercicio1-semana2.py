##Exercício 1 (Questão 16)
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
  
#Infos
  # 1 lata de tinta = 18 litros
  # 1 litro de tinta = 3 metros quadrados
  # 18 litros = 54 metros quadrados
  # 1 lata de tinta = R$80,00
  # A quantidade mínima de latas por pessoa é 1 (18L / 54 metros quadrados / R$80,00)
 
 #Passos
  # 1.Criar variáveis com as informações
  # 2.Input perguntando ao usuário "Qual a área em metros quadrados você quer pintar?"
  # 3.Função que calcula a proporção do número informado de metros quadrados com o número base de 1 lata de tinta (valor inputado / 54)
    # 3.1.Caso o valor recebido no passo 3 seja menor ou igual a 54, retornar o valor de 1 lata de tinta para o usuário.
    # 3.2.Caso o valor recebido no passo 3 seja um número maior do que 54, dividir por 54 e retornar o valor para o usuário. Obs.: caso o quociente da divisão seja um número decimal, arredondar o valor para baixo usando o operador aritmético //
  # 5.Função que multiplique o valor de 1 lata de tinta (R$80,00) pelo resultado do passo 3
  # 6.Apresentar o resultado para o usuário. 

metros_1lata = 54
entrada = int(input("Qual a área em metros quadrados você quer pintar? "))

def calculo_metros(entrada, metros_1lata):
  if (entrada <= 54):
    print("Você precisa de 1 lata de tinta. O preço total da sua compra será de R$80,00")
  if(entrada > 54):
    divisão = entrada//54
    valor_da_compra = divisão*80
    print("Você precisa de ", divisão, " latas de tinta. O preço total da sua compra será de R$ ", valor_da_compra, ",00", sep="")
    
calculo_metros(entrada,metros_1lata)
