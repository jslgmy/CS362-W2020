# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2020

@author: lagmayj
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = testUtility.playerNames()

#number of curses and victory cards
nV = testUtility.get_nV()
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.getBoxes(nV)
supply_order = testUtility.getSupplyOrd()


#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])


#The supply always has these cards
supply = testUtility.getSupply(nV, nC)


#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers()

#Play the game
turn  = 0
while not Dominion.gameover(supply):
#   turn += 1                                   #Error stops the game from incrementing turns, confusing the player
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
