"""
Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. 
Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.

Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?

Exemplo de Entrada:

Digite a URL para validação: https://monitorrenan.com

Saída esperada:

URL válida!
"""
url = 'https://monitorrenan.com'
comeco_url = url.startswith('https://')
fim_url = url.endswith('.com')

if comeco_url and fim_url:
   print('URL válida!')
else:
    print("URL inválida!")