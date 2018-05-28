#!/usr/bin/env python

from survey import AnonymousSurvey

# Define uma pergunta e cria uma pesquisa
question = 'What language didi you first learn to speak?'

# Instance
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena a resposta à pergunta
my_survey.show_question()
print('Digite \'q\' para encerrar.')

while True:
    response = input('Language: ')
    if response == 'q':
        break
    else:
        my_survey.store_response(response)
        

# Exibe o resultado da pesquisa
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()
