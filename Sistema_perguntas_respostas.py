perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': {'a':'1','b': '3','c': '4','d': '5'},
        'Resposta': 'c',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': {'a':'25','b': '55','c': '10','d': '51'},
        'Resposta': 'a',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': {'a':'4','b': '5','c': '2','d': '1'},
        'Resposta': 'b',
    },
    {
        'Pergunta': 'Quanto é 2*6?',
        'Opções': {'a':'10','b':'12','c':'8','d':'15'},
        'Resposta': 'b'
    },
    {
        'Pergunta': 'Quanto é 3+5*2?',
        'Opções': {'a':'10','b':'12','c':'15','d':'13'},
        'Resposta': 'd'
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in opcoes.items():
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    qtd_opcoes = len(opcoes)

    

    if escolha is not None:
        if escolha == pergunta['Resposta']:
            acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')