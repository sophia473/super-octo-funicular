ct = 0
soma = 0
print("ordem decrecente: ")
for numero in range(8,0,-1):
    print(numero)
    ct = ct + 1
    soma = soma+ numero
media = soma / ct
print(f'\nA quantidade de números na repetição: {ct}')
print(f"A soma dos números da repetição é: {soma}")
print(f'A média é: {media}')