from reusables import movementChoices, generateDictionary
import time, story
from items import Healing

class Player:
    def __init__(self, name, currentlocation):
        self.name = name
        self._currentlocation = currentlocation
        self._totalEnergy = 20
        self._currentEnergy = 20
        self._baseHP = 100
        self._armourBuff = 0
        self._TotalHP = self._baseHP + self._armourBuff
        self._currentHP = self._TotalHP
        self._baseStrength = 3
        self._damageBuff = 0
        self._TotalDamage = self._baseStrength + self._damageBuff
        self._inventory = []
        self._keyItemInventory = []
        self._funds = 100
        self._level = 1
        self._XP = 0
        self._equippedWeapon = ""
        self._equippedArmour = ""
        self.currentQuest = ""
        self._isAlive = True
        self._isDefending = False
        self._fastTravelLocations = []
    
    def add_fast_travel_location(self, location): #purely for set up
        self._fastTravelLocations.append(location)
    
    def get_summary(self): #might cut the XP from this if it's too complicated to impliment
        if self._equippedArmour != "":
            armourName = self._equippedArmour._name
        else:
            armourName = "None"
        if self._equippedWeapon != "":
            weaponName = self._equippedWeapon._name
        else:
            weaponName = "None"
        if self.currentQuest != "":
            questName = self.currentQuest.title
        else:
            questName = "None"
        input(f'''
              Name: {self.name}
              Current HP: {self._currentHP} / {self._baseHP}(+{self._armourBuff})
              Current Energy: {self._currentEnergy} / {self._totalEnergy}
              Strength: {self._baseStrength} (+{self._damageBuff})
              Money: {self._funds}
              Level: {self._level}
              XP: {self._XP}
              Current Quest: {questName}
              Equipped Weapon: {weaponName}
              Equipped Armour: {armourName}''')

    def set_totalDamage(self):
        self._TotalDamage = self._baseStrength + self._damageBuff

    def set_totalHP(self):
        self._TotalHP = self._baseHP + self._armourBuff
    
    def set_currentHP(self):
        if (self._currentHP >= self._baseHP):
            self._currentHP = self._baseHP + self._armourBuff
        elif (self._currentHP < self._baseHP):
            self._currentHP = self._currentHP + self._armourBuff

    def move(self):
        currentdict = generateDictionary(self._currentlocation._connectedAreas)
        movementChoices(currentdict, self)
    
    def pick_up(self, new_item):
        if new_item._type.upper() == "KEY":
            self._keyItemInventory.append(new_item)
            input(f"'{new_item._name}' has been added to Key Inventory")
        
        else:
            if len(self._inventory) == 10:
                choice = input(f"Your rucksack is full. Would you like to replace an item with {new_item._name}? (Y/N) ")

                if choice.upper() == "Y":
                    print("INVENTORY:")
                    for item in self._inventory:
                        print(item._name)

                    print("WARNING: Any item dropped in a shop will likely be sold off before you find it again. (Items dropped in shops will be lost forever.)")
                    dropped = input("Please type the name of the object you would like to drop, or press ENTER to cancel: ")

                    selected = ""
                    for item in self._inventory:
                        verify = item._name.upper()
                        if ((dropped.upper() == verify) == True):
                            selected = item
                            break
                    
                    if selected != "":

                        print(f"Are you sure you would like to drop {selected._name}? (Y/N)")
                        selected.get_summary()
                        choice = input()

                        if choice.upper() == "Y":
                            self._inventory.remove(selected)
                            self._inventory.append(new_item)
                            print(f"'{selected._name}' was dropped.")
                            input(f"'{new_item._name}' has been added to your inventory.")
                        else:
                            input(f"You chose to leave {new_item._name} behind.")
                    else:
                        input(f"You chose to leave {new_item._name} behind.")
                else:
                    input(f"You chose to leave {new_item._name} behind.")
            
            else:
                self._inventory.append(new_item)
                input(f"'{new_item._name}' has been added to your inventory.")
    
    def takeDamage(self, damage):
        if self._isDefending == True:
            damage = int(((damage*0.4)//1)+1)
            self._isDefending = False
        
        self._currentHP = self._currentHP - damage
        print(f"-{damage} HP")
        print(f"HP Remaining: {self._currentHP}")
        input()

        if self._currentHP <= 0:
            print("You have died.")
            self._isAlive = False
            input()
            for i in range (3):
                print(".")
                time.sleep(1)
            input("...Looks like your family will get to say 'I told you so' after all.")
            exit()
    
    def long_rest(self):
        if self._currentlocation._hostile == False:
            input("Energy and HP have been restored!")
            self._currentHP = self._TotalHP
            self._currentEnergy = self._totalEnergy
        else:
            input("Cannot rest in a hostile area.")
        self._currentlocation.get_summary(self)
    
    def get_XP(self, amount):
        self._XP = self._XP + amount
        input(f"+{amount} XP")
        #a dictionary in the form XP required : level
        level_dict = {0 : 1,
                      100 : 2,
                      200: 3,
                      300: 4,
                      400: 5,
                      500: 6,
                      600 : 7,
                      700 : 8,
                      800: 9,
                      900: 10}
        prev_lvl = self._level

        for xpValue in level_dict:
            if self._XP >= xpValue:
                new_lvl = level_dict[xpValue]
        
        if new_lvl != prev_lvl:
            input("You have levelled up!")
            input(f"Level: {new_lvl}")
            self._level = new_lvl
            self._TotalHP += 15
            input("+5 Max. HP")
            self._totalEnergy += 5
            input("+15 Max Energy")
            self._baseStrength += 15
            input("+15 Strength")
        
    
    def get_money(self, amount):
        input(f"+{amount} Gold")
        self._funds += amount
        if self._funds >= 15000000:
            input("Looking at your wallet, you notice that you seemed to have already made a fortune of your own. What's the point of risking your life like this if you've already got the savings for a more than happy retirement?")
            choosing = input("Return home to brag to your family's faces? (Ending 5/5) (Y/N) ")
            while choosing not in ["Y", "y", "n", "N"]:
                choosing = input()
            story.secret_ending(choosing)
    
    def defend(self):
        input("You used 'defend'.")
        self._isDefending = True
        return True

    def basic_attack(self, enemy):
        print(f"You used 'slash' on {enemy._name}")
        enemy.takeDamage(self._TotalDamage, self)
        return True
    
    def special_attack(self, enemy):
        if self._currentEnergy >= 3:
            print(f"You used 'cleave' on '{enemy._name}' (-3 Energy)")
            print(f"Remaining Energy: {self._currentEnergy}")
            self._currentEnergy -= 3
            enemy.takeDamage(self._TotalDamage*2, self)
            return True #when running battle-type actions, run them like turnOver = special_attack(enemyName) so in the battle class, it'll be like while turnOver = False: and so on with an option screen of what the player can do
        else:
            print("You don't have enough energy to use this move.")
            return False
        
    def fast_travel(self):
        fast_dict = generateDictionary(self._fastTravelLocations)
        movementChoices(fast_dict, self)

    def drop_item(self, item):
        self._inventory.remove(item)
        if self._equippedArmour == item or self._equippedWeapon == item:
            item.toggle_equip(self)
        input(f"You have dropped '{item._name}'.")
        if self._currentlocation._shop == False:
            self._currentlocation._interactables_objects.append(item)
    
    def open_inventory(self):
        temp_list = self._keyItemInventory + self._inventory
        if len(temp_list) == 0:
            print("Inventory Is Empty.")
        if len(self._keyItemInventory) != 0:
            print("KEY INVENTORY:")
            for object in self._keyItemInventory:
                print(object._name)
        if len(self._inventory) != 0:
            print("INVENTORY:")
            for item in self._inventory:
                print(item._name)
        
        item_dict = generateDictionary(temp_list)

        options = generateDictionary(["View Item Details/Consume Health Item", "Drop An Item", "Equip/Unequip Item", "Close Inventory"])
        for option in options:
            print(f"({option}) {options[option]}")
        print("WARNING: Any item dropped in a shop will likely be sold off before you find it again. (Items dropped in shops will be lost forever.)")
        choice = input()

        if choice == "1" or choice == "2" or choice == "3":
            if len(temp_list) == 0:
                input("Inventory Is Empty")

            else:
                for number in item_dict:
                    print(f"({number}) {item_dict[number]._name}")
                
                chosen = input("Please enter the number of an item: ")
                chosenItem = ""

                while chosenItem == "":
                    try:
                        chosenItem = item_dict[chosen]
                    except KeyError:
                        chosen = input("Please enter a valid number: ")
                
                if choice == "1": #Get summary
                    chosenItem.get_summary()
                    if isinstance(chosenItem, Healing) == True:
                        chosenItem.consume(self)
                
                elif choice == "2": #Drop Item
                    if chosenItem._type.upper() == "KEY":
                        input("Cannot drop a key item.")
                    else:
                        self.drop_item(chosenItem)
                
                elif choice == "3":
                    chosenItem.toggle_equip(self)
        
        else:
            input("Closed inventory")