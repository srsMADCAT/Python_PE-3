#! python
# coding: utf-8

import random
import time

cases={
"so":"you lose.loser.",
"os":"You win! Nice job Vanga.",
"o#":"you lose.loser.",
"#o":"You win! Nice job Vanga.",
"s#":"You win! Nice job Vanga.",
"#s":"you lose.loser.",
"oo":"draw",
"ss":"draw",
"##":"draw"
}

def reply():
	reply_vars=['o','s','#']
	return reply_vars[random.randint(0,2)]
	
print('THIS IS WAAAAR! \n Joking. Not realy a war but a \n Rock-paper-scissors game \n s for scissors \n o for rock \n # for paper \n')

play=True;

while play:
	player=input('Enter your choose(s , o or #) \n')
	bot=reply()
	print('Su...\n')
	time.sleep(0.7)
	print('Je..\n')
	time.sleep(0.7)
	print('...Fa\n')
	time.sleep(0.7)
	print('bot answer ' + str(bot))
	print(cases[player+bot])
	more=input('try again? (y/n)')
	if more == 'n':
		play = False