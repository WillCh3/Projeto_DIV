#faça um programa que leia 5 números e informe a soma e a média dos números.
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite segundo numero: "))
n3 = float(input("Digite terceiro numero: "))
n4 = float(input("Digite quarto numero: "))
n5 = float(input("Digite quinto numero: "))

soma = n1 + n2 + n3 + n4 + n5
media = soma/5

print(f"""

A soma é {soma}
a media é {media}


""")