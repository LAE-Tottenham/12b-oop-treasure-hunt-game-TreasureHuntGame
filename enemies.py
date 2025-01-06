import story

class Enemies:
    def __init__(self, name, type, hp, attackDmg, gold, xp):
        self._name = name
        self._type = type
        self._HP = hp
        self._attackDamage = attackDmg
        self._Reward_Gold = gold
        self._Reward_XP = xp
        self._isAlive = True
    
    def attack(self, player):
        print(f"'{self._name}' attacked '{player.name}'!")
        player.takeDamage(self._attackDamage)
        return True

    def takeDamage(self, damage, player):
        self._HP = self._HP - damage
        print(f"'{self._name}' has lost {damage} HP!")
        print(f"HP Remaining: {self._HP}")
        input()

        if self._HP <= 0:
            print(f"'{self._name}' has been slain!")
            player.get_XP(self._Reward_XP)
            player.get_money(self._Reward_Gold)
            self._isAlive = False
            if player.currentQuest != "":
                player.currentQuest.add_counter(self)
            if self in player._currentlocation._interactables_people:
                player._currentlocation._interactables_people.remove(self)

class Boss_Enemy(Enemies):
    def __init__(self, name, type, hp, attackDmg, gold, xp, item, special_damage, special_attack_name, world, ending):
        super().__init__(name, type, hp, attackDmg, gold, xp)
        self._KeyItem = item
        self._specialAttackDamage = special_damage
        self._specialAttackName = special_attack_name
        self._isDefending = False
        self._nextWorld = world
        self._ending = ending
    
    def takeDamage(self, damage, player):
        if self._isDefending == True:
            damage = int(((damage * 0.3)//1+1))
            self._isDefending = False

        self._HP = self._HP - damage
        print(f"'{self._name}' took {(damage)} damage!")
        print(f"HP Remaining: {self._HP}")
        input()
        
        
        if self._HP <= 0:
            print(f"'{self._name}' has been slain!")
            self._isAlive = False
            if player.currentQuest != "":
                player.currentQuest.add_counter(self)
            input()

            print(f"Congratulations! You have acquired '{self._KeyItem._name}'!")
            player.pick_up(self._KeyItem)
            if isinstance(self._nextWorld, str) != False:
                self._nextWorld.unlock(player, self._KeyItem)
            player.get_XP(self._Reward_XP)
            player.get_money(self._Reward_Gold)
            if self._ending == 1:
                input("Huh... Looks like you've already got some treasure. Maybe this could be enough to impress your family?")
                ending = input("Go back home? (Ending 1/5) (Y/N) ")
                while ending.upper() != "Y" and ending.upper() != "N":
                    ending = input()
                story.ending_one(ending)
            elif self._ending == 2:
                input("Well, that makes more treasure to show off. Do you really have to do this another two times?")
                ending = input("Go back home? (Ending 2/5) (Y/N) ")
                while ending.upper() not in ["Y", "N"]:
                    ending = input()
                story.ending_two(ending)
            elif self._ending == 3:
                input("That makes three... You sure you really wanna keep going?")
                ending = input("Go back home? (Ending 3/5) (Y/N) ")
                while ending.upper() not in ["Y", "N"]:
                    ending = input()
                story.ending_three(ending)
            elif self._ending == 4:
                input("Finally... It's about time!")
                input("Back home we go!")
                story.ending_four()
            self._KeyItem = ""
            if self in player._currentlocation._interactables_people:
                player._currentlocation._interactables_people.remove(self)
            input()


    def special_attack(self, player):
        print(f"'{self._name}' used {self._specialAttackName} on '{player.name}")
        player.takeDamage(self._specialAttackDamage)
        return True
    
    def defend(self):
        input(f"{self._name} used 'defend'!")
        self._isDefending = True