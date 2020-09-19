"""
Data : 19/09/2020
Curso : Python 3 do Básico ao Avançado
Aluno : Marcos Gallo
Assunto da Aula : Formatando Valores

Formatando valores com modificadores

:s - Texto (Strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. - (NÚMERO)f - Quantidade de casas decimais (float)
: - (CARACTERE) (> ou < ou ^)(QUANTIDADE/TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
nome = 'Marcos Gallo'
print(f'{nome:s}')
print(f'{num_1:0>10}')
print(f'{num_1:0<10}')