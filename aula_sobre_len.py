'''
Data : 18/09/2020
Curso : Python 3 do Básico ao Avançado
Aluno : Marcos Gallo
Assunto da Aula : LEN
'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')