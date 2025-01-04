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