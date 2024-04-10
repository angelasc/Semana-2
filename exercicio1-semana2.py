pintura_metros_1lata = 54
entrada = int(input("Qual a área em metros quadrados você quer pintar? "))

if (entrada <= 54):
  print("Você precisa de 1 lata de tinta. O preço total da sua compra será de R$80,00")
if(entrada > 54):
  divisão = entrada//54
  valor_da_compra = divisão*80
  print("Você precisa de ", divisão, " latas de tinta. O preço total da sua compra será de R$ ", valor_da_compra, ",00", sep="")
    
