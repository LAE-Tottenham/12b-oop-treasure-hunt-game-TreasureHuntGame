import random
from places import Place, story
from player import Player
from enemies import Boss_Enemy, Enemies
from items import Item, Healing, Weapon_Armour
from npc import NPC
from quests import Quest

#pyifglet needs to be downloaded

#Set Up
###Key items
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
goblinBoss = Boss_Enemy("Bokoblin", "Goblin Leader", (random.randint(90, 110)), (random.randint(30,40)), (random.randint(100, 140)), 120, treasure1, (random.randint(41, 45)), "Smash", world2, 1)
skeletonBoss = Boss_Enemy("Osseus", "Skeleton Leader", (random.randint(190, 210)), (random.randint(40, 50)), (random.randint(200, 300)), 120, treasure2, (random.randint(55, 61)), "Back Breaker", world3, 2)
antQueen = Boss_Enemy("The Ant Queen", "Ant Queen", (random.randint(290, 310)), (random.randint(71, 75)), (random.randint(300, 400)), 120, treasure3, (random.randint(76, 80)), "Colony", world4, 3)
spiderBoss = Boss_Enemy("Widow", "Spider Boss", (random.randint(390, 410)), (random.randint(76, 80)), 500, 140, treasure4, (random.randint(81, 85)), "Spider's Web", "", 4)
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
player.add_fast_travel_location(world1)
player.add_fast_travel_location(world2)
player.add_fast_travel_location(world3)
player.add_fast_travel_location(world4)

world1.get_summary(player)