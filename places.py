import pyfiglet, story
import random
from reusables import generateDictionary
from enemies import Boss_Enemy, Enemies
from battle import Battle
from items import Healing

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

class Place:
    def __init__(self, name, locked, objects, fastTravel, hostile, shop, people):
        self.name = name
        self._connectedAreas = []
        self._locked = locked
        self._interactables_objects = objects #maybe use this list to incorporate the tree idea you had from the interview
        self._interactables_people = people #can add monsters to this list in hostile places
        self._canFastTravel = fastTravel
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