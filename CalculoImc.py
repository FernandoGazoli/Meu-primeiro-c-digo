
'''
Auto: Luiz Fernando da Silva Gazoli
Data: 16/11/2022
Projeto: Cálculo IMC
'''

nome = str (input('Digite seu nome: '))

altura = float (input('Digite sua altura (centímetros): '))

peso = float (input('Digite seu peso (kg): '))

calculoimc = peso / altura **2


if calculoimc >= 18.5 and calculoimc <= 25.0: 
    print("Seu IMC está dentro do parâmetro, continue se alimentando bem e fazendo exercícios")
else:
    print("Seu IMC está fora dos padrões da estupulados pela ANVISA, procure um médico") 
