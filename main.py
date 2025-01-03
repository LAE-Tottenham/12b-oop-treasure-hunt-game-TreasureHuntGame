import random, time, story, pyfiglet
#install pyfiglet first

def playerMenu(player, self):
    if player.currentQuest == "":
        dictionary = generateDictionary(["View Self Info", "View Inventory", "Cancel"])
    else:
        dictionary = generateDictionary(["View Self Info", "View Inventory", "Cancel", "View Quest Details"])

    print("Would you like to: ")
    for option in dictionary:
        print(f"({option}) {dictionary[option]}")
    choice = str(input())
    
    if player.currentQuest == "":
        while choice != "1" and choice != "2" and choice != "3":
            choice = str(input())
    
    else:
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = str(input())

    if choice == "1": #Self Info
        player.get_summary()
        self.get_summary(player)
    
    elif choice == "2": #Inventory
        player.open_inventory()
        self.get_summary(player)

    elif choice == "3": #Cancel
        self.get_summary(player)
    
    elif choice == "4" and player.currentQuest != "": #Quest Details
        player.currentQuest.show_details(player)
        self.get_summary(player)

def generateDictionary(list):
    currentdict = {} #This refers to the dictionary of options (e.g. locations, items, etc)
    i = []
    j = 0
    for x in range (len(list)): #Forms numbered options for the dictionary for the amount of items in the list
        j = j + 1
        i.append(str(j))

    position = 0
    for value in i: #Assigns the different numbers to certain different options in the list
        currentdict[value] = list[position]
        position = position + 1
    
    return currentdict

def movementChoices(currentdict, self):
    print("Would you like to travel to:")
    for option in currentdict:
        lock = ""
        if currentdict[option]._locked == True:
            lock = "[LOCKED]"
        print(f"({option}) {currentdict[option].name} {lock}")
    print("(Press 'enter' to cancel)")
    choice = input()

    try:
        location = currentdict[choice]
    except KeyError:
        location = ""
    
    if isinstance(location, Place) == True:
        if location._locked == True:
            input(f"Cannot travel to {location.name}")
        
        else:
            choice = input(f"Travel to {location.name}? (Y/N) ")
            if choice.upper() == "Y":
                story.os.system('clear')
                travel = "Travelling"

                for i in range (3):
                    print(travel + ".")
                    travel = travel + "."
                    time.sleep(1)
                    story.os.system('clear')
                
                input(f"You have travelled to {location.name}")
                self._currentlocation = location
        
            else:
                input("Cancelled")
        
    else:
        input("Cancelled")
    self._currentlocation.get_summary(self)

