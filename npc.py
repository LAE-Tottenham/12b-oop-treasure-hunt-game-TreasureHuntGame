import time

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