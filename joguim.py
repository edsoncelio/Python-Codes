
import os
import random

  
''' Regras :
As regras de Pedra-papel-tesoura-lagarto-Spock sao:

    Tesoura corta papel
    Papel cobre pedra
    Pedra esmaga lagarto
    Lagarto envenena Spock
    Spock esmaga (ou derrete) tesoura
    Tesoura decapita lagarto
    Lagarto come papel
    Papel refuta Spock
    Spock vaporiza pedra
    Pedra quebra tesoura
'''
  


def cnd_game(play1,play2):
	jogadas = ['pedra','papel','tesoura','lagarto','spock']	
	
	if (play1 == jogadas[0] and play2 == jogadas[1]) or (play1 == jogadas[1] and play2 == jogadas[0]):
		print 'papel cobre pedra'
	elif (play1 == jogadas[0] and play2 == jogadas[2]) or (play1 == jogadas[2] and play2 == jogadas[0]):
		print 'pedra quebra tesoura'
	elif (play1 == jogadas[0] and play2 == jogadas[3]) or (play1 == jogadas[3] and play2 == jogadas[0]):
		print 'pedra esmaga lagarto'
	elif (play1 == jogadas[0] and play2 == jogadas[4]) or (play1 == jogadas[4] and play2 == jogadas[0]):			
		print 'spock vaporiza pedra'
	elif (play1 == jogadas[1] and play2 == jogadas[2]) or (play1 == jogadas[2] and play2 == jogadas[1]):
		print 'tesoura corta papel'
	elif (play1 == jogadas[1] and play2 == jogadas[3]) or (play1 == jogadas[3] and play2 == jogadas[1]):
		print 'lagarto come papel'
	elif (play1 == jogadas[1] and play2 == jogadas[4]) or (play1 == jogadas[4] and play2 == jogadas[1]):
		print 'papel refuta spock'
	elif (play1 == jogadas[2] and play2 == jogadas[3]) or (play1 == jogadas[3] and play2 == jogadas[2]):
		print 'tesoura decapita lagarto'
	elif (play1 == jogadas[2] and play2 == jogadas[4]) or (play1 == jogadas[2] and play2 == jogadas[4]):
		print 'spock derrete tesoura'
	elif (play1 == jogadas[3] and play2 == jogadas[4]) or (play1 == jogadas[4] and play2 == jogadas[3]):
		print 'lagarto envenena spock'
	else:
		print 'empate, vixi'							

def mode2play():
    play1 = raw_input('Jogador 1 : ')
    play2 = raw_input('Jogador 2 : ')
    cnd_game(play1,play2)
     

def modobot():
	jogadas = ['pedra','papel','tesoura','lagarto','spock']
	play1 = raw_input('Jogador 1 : ')
	if str(play1) in jogadas:
		for i in range(len(jogadas)):
		    bot = random.choice(jogadas)
		print 'jogada do bot : '+bot
		cnd_game(play1,bot)

class __main__():
	print '''
Joguim em Py
Regras:
As opcoes de jogadas sao: pedra,papel,tesoura,lagarto,spock'''

entr = raw_input('''Escolha uma opcao:'
1- Jogar com o bot
2-jogar com outra pessoa
''')

if entr == '1':
   print 'modo contra bot'
   modobot()
   resp = raw_input('again? y/n: ')
   while resp !='n':
	   modobot()
	   resp = raw_input('again? y/n: ')
else:
   print 'modo two players'
   mode2play()
   resp = raw_input('again? y/n: ')
while resp != 'n':
	mode2play()
	resp = raw_input('again? y/n: ')	