#################################################### Classes ##########################################################
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
        i = [1, 2, 3, 4] #There will only be 4 places you can fast travel to
        locations = [world1, world2, world3, world4]
        fast_dict = {} #Dictionary of fast travel locations
        position = 0
        for item in i:
            fast_dict[str(item)] = locations[position]
            position += 1
        
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

        options = generateDictionary(["View Item Details", "Drop An Item", "Equip/Unequip Item", "Close Inventory"])
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
        
                
class Place:
    def __init__(self, name, locked, objects, fast_travel, hostile, shop, people):
        self.name = name
        self._connectedAreas = []
        self._locked = locked
        self._interactables_objects = objects #maybe use this list to incorporate the tree idea you had from the interview
        self._interactables_people = people #can add monsters to this list in hostile places
        self._canFastTravel = fast_travel
        self._hostile = hostile
        self._shop = shop
    
    def add_connected_area(self, location):
        self._connectedAreas.append(location)
    
    def open_shop(self, player):
        sell_buy = input("Please enter 'sell' to sell items, 'buy' to buy items, or press 'enter' to cancel: ")
        
        if sell_buy.upper() == "BUY":
            if len(self._interactables_objects) == 0:
                input("This shop is out of stock.")
                self.get_summary(player)

            for item in self._interactables_objects:
                item.get_summary()
                print(f"Priced At {self._interactables_objects[item]} Gold")
            print("Please enter the name of the object you would like to buy, or press 'enter' to close the shop: ")
            choice = input()
            item = ""
            for object in self._interactables_objects:
                if choice.upper() == object._name.upper():
                    item = object
            try:
                price = self._interactables_objects[item]
            except KeyError:
                pass

            if item == "":
                print("Cancelled.")
            else:
                if player._funds - price < 0:
                    print("You can't afford this item.")
                    print(f"Current Gold: {player._funds}")
                    print("Purchase Cancelled.")
                    input()
                else:
                    print(f"Current Gold: {player._funds}")
                    verify = input(f"Purchase {item._name} for {price} Gold? It's recommended that you ensure you have space in your inventory first. (Y/N) ")
                    if verify.upper() == "Y":
                        player._funds -= price
                        player.pick_up(item)
                        del self._interactables_objects[item]
                    else:
                        print("Transaction cancelled.")
        
        elif sell_buy.upper() == "SELL":
            item_dict = generateDictionary(player._inventory)
            for item in item_dict:
                print(f"({item}) {item_dict[item]._name}")
            sold = input("Please enter the number of the item you would like to sell, or press 'enter' to cancel: ")
            soldItem = ""

            try:
                soldItem = item_dict[sold]
            except KeyError:
                sold = ""
            
            if sold == "":
                print("Transaction Cancelled")
            else:
                verify = input(f"Sell {soldItem._name} for {soldItem._sell_price} Gold? (Y/N) ")
                if verify.upper() == "Y":
                    player._inventory.remove(soldItem)
                    print(f"Sold {soldItem._name}")
                    player.get_money(soldItem._sell_price)
        self.get_summary(player)

    
    def get_summary(self, player):
        story.os.system('clear')
        print(pyfiglet.figlet_format(self.name, font = "3d-ascii", width = 150))
        print(f"You are currently in {self.name}.")
        print("At the moment, you can do the following:")

        if self._hostile == False: #The basic options for safe areas

            if self._shop == False: #Changes depending on if its a shop or not
                current_dict = generateDictionary(["Go Somewhere Else","Search For Items","Talk To The Locals", "Long Rest", "Menu"])
            else:
                current_dict = generateDictionary(["Go Somewhere Else", "Shop For Items", "Talk To The Locals", "Long Rest", "Menu"])

            for item in current_dict:
                print(f"({item}) {current_dict[item]}")
            choice = str(input())
            while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
                print("Please choose from the provided options.") #Player has to choose one of the options
                choice = str(input())
            
            if choice == "1": #Go somewhere else
                fast_travel = False
                if self._canFastTravel == True: #Choose if they're going to fast travel or not
                    option = input("Would you like to fast travel somewhere else? (Y/N) ")
                    if option.upper() == "Y":
                        fast_travel = True
                else:
                    pass

                if fast_travel == False:
                    player.move()
                else:
                    player.fast_travel()
            
            elif choice == "2" and self._shop == False: #Search for items (shop = false)
                if len(self._interactables_objects) != 0:
                    print("While searching for items, you find the following: ")
                    for item in self._interactables_objects:
                        print(item._name)
                    print("Would you like to pick any of them up? (Y/N) ")
                    choice = input()
                    if choice.upper() == "Y":
                        current_dict = generateDictionary(self._interactables_objects)
                        for thing in current_dict:
                            print(f"({thing}) {current_dict[thing]._name}")
                        chosen = input()
                        item = ""
                        while item == "":
                            try:
                                item = current_dict[chosen]
                            except KeyError:
                                chosen = input("Please input the number of the item you'd like to grab: ")
                        player.pick_up(item)
                        pickedUp = False
                        for entity in player._inventory:
                            if item == entity:
                                pickedUp = True
                                break
                        
                        if pickedUp == True:
                            self._interactables_objects.remove(item)

                        self.get_summary(player)
                    else:
                        self.get_summary(player)
                else:
                    input("It seems like there aren't any items here...")
                    self.get_summary(player)
            
            elif choice == "2" and self._shop == True: #Shop for items
                self.open_shop(player)
            
            elif choice == "3": #Talk to the locals
                if len(self._interactables_people) != 0:
                    print("Looking around, you meet the following people: ")
                    for people in self._interactables_people:
                        print(people._name)
                    print("Would you like to talk to any of them? (Y/N) ")
                    choice = input()
                    if choice.upper() == "Y":
                        current_dict = generateDictionary(self._interactables_people)
                        for person in current_dict:
                            print(f"({person}) {current_dict[person]._name}")
                        chosen = input()
                        person = ""
                        while person == "":
                            try:
                                person = current_dict[chosen]
                            except KeyError:
                                chosen = input("Please input a valid option: ")
                        
                        person.talk(player)
                    else:
                        self.get_summary(player)
                else:
                    input("Seems like there's nobody here...")
                    self.get_summary(player)
            
            elif choice == "4": #Long Rest
                player.long_rest()
            
            elif choice == "5": #Menu
                playerMenu(player, self)
        
        else: #Basic options for hostile areas
            current_dict = generateDictionary(["Go Somewhere Else", "Search For Items", "Look For Monsters", "Menu"])
            for option in  current_dict:
                print(f"({option}) {current_dict[option]}")
            choice = input()
            while choice != "1" and choice != "2" and choice != "3" and choice != "4":
                choice = input("Please choose from the above list: ")
            
            if choice == "1": #Go Somewhere Else
                player.move()
            
            elif choice == "2": #Search For Items
                if len(self._interactables_objects) != 0 and len(self._interactables_people) != 0:
                    temp_list = self._interactables_objects + self._interactables_people
                    found = random.choice(temp_list)

                    if isinstance(found, Boss_Enemy) == True:
                        print(f"Uh oh! Looks like the {found._name} noticed you!")
                        input(f"You've entered a battle with '{found._name}'.")
                        fight = Battle(player, found)
                        fight.playerTurn()
                    elif isinstance(found, Enemies) == True and isinstance(found, Boss_Enemy) == False:
                        print(f"Uh oh! It looks like you disturbed a monster while they were sleeping!")
                        input(f"You've entered a battle with '{found._name}'.")
                        fight = Battle(player, found)
                        fight.playerTurn()
                    elif isinstance(found, Healing) == True:
                        input("Oh! It looks like you found something!")
                        found.get_summary()
                        choose = input("Would you like to pick this up? (Y/N) ")
                        while choose.upper() != "Y" and choose.upper() != "N":
                            choose = input()
                        if choose.upper() == "Y":
                            player.pick_up(found)
                            self._interactables_objects.remove(found)
                        else:
                            input(f"You chose to leave {found._name} where it was.")
                        self.get_summary(player)
                
                else:
                    input("Seems like you couldn't find anything...")
                    self.get_summary(player)
                
            elif choice == "3": #Look for monsters
                if len(self._interactables_people) != 0:
                    monster_dict = generateDictionary(self._interactables_people)
                    print("After scouting the area, you see the following:")
                    for monster in monster_dict:
                        print(monster_dict[monster]._name)
                    choose = input("Would you like to fight one? (Y/N) ")
                    while choose.upper() != "Y" and choose.upper() != "N":
                        choose = input()
                    
                    if choose.upper() == "Y":
                        for mob in monster_dict:
                            print(f"({mob}) {monster_dict[mob]._name}")
                        
                        target = input("Please enter the number of a monster: ")
                        chosenTarget = ""

                        while chosenTarget == "":
                            try:
                                chosenTarget = monster_dict[target]
                            except KeyError:
                                target = input("Please enter a valid number: ")
                        
                        fight = Battle(player, chosenTarget)
                        fight.playerTurn()
                    else:
                        self.get_summary(player)
                else:
                    input("It seems like there are no more monsters in this area...")
                    self._hostile = False
                    self.get_summary(player)
                
            elif choice == "4": #Menu
                playerMenu(player, self)



    
    def unlock(self, player, keyItem):
        if keyItem in (player._keyItemInventory):
            input(f"You can now travel to '{self.name}'!")
            self._locked = False

