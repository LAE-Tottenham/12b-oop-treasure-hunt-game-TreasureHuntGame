import random
from reusables import generateDictionary
from enemies import Boss_Enemy

class Battle:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy
        self._playTurnOver = False
        self._enemyTurnOver = False
    
    def playerTurn(self):
        while self._playTurnOver == False:
            self._player.isDefending = False
            choice_dict = generateDictionary(["Basic Attack", "Special Attack", "Defend", "Open Inventory", "Flee"])
            print("Would you like to:")
            for option in choice_dict:
                print(f"({option}) {choice_dict[option]}")
            decision = ""
            while decision != "1" and decision != "2" and decision != "3" and decision != "4" and decision != "5":
                decision = input()
            
            if decision == "1": #Basic attack
                self._playTurnOver = self._player.basic_attack(self._enemy)
                self._enemyTurnOver = False
            elif decision == "2": #Special attack
                self._playTurnOver = self._player.special_attack(self._enemy)
                self._enemyTurnOver = False
            elif decision == "3": #Defend
                self._playTurnOver = self._player.defend()
                self._enemyTurnOver = False
            elif decision == "4": #Open Inventory (e.g. for healing items)
                self._player.open_inventory()
                self._enemyTurnOver = False
            elif decision == "5": #Flee
                input("You decided to flee.")
                self._player._currentlocation.get_summary(self._player)
            
        if self._enemy._isAlive == False:
            self._player._currentlocation.get_summary(self._player) 
        self._enemyTurnOver = False
        self.enemyTurn()
    
    def enemyTurn(self):
        while self._enemyTurnOver == False:
            if isinstance(self._enemy, Boss_Enemy) == True:
                self._enemy._isDefending = False
                choice = str(random.randint(1, 3))
                if choice == "1": #basic attack
                    self._enemyTurnOver = self._enemy.attack(self._player)
                elif choice == "2": #special atack
                    self._enemyTurnOver = self._enemy.special_attack(self._player)
                elif choice == "3": #defend
                    self._enemyTurnOver = self._enemy.defend()
            
            else:
                self._enemyTurnOver = self._enemy.attack(self._player)
        self._playTurnOver = False
        self.playerTurn()