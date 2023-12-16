import conversion


print('Seja Bem-vindo ao Conversor de Moedas!')
print()

valor = float(input('Digite o valor que deseja converter: '))
moeda_origem = input('Digite a moeda de origem: ').upper()
moeda_destino = input('Digite a moeda de destino: ').upper()

valor_convertido = conversion.conversion(moeda_origem, moeda_destino, valor)

print(f'{valor} {moeda_origem}\n{valor_convertido} {moeda_destino}')