class Item:
    def __init__(self, name, equippable, sell_price, type):
        self._name = name
        self._equippable = equippable
        self.equipped = False
        self._sell_price = sell_price
        self._type = type
    
    def get_summary(self):
        if isinstance(self, Weapon_Armour) == False and isinstance(self, Healing) == False:
            input(f'''
                Item: {self._name}
                Equippable: {self._equippable}
                Equipped: {self.equipped}
                Sell Price: {self._sell_price}
                Type: {self._type}''')
        else:
            print(f'''
                Item: {self._name}
                Equippable: {self._equippable}
                Equipped: {self.equipped}
                Sell Price: {self._sell_price}
                Type: {self._type}''')
    
    def toggle_equip(self, player):
        if self._equippable == True and (isinstance(self, Weapon_Armour) == True):
            if player._equippedArmour == self:
                player._equippedArmour = ""
                player._armourBuff = 0
                player.set_totalHP()
                player.set_currentHP()
                input(f"Unequipped '{self._name}")
            
            elif player._equippedWeapon == self:
                player._equippedWeapon = ""
                player._damageBuff = 0
                player.set_totalDamage()
                input(f"Unequipped {self._name}")
            
            else:
                if player._level >= self._minimumLvl:

                    if self._type.upper() == "WEAPON":
                        player._equippedWeapon = self
                        input(f"You have equipped '{self._name}'")
                        player._damageBuff = self._buff
                        player.set_totalDamage()
                    elif self._type.upper() == "ARMOUR":
                        player._equippedArmour = self
                        input(f"You have equipped '{self._name}'")
                        player._armourBuff = self._buff
                        player.set_totalHP()
                        player.set_currentHP()
                else:
                    input("Your level is too low!")
        else:
                input("This item cannot be equipped.")
            

