"""
Data : 25/09/2020
Curso : Python 3 do Básico ao Avançado
Aluno : Marcos Gallo
Assunto da Aula : Iterando Strings com While

Índices

"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
