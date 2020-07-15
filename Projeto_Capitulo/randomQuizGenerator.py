#! python3
# randomQUizGenerator.py - Cria provas com perguntas e respostas em ordem aleatória
# juntamente com os gabaritos contendo as respostas.

import random

captals = {'Acre (AC)': 'Rio Branco', 'Alagoas (AL)': 'Maceió', 'Amapá (AP)': 'Macapá', 'Amazonas (AM)': 'Manaus',
           'Bahia (BA)': 'Salvador', 'Ceará (CE)': 'Fortaleza', 'Distrito Federal (DF)': 'Brasília',
           'Espírito Santo (ES)': 'Vitória', 'Goiás (GO)': 'Goiânia', 'Maranhão (MA)': 'São Luís', 'Mato Grosso (MT)':
           'Cuiabá', 'Mato Grosso do Sul (MS)': 'Campo Grande', 'Minas Gerais (MG)': 'Belo Horizonte', 'Pará (PA)':
           'Belém', 'Paraíba (PB)': 'João Pessoa', 'Paraná (PR)': 'Curitiba', 'Pernambuco (PE)': 'Recife',
           'Piauí (PI)': 'Teresina', 'Rio de Janeiro (RJ)': 'Rio de Janeiro', 'Rio Grande do Norte (RN)': 'Natal',
           'Rio Grande do Sul (RS)': 'Porto Alegre', 'Rondônia (RO)': 'Porto Velho', 'Roraima (RR)': 'Boa Vista',
           'Santa Catarina (SC)': 'Florianópolis', 'São Paulo (SP)': 'São Paulo', 'Sergipe (SE)':  'Aracaju',
           'Tocantins (TO)': 'Palmas'}

# Gera os arquivos contendo as provas de acordo com a quantidade de loopings.
for quizNum in range(1):
    # Cria os arquivos de prova e gabarito
    quizFile = open(f'captalsquiz{quizNum + 1}.txt', 'w', encoding='utf-8')
    answerKeyFile = open(f'capital_answers{quizNum + 1}.txt', "w", encoding='UTF-8')

    # Escreve o cabeçalho da prova
    quizFile.write(f'Name: \n\nDate: \n\nPeriod: \n\n')
    quizFile.write(f'{"*" * 20} State Captals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    # Embaralha a lista de estados
    states = list(captals.keys())
    random.shuffle(states)

    # Percorre todos os estados criando um looping para gerar uma pergunta para cada
    for questionNum, _ in enumerate(states):
        correctAnswer = captals[states[questionNum]]
        wrongAnswers = list(captals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Grava pergunta e as opções de resposta no arquivo de prova
        quizFile.write(f'{questionNum + 1}. What is the captal of {states[questionNum]}? \n')
        for i in range(4):
            quizFile.write(f'\t( {"ABCD"[i]} ) {answerOptions[i]}\n')
        quizFile.write('\n')

        # Grava o gabarito com as respostas em um arquivo
        answerKeyFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')
    quizFile.close()
    answerKeyFile.close()
