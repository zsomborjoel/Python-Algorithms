"""
Készíts egy boolean tamadas(int monsterHp) függvényt. A függvény akkor ad igazat, ha a hős legyőzi a monstert. 
A harc körökre van osztva, a hős minden körben dob egy hat oldalú kockával, és pont ennyi életerőt sebez a monsteren. 
A paraméterben megadott szám adja a monster kezdeti életerejét. A monster is dob minden körben, és ha egy 7 oldalú kockával 7-est dob, akkor azonnal megöli a hőst.
"""


import randomdef fight(monsterhp):
    while True:
        dmg = random.randint(1,6)
        monsterdmg = random.randint(1,7)
        print('monster: ', monsterdmg)
        if monsterdmg == 7:
            return False
            continue
        
        print('player', dmg)
        monsterhp = monsterhp - dmg
        print('monsterhp: ',monsterhp)
        
        if monsterhp == 0:
            return True
            continue
        
#giving 50hp for the monster
fight(50)
