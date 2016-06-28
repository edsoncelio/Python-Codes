# -*- coding: utf-8 -*-
import os

#projeto de um joguim de 'rpg' modo texto :3

class Main(object):

     def ans_one(awr):
         if awr == 'claro':
		    print ('certeza? você é o mais velho aqui, vou confiar')
		    os.system('sleep 2')
		    print ('eles tinham bastante comidaaaa, escolha certa =D ')
		 	 	 	 
         elif awr == 'nem pense':
		      print ('é, talvez tenha razão, melhor não falar com estranhos')
		      os.system('sleep 4')
		      print ('cara, você vai me matar de fome, eu devia ter pedido ajuda a alguem util ')
		      exit(1)
         else:
		      print ('não entendi :/')
		      exit	
         
     def ans_intro(awr):
         if awr == 'sim':
		    print ('eba, alguém na escuta, obrigado por ser meu companheiro de viagem :) ')
		    os.system('sleep 2')
		    print ('Primeiro Capitulo : Pé na Estrada ')
		    print ('\n')
		 	 	 	 
         elif awr == 'não':
		      print ('poxa :(')
		      os.system('sleep 2')
		      print ('nesse caso, foi um desprazer te conhecer -.- ')
		      exit(1)
         else:
		      print ('não entendi :/ ')
		      exit	
         
     print ('Em uma terra muito distante existia um garoto com sede de conhecimento, entao ele resolveu partir...')
     print ('........')
     awr = raw_input('Oi, alguém ai? gostaria de me ajudar? [sim/não] ')
     print ('\n')
     ans_intro(awr)
     awr = raw_input('''O dia tá claro, passei por dois viajantes, ambos me olharam estranho, 
to cansado, devo pedir ajuda ?[claro/nem pense] ''')
     print ('\n')
     ans_one(awr)
     

    





if __name__=='__main__':
	pass
