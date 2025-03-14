# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que 
# todos os números de telefone dos clientes estão armazenados como strings. No entanto,
# para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, 
# faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão 
# foi feita corretamente e todos os números de telefone são inteiros:

## Exemplo de entrada:
# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

## Saida esperada:
# Todos os números foram convertidos corretamente!

def converter_telefones_para_inteiro(telefones):
    for i in range(len(telefones)):
        telefones[i] = int(telefones[i])
    return "Todos os números foram convertidos corretamente!"

def verificar_conversao_inteiro(telefones):
    for telefone in telefones:
        if not isinstance(telefone, int):
            return "Existem números de telefone não convertidos!"
    return "Todos os números foram convertidos corretamente!"

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

print(converter_telefones_para_inteiro(telefones))
print(verificar_conversao_inteiro(telefones))