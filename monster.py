# Monster.py
# Thorin Schmidt
# 11/16/2016

''' Monster Package '''
from character import *
from random import randint, choice

class Monster(Character):
    ''' generic monster class '''
    def __init__(self,
                 name = "Generic Foe",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 10,
                 intelligence = 10,
                 dexterity = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 50,
                 awareness = 50,
                 fear = 50):
        super(Monster, self).__init__(name, maxHealth, speed, stamina,
                                      strength, intelligence, dexterity,
                                      numberOfPotions, inventory)
        self.aggression = aggression
        self.awareness = awareness
        self.fear = fear  #indicates cowardice level

    def combat_choice(self):
        ''' combat AI

            returns a, h, or f.  Based on aggression, awareness, morale
            
            '''
        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness
        fleeValue = randint(1,100) + self.fear

        if attackValue >= healValue and attackValue >= fleeValue:
            return "a"
        elif healValue >= attackValue and healValue >= fleeValue:
            return "h"
        elif fleeValue >= attackValue and fleeValue >= healValue:
            return "f"
        else:
            return "AI_error"

class Boss(Monster):
    ''' Serves as a bass class for boss monsters that stops them from fleeing '''
    def __init__(self,
                 name = "Dorque da Orc",
                 maxHealth = 100,
                 speed = 25,
                 stamina = 25,
                 strength = 8,
                 intelligence = 8,
                 dexterity = 8,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 80,
                 awareness = 30,
                 fear = 20):
        super(Boss, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

    def combat_choice(self):
        ''' combat AI

            returns a, h, or f.  Based on aggression, awareness, morale

            '''
        attackValue = randint(1, 100) + self.aggression
        healValue = randint(1, 100) + self.awareness

        if attackValue >= healValue:
            return "a"
        elif healValue >= attackValue:
            return "h"
        else:
            return "AI_error"

class Orc(Monster):
    ''' generic Orc class '''
    def __init__(self,
                 name = "Dorque da Orc",
                 maxHealth = 100,
                 speed = 25,
                 stamina = 25,
                 strength = 8,
                 intelligence = 8,
                 dexterity = 8,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 80,
                 awareness = 30,
                 fear = 20):
        super(Orc, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

class Chicken(Monster):
    ''' generic Chicken class'''
    def __init__(self,
                 name = 'Clucky',
                 maxHealth=15,
                 speed=20,
                 stamina=20,
                 strength=1,
                 intelligence=1,
                 dexterity=1,
                 numberOfPotions=0,
                 inventory=[],
                 aggression=0,
                 awareness=20,
                 fear=80
                 ):
        super(Chicken, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

class Raider(Monster):
    '''generic Raider class'''
    def __init__(self,
                 name = 'Ray',
                 maxHealth=100,
                 speed=25,
                 stamina=25,
                 strength=10,
                 intelligence=6,
                 dexterity=8,
                 numberOfPotions=1,
                 inventory=[],
                 aggression=60,
                 awareness=35,
                 fear=50
                 ):
        super(Raider, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
        self.weapon = Weapon(name='Longsword', base=8, bonus=1)
        self.armor = Armor(name='Studded Leather', base=2, bonus=1)

class CultFanatic(Boss):
    ''' serves as a first Boss '''
    def __init__(self,
                 name = 'Francis',
                 maxHealth=225,
                 speed=25,
                 stamina=25,
                 strength=14,
                 intelligence=16,
                 dexterity=10,
                 numberOfPotions=4,
                 inventory=[],
                 aggression=75,
                 awareness=25,
                 fear=10
                 ):
        super(CultFanatic, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
        self.weapon = Weapon(name='Battle Axe', base=10, bonus=2)
        self.armor = Armor(name='Studded Leather', base=3, bonus=2)

class Avatar(Boss):
    ''' A monster that is a representation of a deity's spirit '''
    def __init__(self,
                 name = 'Francis',
                 maxHealth=float('inf'),
                 speed=50,
                 stamina=1000000,
                 strength=16,
                 intelligence=16,
                 dexterity=18,
                 numberOfPotions=10,
                 inventory=[],
                 aggression=75,
                 awareness=25,
                 fear=10
                 ):
        super(Avatar, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
        self.weapon = Weapon(name='Blinding Blade', base=float('inf'), bonus=float('inf'))
        self.armor = Armor(name='Studded Leather', base=float('inf'), bonus=float('inf'))

def random_monster():
    '''generate a monster at random

    create an instance of each monster here, then add that instance to
    the listOfMonsters.  The function will pick a random instance out of
    the list, then return it to the caller.'''
    
    monster = Monster()
    orc = Orc()
    chicken = Chicken()
    raider = Raider()
    leader = CultFanatic()
    avatar = Avatar()
    
    listOfMonsters = [monster, orc, chicken, raider, leader, avatar]
    return choice(listOfMonsters)


if __name__ == "__main__":

    Grr = Monster(name = "Freddy")
    Randy = random_monster()
    print(Randy.name)



