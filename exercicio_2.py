"""
Data : 19/09/2020
Curso : Python 3 do Básico ao Avançado
Aluno : Marcos Gallo
Assunto da Aula : Exercício Proposto

Problema

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex
Bom dia 0 - 11, Boa tarde 12-17 e Boa noite 18-23.
"""



nome = str(input('Qual seu nome: '))
horas = int(input('Por favor Digite as horas: '))
minutos = int(input('Por Favor Digite os minutos: '))

if horas < 12:
    print(f'Olá, {nome} são {horas}:{minutos}  tenha um Bom dia')
elif horas < 17:
    print(f'Olá, {nome} são {horas}:{minutos}  tenha uma Boa Tarde')
else:
    print(f'Olá, {nome} são {horas}:{minutos}  tenha uma Boa noite')
