"""
Data : 18/09/2020
Curso : Python 3 do Básico ao Avançado
Aluno : Marcos Gallo
Assunto da Aula : Exercício Proposto

Problema

Faça um programa que peça o primeiro nome do usúario. Se o nome tiver 4 letras ou menos escreva
"Seu nome é curto"; se tiver entre 5 ou 6 letras, escreva "Seu nome é normal"; maior do que 6 escreva
"Seu nome é muito grande"
"""

nome = str(input('Escreva seu nome: '))
qtd_caracteres = len(nome)

if qtd_caracteres <= 4:
    print(f'{nome} é um nome curto')
elif qtd_caracteres == 5:
    print(f'{nome} é um nome normal')
elif qtd_caracteres == 6:
    print(f'{nome} é um nome normal')
else:
    var = qtd_caracteres > 7
    print(f'{nome} é um nome grande')