class Weapon_Armour(Item):
    def __init__(self, name, equippable, sell_price, type, buff, minimum):
        super().__init__(name, equippable, sell_price, type)
        self._buff = buff
        self._minimumLvl = minimum
    
    def get_summary(self):
        super().get_summary()
        if self._type.upper() == "WEAPON":
            print(f'''              Damage buff: {self._buff}''')
        elif self._type.upper() == "ARMOUR":
            print(f'''              Health buff: {self._buff}''')
        input(f'''              Minimum Level Required: {self._minimumLvl}''')

class Healing(Item):
    def __init__(self, name, equippable, sell_price, type, health, energy):
        super().__init__(name, equippable, sell_price, type)
        self._healingPower = health
        self._energyRestored = energy

    def get_summary(self):
        super().get_summary()
        if self._type.upper() != "POTION":
            print(f"              Energy Restored: +{self._energyRestored} Energy")
        else:
            pass

        input(f"              Healing Ability: +{self._healingPower} HP")

    def consume(self, player):
        choice = input(f"Consume {self._name}? (Y/N) ")
        if choice.upper() == "Y":
            if (player._currentHP + self._healingPower) >= player._TotalHP:
                player._currentHP = player._TotalHP
                print(f"{player.name} has been restored to full health!")
            elif (player._currentHP + self._healingPower) < player._TotalHP:
                player._currentHP = player._currentHP + self._healingPower
                print(f"+{self._healingPower} HP")
            input(f"Current HP: {player._currentHP}")

            if self._type.upper() != "POTION":
                if (player._currentEnergy + self._energyRestored) >= player._totalEnergy:
                    player._currentEnergy = player._totalEnergy
                    print("You have been restored to full energy!")
                else:
                    player._currentEnergy += self._energyRestored
                    print(f"+{self._energyRestored} Energy")
                input(f"Current Energy: {player._currentEnergy}")
            player._inventory.remove(self)
        else:
            pass

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
            if isinstance(self._nextWorld, Place):
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
    
class NPC:
    def __init__(self, name, hasQuest, quest, lines):
        self._name = name
        self._lines = lines #Ensure lines are input in order
        self._hasQuest = hasQuest
        self._quest = quest
    
    def talk(self, player):
        if player.currentQuest != self._quest:
            for line in self._lines:
                input(f"'{line}'")
        else:
            input("'Thanks for agreeing to help!'")
        
        if self._hasQuest == True and self._quest._complete == False and player.currentQuest != self._quest:
            print("'Would you help me with my problem?'")
            self._quest.show_details(player)
            choice = input("Accept Quest? (Y/N) ")

            if choice.upper() == "Y":
                self.grant_quest(player)
            
            else:
                pass
        
        if self._quest == player.currentQuest:
            self.complete_quest(player)
        
        player._currentlocation.get_summary(player)
    
    def grant_quest(self, player):
        accept = True
        if player.currentQuest != "":
            choice = input("Warning: Accepting this quest will override your previous quest. Are you sure? (Y/N) ")
            if choice.upper() == "N":
                accept = False
        else:
            pass

        if accept == True and self._quest._complete == False:
            print(f"You have accepted {self._name}'s quest!")
            player.currentQuest = self._quest
            time.sleep(1)
        elif accept == True and self._quest._complete == True:
            print(f"{self._name}'s quest has already been completed.")
            time.sleep(1)
        else:
            print("Cancelled")
    
    def complete_quest(self, player):
        if player.currentQuest == self._quest:
            self._quest.check_completed()

            if self._quest._complete == True:
                print(f"'Thank you so much help!'")
                self._quest.grant_rewards(player)
                self._lines = ["Thank you so much for your help!"]
                player.currentQuest = ""
            
            else:
                input("Quest incomplete.")
        
        else:
            input(f"You don't have a quest from {self._name}.")
        player._currentlocation.get_summary(player)
        

