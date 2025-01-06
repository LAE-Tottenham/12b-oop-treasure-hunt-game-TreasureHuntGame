import os, time

def beginning(): #Intro story
    input("Growing up, you always believed that being a treasure hunter was the greatest job anybody could have.") 
    input("For years, you would devote your time to growing stronger solely for the purpose of setting off on your own journey someday.") 
    input("Sure - the money was appealing - but the real prize was the glory! Fighting monsters, exploring unseen land, the whole package!")
    print()
    input("Slight issue - upon realising you were serious about this dream, your family have been treating you anything but seriously, absolutely certain that you would regret it for the rest of your life.")
    print()
    input("Slightly bigger issue - they’re right.")
    print()
    input("Turns out, almost dying being a ‘typical occurrence at work’ isn’t as fun as a childlike mind would have made it out to be, and thus your dream has promptly changed from being a treasure hunter into retiring early and never leaving the house.")
    input("Of course, you can’t just return home! You would be humiliated!")
    print()
    input("Although you and your family are still close, it might just be better to end up in some monster’s stomach than it would be to return home with nothing to show for it.")
    input("No matter what, you must find some sort of riches and make your own fortune!")
    print()
    print()
    input("The plan is simple:")
    input("There are 4 major civilisations to go through, each with their own monster troubles and brilliant rewards:")
    input("LERWICK: The Goblin Crown")
    input("WELLSPRING: The Skull of Knowledge")
    input("BROUGHTON: The Queen's Jewels")
    input("CAISTER: The Spider's Eye")
    input("If you can just collect all of these, your family will HAVE to respect you!")
    input("...Probably.")
    input("Well, no time to waste!")
    print("But first, what's your name, adventurer?")
    name = input()
    input(f"Well, {name}, best of luck to you!")
    return name

def ending_one(ending): #Bad Ending (1st treasure)
    if ending.upper() == "Y":
        os.system('clear')
        print("After a treacherous trip, you finally make it back to your family home.")
        time.sleep(2)
        print("A little too eagerly, you burst in with your treasure on display, proudly telling your family to look at what you found.")
        time.sleep(3)
        print("Holding for applause, you bask in their awe... Until you hear them laughing.")
        time.sleep(3)
        print("Rather than the cheers you were waiting for, they ended up making fun of how little you had earned after being gone for so long.")
        time.sleep(3)
        print("...")
        time.sleep(3)
        input("I guess spending so many years getting one piece of treasure isn't all that impressive after all...")
        input("Bad Ending - 'Tough Crowd'")
        exit()
    else:
        input("Right, there's always more treasure to find!")

def ending_two(ending): #Sub-Par Ending (2nd Treasure)
    if ending.upper() == "Y":
        os.system('clear')
        input("After a tiring trip home, you finally make it back to your family's doorstep, both pieces of treasure ready in hand.")
        input("The second they open the door, you think about nothing but achieving your goal:")
        input("Proving to them that you were right about being an adventurer (even if you weren't).")
        input("All of a sudden, you hold up both of the fruits of your labour, sure of your own success.")
        input("...But after a moment of holding for applause, you realise they're not really saying anything at all.")
        input("The best you get out of them is a 'Well... It's not that bad...'")
        input("Eh... It's better than nothing I suppose...")
        input("Ending 2/5 - 'At Least They Didn't Laugh'")
        exit()
    else:
        input("Right, you're already half-way there, no point quitting now!")

def ending_three(ending): #Decent Ending
    if ending.upper() == "Y":
        os.system('clear')
        input("After a boring trip home, you finaly reach your family's doorstep.")
        input("The moment you went inside and sat down, you finally felt like you could relax.")
        input("You had to admit, you missed the calm life back with your family.")
        input("...And then the jokes about adventuring started.")
        input("Alright, no time like the present.")
        input("With a smug grin, you place each piece of treasure you've found onto a table, proudly on display.")
        input("...And they actually seem somewhat proud!")
        input("Who would've thought? Not bad, adventurer!")
        input("Ending 3/5 - 'Not Bad At All'")
        exit()
    else:
        input("You're right, only one more thing left to grab!")

def ending_four(): #Good Ending
        os.system('clear')
        input("After an exhausting trip back home, you finally make it to your family's door.")
        input("They let you in with massive smiles on their faces, glad you're finally home.")
        input("It's not until dinner that night that someone finally brings it up...")
        print()
        input("'So how was being an adventurer?'")
        print()
        input("Overwhelmingly (and honestly kind of embarrassingly) prepared for this question, you pull out each piece of treasure you found and lay them on the table.")
        input("One by one, each of your family members start asking how you managed to collect so much.")
        input("For the rest of the night, you tell them the stories of all the monsters you faced and the people you met.")
        input("It's not until you're finally laying in bed that you decide:")
        input("'You know what, maybe it wasn't so bad after all.'")
        input("(Good) Ending 5/5 - 'All's Well That Ends Well'")
        exit()

def secret_ending(choice): #Secret Ending (15000000+ Gold)
    if choice.upper() == "Y":
        os.system('clear')
        print("After a luxurious trip home (generously funded by your own wallet) you finally make it back safe and sound.")
        time.sleep(2)
        print("Your family greet you with nothing but relief that you're alright after going off on your own, which almost makes you feel bad about being so desperate to brag.")
        time.sleep(2)
        input("...")
        input("Then your mum says 'I told you that you weren't cut out for being an adventurer.'")
        print("Well, no harm in sticking to the plan.")
        time.sleep(1)
        print("Gleefully, you pull out your wallet full of hard-earned money and watch them stare.")
        input("As you listen to them slowly begin to erupt into a cacophony of 'How!?'s, one thought fills your mind...")
        print("'Man, being an adventurer is awesome!'")
        time.sleep(3)
        input("Secret Ending - 'Set For Life'")
        exit()
    else:
        input("'Nah, it's always better to go the flashier route. Treasure it is!'")