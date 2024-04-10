metros_1galão = 21.6
entrada = float(input("Qual a área em metros quadrados você quer pintar? "))

import math

opção1_latas = math.ceil(entrada/108)
valor_da_compra1 = opção1_latas*80
print("Opção 1 (Somente latas): Você precisa de ", opção1_latas, " latas. O preço total da sua compra será de R$ ", valor_da_compra1, ",00.", sep="")
    
opção2_galões = math.ceil(entrada/21.6)
valor_da_compra2 = opção2_galões*25
print("Opção 2 (Somente galões): Você precisa de ", opção2_galões, " galões. O preço total da sua compra será de R$ ", valor_da_compra2, ",00.", sep="")

  