class Quest:
    def __init__(self, title, conditions, type, item, xp, gold, current, required):
        self.title = title
        self._clearCondtion = conditions
        self._specifiedType = type
        self._reward_Item = item
        self._reward_XP = xp
        self._reward_Gold = gold
        self._currenCount = current
        self._requiredCount = required
        self._complete = False
    
    def show_details(self, player):
        print(f'''
              '{self.title}'
              {self._clearCondtion}
              Rewards:
              +{self._reward_XP} XP
              +{self._reward_Gold} Gold
              Acquire '{self._reward_Item._name}' ''')

        if player.currentQuest == self:
            input(f"              Currently Slain: {self._currenCount} / {self._requiredCount}")
        else:
            pass
        
        print()
        choice = input(f"See summary of '{self._reward_Item._name}'? (Y/N) ")
        if choice.upper() == "Y":
            self._reward_Item.get_summary()
        else:
            pass
        
    
    def grant_rewards(self, player):
        player.pick_up(self._reward_Item)
        player.get_XP(self._reward_XP)
        player.get_money(self._reward_Gold)
        
    def check_completed(self):
        if self._currenCount >= self._requiredCount:
            self._complete = True
        else:
            pass
    
    def add_counter(self, enemy):
        if enemy._type == self._specifiedType:
            self._currenCount += 1
        else:
            pass

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


##############################################################
# #Most if not all of these names are from random generators
treasure1 = Item("Goblin Crown", False,  2500000, "Key")
treasure2 = Item("Skull of Knowledge", False, 5000000, "Key")
treasure3 = Item("The Queen's Jewels", False, 7500000, "Key")
treasure4 = Item("Spider Eye", False, 10000000, "Key")
###############World 1 Items##################
shop1_potion1 = Healing("Potion", False, 20, "Potion", 20, 0)
shop1_potion2 = Healing("Potion", False, 20, "Potion", 20, 0)
shop1_consumable1 = Healing("Bread", False, 15, "Food", 10, 10)
shop1_consumable2 = Healing("Water", False, 15, "Drink", 10, 10)
shop1_weapon = Weapon_Armour("Wooden Sword", True, 100, "Weapon", 10, 1)
shop1_armour = Weapon_Armour("Cloth Armour", True, 100, "Armour", 15, 1)
mob1_consumable1 = Healing("Berries", False, 10, "Food", 10, 5)
mob1_consumable2 = Healing("Apples", False, 12, "Food", 17, 12)
boss1_consumable = Healing("Brew", False, 30, "Drink", 30, 15)
world1quest_armour = Weapon_Armour("Scrap Amour", True, 150, "Armour", 25, 1)
world1quest_weapon = Weapon_Armour("Gold Sword", True, 150, "Weapon", 15, 1)
##############World 1 Items^^^^################################################
##############World 2 Items#####################################
shop2_potion1 = Healing("Potion", False, 20, "Potion", 20, 0)
shop2_potion2 = Healing("Potion", False, 20, "Potion", 20, 0)
shop2_consumable1 = Healing("Bread", False, 15, "Food", 10, 10)
shop2_consumable2 = Healing("Water", False, 20, "Drink", 10, 10)
shop2_weapon = Weapon_Armour("Iron Sword", True, 200, "Weapon", 30, 3)
shop2_armour = Weapon_Armour("Chainmail Armour", True, 200, "Armour", 35, 3)
mob2_consumable1 = Healing("Blackberries", False, 10, "Food", 10, 5)
mob2_consumable2 = Healing("Oranges", False, 12, "Food", 17, 12)
boss2_consumable = Healing("Hot Chocolate", False, 50, "Drink", 40, 25)
world2quest_armour = Weapon_Armour("Iron Armour", True, 250, "Armour", 45, 3)
world2quest_weapon = Weapon_Armour("Grass Sword", True, 250, "Weapon", 35, 3)
##############World 2 Items^^^^###############################################
##############World 3 Items##################################################
shop3_potion1 = Healing("Potion", False, 20, "Potion", 20, 0)
shop3_potion2 = Healing("Potion", False, 20, "Potion", 20, 0)
shop3_consumable1 = Healing("Bread", False, 15, "Food", 10, 10)
shop3_consumable2 = Healing("Water", False, 20, "Drink", 10, 10)
shop3_weapon = Weapon_Armour("Diamon Sword", True, 300, "Weapon", 50, 5)
shop3_armour = Weapon_Armour("Gold Armour", True, 300, "Armour", 55, 5)
mob3_consumable1 = Healing("Blueberries", False, 10, "Food", 10, 5)
mob3_consumable2 = Healing("Pears", False, 12, "Food", 17, 12)
boss3_consumable = Healing("Cookies", False, 70, "Food", 50, 35)
world3quest_armour = Weapon_Armour("Copper Armour", True, 350, "Armour", 65, 5)
world3quest_weapon = Weapon_Armour("Obsidian Sword", True, 350, "Weapon", 55, 5)
#############World 3 Items^^^^^##########################################
#############World 4 Items###########################################
shop4_potion1 = Healing("Potion", False, 20, "Potion", 20, 0)
shop4_potion2 = Healing("Potion", False, 20, "Potion", 20, 0)
shop4_consumable1 = Healing("Bread", False, 15, "Food", 10, 10)
shop4_consumable2 = Healing("Water", False, 20, "Drink", 10, 10)
shop4_weapon = Weapon_Armour("Ice Sword", True, 400, "Weapon", 70, 7)
shop4_armour = Weapon_Armour("Obsidian Armour", True, 400, "Armour", 75, 7)
mob4_consumable1 = Healing("Strawberries", False, 10, "Food", 10, 5)
mob4_consumable2 = Healing("Bananas", False, 12, "Food", 17, 12)
boss4_consumable = Healing("Chocolate", False, 90, "Food", 70, 45)
world4quest_weapon = Weapon_Armour("Magma Sword", True, 450, "Weapon", 75, 7)
#############World 4 Items^^^^^#############################################

