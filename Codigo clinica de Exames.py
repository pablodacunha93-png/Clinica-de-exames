import random
import json
from time import sleep

print('\n' + '===' * 13)
print('SEJA BEM VINDO(A) CLÍNICA DE EXAMES!')
print('===' * 13)

print('\nINICIANDO SISTEMA...\n')
# sleep(2)

def salvar_dados(dados):
    """Salva os dados do paciente em um arquivo JSON."""
    try:
        with open("pacientes.json", "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        lista = []

    lista.append(dados)

    with open("pacientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

print('Olá, seja bem vindo(a) a nossa clínica de exames!\n')
print('Vamos começar com seu cadastro. Por favor, informe os seguintes dados:')
    
nome = input('Nome: ')
email = input('E-mail: ')
    
while True:
    nmr = input('Número de telefone (apenas números com DDD): ')
    if nmr.isdigit() and len(nmr) == 11:
        break
    print('[ERRO] Número de telefone inválido. Informe 11 dígitos.')

paciente = {
    'nome': nome,
    'email': email,
    'numero': nmr
}
salvar_dados(paciente)

print('\nProcessando cadastro...\n')
sleep(1)
    
print('==' * 10)
print('Cadastro realizado')
print('==' * 10)

# Criamos um loop principal para caso o usuário erre a opção ou o dia

print('\nDeseja realizar um exame agora ou agendar?\n')

print('[A] Agendar exame')
print('[R] Realizar exame')

opcao = input('\nEscolha uma opção: ').strip().lower()

if opcao in ['a', 'agendar']:
    confirmado = False
    while True:
        dia = input("\nEscolha o dia: ").strip().lower()
        horarios = {
            "segunda": "13:00 e 17:00", "seg": "13:00 e 17:00",
            "terça": "09:00 e 15:00", "ter": "09:00 e 15:00",
            "quinta": "11:00 e 16:00", "qui": "11:00 e 16:00",
        }

        if dia in horarios:
            while True:
                hor = input(f"Horários para {dia.capitalize()} ({horarios[dia]}): ")
                if hor in horarios[dia]:
                    print("\n" + "="*30)
                    print(f"CONFIRMADO: {nome} | Dia: {dia.capitalize()} às {hor}")
                    print(f'Enviareamos detalhes para: {email}')
                    print("="*30)
                    confirmado = True
                    exit()
                    break 
                else:
                    print("\n[ERRO] Horário inválido!")
            
            if confirmado: break
        else:
            print("\n[ERRO] Dia não disponível!")

    # Fluxo para realizar exame agora
elif opcao in ['r', 'realizar', 'realizar exame']:        
    print('\n' + '==' * 10)    
    print('EXAMES DISPONÍVEIS')
    print('==' * 10)
    print('\n[1] Hemograma')
    print('\n[2] Glicemia')
    print('\n[3] Colesterol')
    print('\n[4] Triglicerídeos')
    print('\n[5] Urina\n')


    print('===' * 15)
    exame = input('Digite o nome ou número do exame: ').strip().lower()
    print('===' * 15)

        # Dicionário para facilitar a identificação do nome do exame
    exames_nomes = {
        '1': 'Hemograma', 'hemograma': 'Hemograma',
        '2': 'Glicemia', 'glicemia': 'Glicemia',
        '3': 'Colesterol', 'colesterol': 'Colesterol',
        '4': 'Triglicerídeos', 'triglicerídeos': 'Triglicerídeos', 'triglicerideos': 'Triglicerídeos',
        '5': 'Urina', 'urina': 'Urina'
        }

while True:
        if exame in exames_nomes:
            
            senha = random.randint(100, 999)
            
            salas = ['Consultório 1', 'Consultório 2', 'Consultório 3', 'Consultório 4', 'Consultório 5']
            
            consultorio = random.choice(salas)

            print('\nGerando sua ficha de atendimento...\n')
            sleep(2)
            print("-" * 30)
            print(f'PACIENTE: {nome}')
            print(f'EXAME: {exames_nomes[exame]}')
            print(f'SENHA: {senha}')
            print(f'LOCAL: {consultorio}')
            print("-" * 30)
            print(f'\nDetalhes enviados para: {email}\n')
            break
        else:
            print('\n[ERRO] Exame não reconhecido.')
            continue

def salvar_dados(dados):
    try:
        with open('fichas.json', 'r', encoding='utf-8') as arquivo:
            fichas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        fichas = []

    fichas.append(dados)

    with open('fichas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(fichas, arquivo, indent=4, ensure_ascii=False)

dados_ficha = {
        
        'nome': nome,
        'email': email,
        'numero': nmr,
        'exame': exames_nomes[exame],
        'senha': senha,
        'local': consultorio
    }
salvar_dados(dados_ficha)