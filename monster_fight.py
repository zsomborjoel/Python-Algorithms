"""
Készíts egy boolean tamadas(int monsterHp) függvényt. A függvény akkor ad igazat, ha a hős legyőzi a monstert. 
A harc körökre van osztva, a hős minden körben dob egy hat oldalú kockával, és pont ennyi életerőt sebez a monsteren. 
A paraméterben megadott szám adja a monster kezdeti életerejét. A monster is dob minden körben, és ha egy 7 oldalú kockával 7-est dob, akkor azonnal megöli a hőst.
"""


import random

def fight(monsterhp):
    while True:
        dmg = random.randint(1,6)
        monsterdmg = random.randint(1,7)
        print('Monster dmg: ', monsterdmg)
        if monsterdmg == 7:
        	print('Hero been killed')
        	return False
        	break

        print('Hero dmg', dmg)
        monsterhp = monsterhp - dmg
        print('Monster hp: ',monsterhp)

        if monsterhp <= 0:
        	print('Monster been killed.')
        	return True
        	break

#giving 50hp for the monster
fight(50)
