##Exercício 1 (Questão 16)
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

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
