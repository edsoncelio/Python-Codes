
def condicoes_game(play1,play2):
    pass


def modo2play():
	jogadas = ['pedra','papel','tesoura','lagarto','spock']	
	play1 = raw_input('Jogador 1 : ')
	play2 = raw_input('Jogador 2 : ')
   
  



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

class __main__():
	print '''
Exemplo em python
Regras:
As opcoes sao:	pedra,papel,tesoura,lagarto,spock'''

entr = raw_input('''Escolha uma opcao:'
1- Jogar com o bot
2-jogar com outra pessoa
''')

if entr == '1':
   print 'modo contra bot'
   
else:
   print 'modo two players'
   modo2play()
   resp = raw_input('again? y/n: ')
while resp != 'n':
	modo2play()
	resp = raw_input('again? y/n: ')	

