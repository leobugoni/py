# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot('Falcatruas')

conv = ['oi', 'ola', 'tudo bem?', 'tudo e voce?', 'estou bem obrigado', 'como foi seu dia?', 'foi bom e o seu?', 'foi bom tambem']
convI = ['pra que time voce torce?', 'sou colorado e voce?', 'tambem sou, que pena termos perdido para a chapecoense no ultimo jogo', 'verdade, mas eles jogaram bem, mereceram a vitoria']
convII = ['qual seu candidato preferido para essa eleicao?', 'vou votar no bolsonaro e voce?', 'eu ainda nao sei, tem alguns dias ainda para escolher', 'verdade, mas nao esqueça que as eleicoes sao começo do mes que vem', 'sim, pode deixar']

bot.set_trainer(ListTrainer)

bot.train(conv)
bot.train(convI)
bot.train(convII)

while True:
	quest = input('Você: ')
	response = bot.get_response(quest)
	print('Bot: ', response)
	