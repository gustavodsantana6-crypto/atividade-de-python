import os

#Limpe o terminal.
os.system("cls || clear")

print("- Solicitando dados -") 
primeiro_numero = int(input("Digite o primeiro numero:  "))
segundo_numero = int(input("Digite seu segundo numero:"))

  #calculando
produto = primeiro_numero * segundo_numero
soma = primeiro_numero + segundo_numero
media =(primeiro_numero + segundo_numero)
media = soma /2

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero  
    menor = primeiro_numero  
    
print("\n- Exibindo dados -") 
print(f"Soma:{soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")