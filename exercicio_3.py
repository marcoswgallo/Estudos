"""
Data : 19/09/2020
Curso : Python 3 do Básico ao Avançado
Aluno : Marcos Gallo
Assunto da Aula : Exercício Proposto

Problema

Faça um programa que peça ao usuário apra digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""
numero = (input('Digite um número:'))

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é Ímpar')

else:
    print('Isso não é um número inteiro.')
