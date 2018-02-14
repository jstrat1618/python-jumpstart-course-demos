import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level #The names attributes don't have to match the parameters

    def __repr__(self):
        return "Creature of name {} and level {}".format(self.name, self.level)

    def get_roll(self):
        roll = random.randint(1,12)*self.level
        return roll


class Wizard(Creature):
    def attack(self, creature):
        print("The wizard {} is attacking the {}!".format(self.name, creature.name))

        # We will roll a 12 sided die and multiply it by the level
        # The number with the highest number wins
        my_roll = random.randint(1, 12) * self.level
        #creature_roll = random.randint(1, 12) * creature.level
        creature_roll = self.get_roll()

        print("{} rolled a {}".format(self.name, my_roll))
        print("The {} rolled a {}".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("{} has triumphed over the {}".format(self.name, creature.name))
            return True
        else:
            print("{} was defeated :( ".format(self.name))
            return False

class SmallAnimal(Creature):
    def get_roll(self):
        roll = super().get_roll()
        return roll/2

class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, the_level=level)
        self.breathes_fire = breathes_fire
        self.scaliness = scaliness

    def get_roll(self):
        fire_modifier = 5 if self.breathes_fire else 1
        roll = super().get_roll()*fire_modifier*self.scaliness/10
        return roll