##########Mobs##########
#World 1
goblin1 = Enemies("Goblin", "Goblin", (random.randint(30, 50)), (random.randint(10, 30)), (random.randint(60, 100)), 6)
goblin2 = Enemies("Goblin", "Goblin", (random.randint(30, 50)), (random.randint(10, 30)), (random.randint(60, 100)), 6)
goblin3 = Enemies("Goblin", "Goblin", (random.randint(30, 50)), (random.randint(10, 30)), (random.randint(60, 100)), 6)
goblin4 = Enemies("Goblin", "Goblin", (random.randint(30, 50)), (random.randint(10, 30)), (random.randint(60, 100)), 6)
goblin5 = Enemies("Goblin", "Goblin", (random.randint(30, 50)), (random.randint(10, 30)), (random.randint(60, 100)), 6)
#World 2
skeleton1 = Enemies("Skeleton", "Skeleton", (random.randint(50, 70)), random.randint(30, 50), (random.randint(100, 140)), 15)
skeleton2 = Enemies("Skeleton", "Skeleton", (random.randint(50, 70)), random.randint(30, 50), (random.randint(100, 140)), 15)
skeleton3 = Enemies("Skeleton", "Skeleton", (random.randint(50, 70)), random.randint(30, 50), (random.randint(100, 140)), 15)
skeleton4 = Enemies("Skeleton", "Skeleton", (random.randint(50, 70)), random.randint(30, 50), (random.randint(100, 140)), 15)
skeleton5 = Enemies("Skeleton", "Skeleton", (random.randint(50, 70)), random.randint(30, 50), (random.randint(100, 140)), 15)
#World 3
ant1 = Enemies("Ant", "Ant", (random.randint(80, 100,)), (random.randint(60, 70)), (random.randint(160, 200)), 20)
ant2 = Enemies("Ant", "Ant", (random.randint(80, 100,)), (random.randint(60, 70)), (random.randint(160, 200)), 20)
ant3 = Enemies("Ant", "Ant", (random.randint(80, 100,)), (random.randint(60, 70)), (random.randint(160, 200)), 20)
ant4 = Enemies("Ant", "Ant", (random.randint(80, 100,)), (random.randint(60, 70)), (random.randint(160, 200)), 20)
ant5 = Enemies("Ant", "Ant", (random.randint(80, 100,)), (random.randint(60, 70)), (random.randint(160, 200)), 20)
#World 4
spider1 = Enemies("Spider", "Spider", (random.randint(100, 120)), (random.randint(65, 75)), (random.randint(200, 240)), 25)
spider2 = Enemies("Spider", "Spider", (random.randint(100, 120)), (random.randint(65, 75)), (random.randint(200, 240)), 25)
spider3 = Enemies("Spider", "Spider", (random.randint(100, 120)), (random.randint(65, 75)), (random.randint(200, 240)), 25)
spider4 = Enemies("Spider", "Spider", (random.randint(100, 120)), (random.randint(65, 75)), (random.randint(200, 240)), 25)
spider5 = Enemies("Spider", "Spider", (random.randint(100, 120)), (random.randint(65, 75)), (random.randint(200, 240)), 25)
##############################
#Quests
world1quest1 = Quest("Clear Out", "Kill 5 goblins", "Goblin", world1quest_armour, 28, 100, 0, 5)
world1quest2 = Quest("Good Riddance", "Kill the goblin's leader", "Goblin Leader", world1quest_weapon, 28, 250, 0, 1)
world2quest1 = Quest("Skeletons In The Closet", "Kill 5 skeletons", "Skeleton", world2quest_armour, 38, 200, 0, 5)
world2quest2 = Quest("Old Sack of Bones", "Kill the skeleton's leader", "Skeleton Leader", world2quest_weapon, 38, 250, 0, 1)
world3quest1 = Quest("Exterminator", "Kill 5 ants", "Ant", world3quest_armour, 48, 300, 0, 5)
world3quest2 = Quest("Down With The Queen", "Kill the ant queen", "Ant Queen", world3quest_weapon, 58, 600, 0, 1)
world4quest = Quest("Eugh... Spiders...", "Kill 5 spiders", "Spider", world4quest_weapon, 68, 500, 0, 5)
##############################
#NPCs
lucy = NPC("Lucy", True, world1quest1, ["Hey! I've seen you around town recently!", "I noticed that you seem to be an adventurer, is there any chance you could help me out?", "Whenever I try to go outside of town, these annoying goblins keep trying to attack me!"])
filippos = NPC("Filippos", True, world1quest2, ["Oh! You're the one that's been fighting those goblins, aren't you?", "Well, there's actually this one giant goblin somewhere nearby...", "I've been wanting to explore, but I'm too afraid of running into it..."])
kahina = NPC("Kahina", True, world2quest1, ["Ah, you must be that adventurer that helped out with the goblin issue going on!", "Do you think you could help out with the skeletons too?", "I'm not really bothered by them, but whenever I let my dog out I'm always worried that he'll go running towards one and get hurt."])
leo = NPC("Leo", True, world2quest2, ["You're the one who killed that goblin leader, right?", "That's so cool! There's a skeleton just like that somewhere around town, lurking in some cave.", "It'd be awesome if you could take care of that guy too!"])
kseniya = NPC("Kseniya", True, world3quest1, ["Hello!", "You must be that adventurer that I've been hearing about so often recently.", "I heard you've slain all kinds of monsters.", "...Then, do you think you could do me a favour?", "I really HATE ants. They're just so gross!", "But whenever I look around outside of town, there's always some kind of ant there waiting for me!"])
elimar = NPC("Elimar", True, world3quest2, ["Hey, you!", "You're the one that took down those skeleton and goblin guys, yeah?", "Then I'm gonna need a huge favour, but I'll pay you handsomely!", "Somewhere around town, there's this ant queen lurking around.", "Usually I wouldn't care about that kind of stuff, but those darn ants keep stealing my food! It's driving me crazy!"])
keoni = NPC("Keoni", True, world4quest, ["Ah, it's rare to see a new face here.", "As of recently, most people decided to leave this town because of the spider problem.", "Now you won't find many people here...", "I miss how lively the streets used to be, but ever since those spiders started staying around, they've scared everyone away.", "If only someone could just get rid of them."])
###############################
#Main Areas
world1 = Place("Lerwick", False, [], True, False, False, [lucy, filippos])
world2 = Place("Wellspring", True, [], True, False, False, [kahina, leo])
world3 = Place("Broughton", True, [], True, False, False, [kseniya, elimar])
world4 = Place("Caister", True, [], True, False, False, [keoni])
###############################
#Bosses
goblinBoss = Boss_Enemy("Bokoblin", "Goblin Leader", (random.randint(50, 70)), (random.randint(30,40)), (random.randint(100, 140)), 120, treasure1, (random.randint(41, 45)), "Smash", world2, 1)
skeletonBoss = Boss_Enemy("Osseus", "Skeleton Leader", (random.randint(70, 100)), (random.randint(40, 50)), (random.randint(200, 300)), 120, treasure2, (random.randint(55, 61)), "Back Breaker", world3, 2)
antQueen = Boss_Enemy("The Ant Queen", "Ant Queen", (random.randint(100, 120)), (random.randint(71, 75)), (random.randint(300, 400)), 120, treasure3, (random.randint(76, 80)), "Colony", world4, 3)
spiderBoss = Boss_Enemy("Widow", "Spider Boss", (random.randint(120, 140)), (random.randint(76, 80)), 500, 140, treasure4, (random.randint(81, 85)), "Spider's Web", "", 4)
###############################
#SubAreas
shop1 = Place("Lerwick Shop", False, {shop1_potion1 : 20, shop1_potion2 : 20, shop1_consumable1 : 15, shop1_consumable2 : 15, shop1_weapon : 120, shop1_armour : 120}, False, False, True, [])
mobArea1 = Place("Lerwick Meadows", False, [mob1_consumable1, mob1_consumable2], False, True, False, [goblin1, goblin2, goblin3, goblin4, goblin5])
bossArea1 = Place("The Goblin Hideout", False, [boss1_consumable], False, True, False, [goblinBoss])
shop2 = Place("Wellspring Shop", False, {shop2_potion1 : 20, shop2_potion2 : 20, shop2_consumable1 : 15, shop2_consumable2 : 15, shop2_weapon : 220, shop2_armour : 220}, False, False, True, [])
mobArea2 = Place("Wellspring Meadows", False, [mob2_consumable1, mob2_consumable2], False, True, False, [skeleton1, skeleton2, skeleton3, skeleton4, skeleton5])
bossArea2 = Place("The Skeleton Lair", False, [boss2_consumable], False, True, False, [skeletonBoss])
shop3 = Place("Broughton Shop", False, {shop3_potion1 : 20, shop3_potion2 : 20, shop3_consumable1 : 15, shop3_consumable2 : 15, shop3_weapon : 320, shop3_armour : 320}, False, False, True, [])
mobArea3 = Place("Broughton Meadows", False, [mob3_consumable1, mob3_consumable2], False, True, False, [ant1, ant2, ant3, ant4, ant5])
bossArea3 = Place("The Ant Farm", False, [boss3_consumable], False, True, False, [antQueen])
shop4 = Place("Caister", False, {shop4_potion1 : 20, shop4_potion2 : 20, shop4_consumable1 : 15, shop4_consumable2: 15, shop4_weapon : 420, shop4_armour : 420}, False, False, True, [])
mobArea4 = Place("Caister Meadows", False, [mob4_consumable1, mob4_consumable2], False, True, False, [spider1, spider2, spider3, spider4, spider5])
bossArea4 = Place("The Spider's Cave", False, [boss4_consumable], False, True, False, [spiderBoss])
##################################
world1.add_connected_area(shop1)
world1.add_connected_area(mobArea1)
world1.add_connected_area(bossArea1)
world1.add_connected_area(world2)

shop1.add_connected_area(world1)
mobArea1.add_connected_area(world1)
bossArea1.add_connected_area(world1)

world2.add_connected_area(world1)
world2.add_connected_area(shop2)
world2.add_connected_area(mobArea2)
world2.add_connected_area(bossArea2)
world2.add_connected_area(world3)

shop2.add_connected_area(world2)
mobArea2.add_connected_area(world2)
bossArea2.add_connected_area(world2)

world3.add_connected_area(world2)
world3.add_connected_area(shop3)
world3.add_connected_area(mobArea3)
world3.add_connected_area(bossArea3)
world3.add_connected_area(world4)

shop3.add_connected_area(world3)
mobArea3.add_connected_area(world3)
bossArea3.add_connected_area(world3)

world4.add_connected_area(world3)
world4.add_connected_area(shop4)
world4.add_connected_area(mobArea4)
world4.add_connected_area(bossArea4)

shop4.add_connected_area(world4)
mobArea4.add_connected_area(world4)
bossArea4.add_connected_area(world4)

name = story.beginning()
player = Player(name, world1)
world1.get_summary(player)
