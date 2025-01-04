import story, time

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
    
    if isinstance(location, str) != True:
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