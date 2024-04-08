##Exercício 2 (Questão 17)
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
  #Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    #comprar apenas latas de 18 litros;
    #comprar apenas galões de 3,6 litros;
    #misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
  
#Infos
  # Lata de tinta = 18 litros (R$ 80,00)
  # Galão de tinta = 3,6 litros (R$ 25,00)
  # 1 litro de tinta = 6 metros quadrados
  # 18 litros = 108 metros quadrados
  # 3,6 litros = 21,6 metros quadrados
  # 5 galões = 1 lata
  # A quantidade mínima por pessoa é 1 galão (3,6L / 21,6 metros quadrados / R$25,00)
 
 #Passos
  # 1.Criar variáveis com as informações
  # 2.Input perguntando ao usuário "Qual a área em metros quadrados você quer pintar?"
  # 3.Função que calcula a proporção do número informado de metros quadrados com o número base de 1 galão de tinta (valor inputado / 21,6)
    # 3.1.Caso o valor recebido no passo 3 seja menor ou igual a 21,6, retornar o valor de 1 galão de tinta para o usuário.
    # 3.2.Caso o valor recebido no passo 3 seja um número maior do que 21,6, retornar para o usuário 3 opções:
      #Opção 1 - Apenas latas: dividir o valor recebido no input por 108 
      #Opção 2 - Apenas galões: dividir o valor recebido no input por 21,6
      #Opção 3 - Latas e galões: multiplicar o valor recebido no input por 10% (0,1) e dividir por
      # Obs.: caso o quociente da divisão seja um número decimal, arredondar o valor para baixo usando o operador aritmético //
  # 5.Função que multiplique o valor de 1 lata de tinta (R$80,00) pelo resultado do passo 3
  # 6.Apresentar o resultado para o usuário. 

metros_1galão = 21.6
print(type(metros_1galão))
entrada = float(input("Qual a área em metros quadrados você quer pintar? "))

def calculo_metros(entrada, metros_1galão):
  if (entrada <= 21.6):
    print("Você precisa de 1 galão de tinta. O preço total da sua compra será de R$25,00")
  
  if (entrada > 21.6):
    opção_latas = int(entrada//108)
    ceil(opção_latas)
    valor_da_compra_latas = int(opção_latas*80)
    print("Opção 1 (Somente latas): Você precisa de ", opção_latas, " latas. O preço total da sua compra será de R$", valor_da_compra_latas, ",00", sep="")
    
    opção_galões = int(entrada//21.6)
    valor_da_compra_galões = int(opção_galões*80)
    print("Opção 2 (Somente galões): Você precisa de ", opção_galões, " galões. O preço total da sua compra será de R$", valor_da_compra_galões, ",00", sep="")

  if (entrada > 108):
    opção_galões_latas = int(entrada//21.6)
    print("Continua...")
    
    
calculo_metros(entrada,metros_1galão)
