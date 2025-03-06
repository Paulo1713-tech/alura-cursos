texto = input('Digite o texto a ser revisado: ')
subs = input('Qual palavra deseja substituir? ')
nova = input('Qual a nova palavra? ')

novo_texto = texto.replace(subs, nova)
print(f'\n{novo_texto}')

