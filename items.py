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