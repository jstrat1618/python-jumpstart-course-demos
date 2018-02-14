import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon

def main():
    #print header
    print_header()
    #run game loop
    game_loop()


def print_header():
    print("------------------------------------------")
    print("               WIZARD GAME APP ")
    print("------------------------------------------")

def game_loop():
    creatues = [SmallAnimal("Toad", 1),
                Creature("Tiger",12 ),
                SmallAnimal("Bat",3),
                Dragon("Dragon", 50, scaliness=75, breathes_fire=True),
                Wizard("Evil Wizard", 1000)
                ]


    hero = Wizard("Gandolf", 75)

    while True:
        active_creature = random.choice(creatues)

        print("A {} of level {} has appeared from a dark and foggy forest...."
              .format(active_creature.name, active_creature.level))

        cmd = input("Do you [a]ttack, [r]un away, [l]ook around or [e]xit? ")
        cmd = cmd.strip().lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatues.remove(active_creature)
            else:
                print("The wizard {} hides to recover".format(hero.name))
                time.sleep(3)
                print("The wizard {} returns revitalized!".format(hero.name))
        elif cmd == 'r':
            print('The wizard is unsure of his power and runs away.')
        elif cmd == 'l':
            print("The wizard {} looks around and sees: ".format(hero.name))
            for c in creatues:
                print("A {} of level {}".format(c.name, c.level))

        elif cmd == 'e':
            break
        else:
            print("Sorry, we didn't understand that command")

        if not creatues:
            print("{} has triumphed over all the creatures!!".format(hero.name))
            print()
            print("You win!!!")
            break




if __name__ == '__main__':
    main()