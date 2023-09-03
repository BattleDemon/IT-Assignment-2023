from random import randint, choice

# Create a base class representing a living thing
class LivingThing():
    def __init__(self):
        self.name = 'some name'
        self.health = 1
        
    def tire(self):
        # has the chance to deal 2 dmg to the livingthing
        diceroll = randint(0,1)
        if diceroll == 0:
            self.health = self.health - 2
            print('You have gotten tired, your health suffered')
            print('Your health is', hero.health)
        else:
            pass

    def heal(self):
        # adds up to 10 health to the livingthing
        self.health = self.health + 5
        self.health = self.health + randint(0,5)
        print('Your health is now',self.health)

    def mega_heal(self):
        # doubles the livingthings health
        self.health = self.health * 2

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

# Create a class for the player, inheriting from LivingThing
class Player(LivingThing):
    def __init__(self, name,):
        # Initialize player-specific attributes
        global starter_room
        self.name = name
        self.health = 25
        self.status = 'regular'
        self.inventory = []
        self.equipped_weapon = ''
        self.rest_cooldown = 0
        self.gold = 0

    def help(self, monster):
        # Display available actions for the player
        print('Your choices are:')
        print('help : Shows you what you can do ')
        print("stats : Display's your stats")
        print("explore : Allows you to find items and friendly Npc's at the risk of encountering a monster")
        print('inventory : Allows you to view your inventory')
        print('use : Allows you to use items in your inventory') 
        print('equip : Allows you to equip weapons')
        print('go : Allows you to move between rooms')
        print('die : Used for testing and if you want to view credits')
        print('rest : Allows the player to gain health every 5 turns')

    def stats(self, monster):
        # Display player's stats
        print('You are', self.name)
        print('You have a health of', self.health)
        print('your status is', self.status)
        print('You are in', self.room.name)
        if self.equipped_weapon == '':
            print("You don't have anything equiped")
        else:
            print('You have', self.equipped_weapon.name,'equiped')
        print("You can't rest for",self.rest_cooldown,'turns')

    def explore(self, monster):
        # Increase player's health and possibly trigger a monster encounter
        self.rest_cooldown = self.rest_cooldown - 1
        self.tire()
        diceroll = randint(0,2)
        if diceroll == 0:
            if self.room.monsters != '':
                print('You have been confronted by',self.room.monsters.name)
                self.status = 'Confronted'
                input('Press Enter to continue\n>>')
            else:
                print("You couldn't find anything")
        elif diceroll == 1:
            # Player found an item while exploring
            if self.room.items != '':
                print('You found a',self.room.items.name)
                hero.pick_up_item(self.room.items)
                self.room.items = ''
                print(self.room.items)
            else:
                print("You couldn't find anything")
        elif diceroll == 2:
            # Player encountered an FriendlyNPC
            if self.room.npcs != '':
                print('You have Encountered the', self.room.npcs.name)
                self.status = 'Encountered'
                input('Press Enter to continue\n>>')
            else:
                print("You couldn't find anything")

    def fight(self, monster):
        # Engage in combat with a monster
        self.rest_cooldown = self.rest_cooldown - 1
        monster = self.room.monsters
        while self.health > 0 and monster.health > 0:
            # First deals Dmg to the monster then to the hero 
            monster.health = monster.health - randint(0,15)
            if self.equipped_weapon != '':
                monster.health = monster.health - self.equipped_weapon.modifier
            self.health = self.health - randint(0,monster.maxdamage)
            print(monster.name, 'attacks you')
            print('your health is now',self.health)
            print(monster.name,'health is now',monster.health)
            input('Press Enter to continue\n>>')

        if self.health <= 0:
            print('You were Killed by the', monster.name)
            self.status = 'regular'
        else:
            print('Victory!\nYou defeated the', monster.name)
            print('your health is now',self.health)
            self.status = 'regular'
            self.room.monsters = ''

        def boss_fight(self,monster):
            pass
            
    def friendlyencounter(self,monster):
        # Allows the player to encounter friendlyNPC's
        option = input('Your options are \n>Leave (leave the Npc you encountered)\n>Buy ()\n>Talk ()\n>>')
        option = option.capitalize()
        while self.status == 'Encountered':
            if option == 'Leave':
                print(self.name,'walks away')
                self.status = 'regular'
                return
            elif option == 'Buy':
                print('You can buy',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                option_2 = input('Do you want to buy this item? (yes/no)\n>>')
                if option_2 == 'yes':
                    if self.gold >= self.room.npcs.item_cost:
                        print('You bought',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                        self.pick_up_item(self.room.npcs.items)
                        return
                    else:
                        print("you don't have enough gold to buy", self.room.npcs.items.name)
                else:
                    return
            elif option == 'Talk':
                pass
            else:
                print(self.name,"doesn't understand this suggestion")

    def show_inventory(self, monster):
        # Allows the player to view their inventory
        if self.inventory:
            print('You have:')
            for item in self.inventory:
                print(f'{item.name}: {item.description}')
        else:
            print('Your inventory is empty.')
    
    def pick_up_item(self, item):
        # Allows the player to pick up items
        self.inventory.append(item)  # Add the item to the inventory list
        print(f'You picked up {item.name}.')

    def use(self, monster):
        # Allows the player to use item such as health potions
        item_name = input('What item do you want to use?\n>>')
        item_name = item_name.capitalize()
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, Weapon):
                    print("You can't use a weapon in this way.")
                else:
                    item.attributes()  # Call the item's attributes method
                    self.inventory.remove(item)  # Remove the used item from inventory
                    self.rest_cooldown = self.rest_cooldown - 1
                return
        print("You don't have that item in your inventory.")

    def equip(self, monster):
        # Allows the player to equip items they have in their inventory
        item_name = input('What do you want to equip?\n>> ')
        item_name = item_name.capitalize()
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, Weapon):
                    if self.equipped_weapon == '':
                        self.equipped_weapon = item
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        return  # Exit the function after equipping
                    else:
                        self.inventory.append(self.equipped_weapon)
                        self.equipped_weapon = item
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        return  # Exit the function after equipping
                else:
                    print('that is not a weapon and can not be equiped')
                    return # Exits function
        print("You can't equip that")

    def go(self,monster):
        # Allows the player to move between rooms 
        try:
            direction = input("Which direction do you want to go? (north/south/east/west)\n>> ")
            # checks if the direction that was inputed is an avaliable direction
            if direction in room_connections[self.room]:
                self.room = room_connections[self.room][direction]
                print(f'You went {direction}')
                print(f'you are now in the {self.room.name}')
                self.rest_cooldown = self.rest_cooldown - 1
                self.tire()
            else:
                print("You can't go that way.")
        except KeyError:
            print("Invalid input or no valid connections from this room.")
            
    def die(self,monster):
        # Allows the player to die at will 
        self.health = 0
        print('せっぷく')

    def rest(self,monster):
        # allows the player to rest (gaining a small amount of health) resting can only happen once every couple of turns
        if self.rest_cooldown <= 0:
            self.heal()
            print(f'Your health is now {self.health}')
            self.rest_cooldown = 5
        else:
            print('your not tired enough to rest')

    def show_exits(self,monster):
        pass

    def god_mode(self,monster):
        pass

    def egg(self,monster):
        print('This is an easter egg')

# Create a class for monsters, also inheriting from LivingThing
class Monster(LivingThing):
    def __init__(self, name, health, maxdamage,drops,gold_drops):
        # Initialize monster attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops

# Create a class for friendly NPC's, also inheriting from LivingThing
class FriendlyNPC(LivingThing):
    def __init__(self,name,health,lines,items,item_cost):
        # Initialize friendly NPC attributes
        self.name = name
        self.health = health
        self.lines = lines
        self.items = items
        self.item_cost = item_cost

# Create a Class for Items
class Item():
    def __init__(self,name,description,attributes):
        # Initialize Items
        self.name = name 
        self.description = description
        self.attributes = attributes

class Potion(Item):
    def __init__(self,name,attributes):
        self.name = name 
        self.description = 'Restores some health points.'
        self.attributes = attributes

# Create a class for Weapons, inheriting from Item
class Weapon(Item):
    def __init__(self,name,description,modifier):
        # Initialize Weapons
        self.name = name
        self.description = description
        self.modifier = modifier

# Create a class for Rooms
class Room():
    def __init__(self,name ,description, monsters, npcs, items):
        # Initialize Rooms
        self.name = name
        self.description = description
        self.monsters = monsters
        self.npcs = npcs
        self.items = items

# function to roll credits
def credits():
    input('Press Enter to continue\n>>')
    print('\n\n\n')
    print('░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀\n'
          '░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█\n'
          '░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀')
    print('Lead Design -- Dexter Hart')
    print('Lead Artist -- Dexter Hart')
    print('Lead Programmer -- Dexter Hart')
    print('Lead Level Designer -- Dexter Hart')
    print('Tester -- Dexter Hart')
    print('Tester -- Joss Ormes')
    print('Tester -- Samson Droney')
    print('Tester -- Gabriel Mesquita')
    print('Tester -- Zen Xeri')

# Dictionary of commands mapped to player methods
Commands = {
    'help': Player.help,
    'stats': Player.stats,
    'explore': Player.explore,
    'inventory': Player.show_inventory,
    'inv': Player.show_inventory,
    'use' : Player.use,
    'equip': Player.equip,
    'go' : Player.go,
    'die': Player.die,
    'rest': Player.rest,
    '': Player.egg
}

# Dictionary of Difficultys 
Difficulty = {
    'Really Easy': 1,
    'Easy': 2,
    'Normal': 3,
    'Hard': 4,
    'Extra Hard': 5,
    'Extreme': 6,
    'really easy': 1,
    'easy': 2,
    'normal': 3,
    'hard': 4,
    'extra hard': 5,
    'extreme': 6,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6
}

# Title
print(
    "_________ _______  _        _______  _______        _______  _______               _______  _        _______           _______ \n"
    "\__   __/(  ___  )( \      (  ____ \(  ____ \      (  ___  )(  ____ \    |\     /|(  ___  )( \      (  ___  )|\     /|(  ____ )\n"
    "   ) (   | (   ) || (      | (    \/| (    \/      | (   ) || (    \/    | )   ( || (   ) || (      | (   ) || )   ( || (    )|\n"
    "   | |   | (___) || |      | (__    | (_____       | |   | || (__        | |   | || (___) || |      | |   | || |   | || (____)|\n"
    "   | |   |  ___  || |      |  __)   (_____  )      | |   | ||  __)       ( (   ) )|  ___  || |      | |   | || |   | ||     __)\n"
    "   | |   | (   ) || |      | (            ) |      | |   | || (           \ \_/ / | (   ) || |      | |   | || |   | || (\ (   \n"
    "   | |   | )   ( || (____/\| (____/\/\____) |      | (___) || )            \   /  | )   ( || (____/\| (___) || (___) || ) \ \__\n"
    "   )_(   |/     \|(_______/(_______/\_______)      (_______)|/              \_/   |/     \|(_______/(_______)(_______)|/   \__/\n"
)
input('Press Enter to continue\n>>')

# Get the player's name
print('Welcome hero')
print('you are a travelar from a far of land')
print('you came to this land to find valour of die trying')
name = input('What is your name?\n>> ')
hero = Player(name)
difficulty = ''

# Get difficulty function
def get_difficulty():
    global difficulty
    while difficulty == '':
        difficulty = input('Please select a difficulty\nReally Easy <1>\nEasy <2>\n'
                           'Normal <3>\nHard <4>\nExtra Hard <5>\nExtreme <6>\n>>  ')
        if difficulty in Difficulty.keys():
            difficulty = Difficulty[difficulty]
        else:
            print('!!Please select a real difficulty!!')
            difficulty = ''
    return difficulty

# get difficulty
get_difficulty()

# Create Item instances
health_potion = Potion('Health potion',hero.heal) # found in starter room
health_potion_2 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_3 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_4 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_5 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_6 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_7 = Item('Health potion','Restores some health points.',hero.heal) # found in
mega_health_potion = Item('Mega health potion','Restores many health points.',hero.mega_heal) # drops from 
mega_health_potion_2 = Item('Mega health potion','Restores many health points.',hero.mega_heal) # buy from hermit for 200 gold
teleport = Item('Teloport stone','Teleports user to any* room','') # Add fuc to teleport/ found in boss room

# Create Weapon instances
magic_sword = Weapon('Magic Sword','Increase damage by 15',15) # Drops from dragon
pitch_folk = Weapon('Pitch Folk','Increase damage by 6',6) # found in village
sword = Weapon("Sword",'Increase damage by 4',4) # found in 
axe = Weapon('Axe','Increase damage by 2',2) # found on path in forest
traveler_sword = Weapon('Traveler sword','Increase damage by 8',8) # buy from travelar for 250 gold
village_guard_sword = Weapon('Guard sword','Increase damage by 10',10) # buy from villager for 300 gold
sharp_stick = Weapon('Sharp stick','Increases damage by 1',1) # found in forest
lords_sword = Weapon('Lords Sword','Increase damage y 12',12) # found in keep

# list of Items
items = [
    health_potion,
    health_potion_2,
    health_potion_3,
    health_potion_4,
    health_potion_5,
    health_potion_6,
    health_potion_7,
    mega_health_potion,
    mega_health_potion_2,
    teleport,
    sword,
    axe,
    pitch_folk,
    traveler_sword,
    magic_sword,
    village_guard_sword,
    sharp_stick,
    lords_sword
]

# Create friendly NPC instances
villiger = FriendlyNPC('Villiger',5,"PLACE HOLDER",'','')
traveler = FriendlyNPC('Traveler',10,"PLACE HOLDER",traveler_sword,250)
hermit = FriendlyNPC('Hermit',15,'Place Holder',mega_health_potion,200)
lord = FriendlyNPC('Lord Joss',20,'','','')

# Create monster instances
wolf = Monster('Wolf',round(10*difficulty),5*difficulty,'',20)
wolf_2 = Monster('Wolf',round(10*difficulty),5*difficulty,'',20)
bear = Monster('Bear Cub',round(15*difficulty),7*difficulty,'',30)
spider = Monster('Giant Spider',round(15*difficulty),7*difficulty,'',30)
goblin_scout = Monster('Goblin Scout',round(5*difficulty),5*difficulty,'',50)
bandit = Monster('Bandit',round(25*difficulty),7*difficulty,'',100)
thug = Monster('Thug',round(15*difficulty),7*difficulty,'',100)
goblin = Monster('Goblin', round(15*difficulty),5*difficulty,'',50)
goblin_scout_2 = Monster('Goblin Scout',round(5*difficulty),5*difficulty,'',50)
goblin_scout_3 = Monster('Goblin Scout',round(5*difficulty),5*difficulty,'',50)
goblin_runt = Monster('Goblin Runt',round(2*difficulty),3*difficulty,'',30)
goblin_brute = Monster('Goblin Brute',round(20*difficulty),9*difficulty,'',100)
troll = Monster('Troll',round(20*difficulty),9*difficulty,'',100)

# Create Boss instance
dragon = Monster('Red Dragon',round(25*difficulty),12*difficulty,magic_sword,400)

# Create Rooms
forest_clearing = Room('Forest Clearing','you are in a forest clearing','','',health_potion)
forest = Room('Forest','you are in a forest',wolf,'',sharp_stick)
path_in_forest = Room('Path in Forest','you find a path in the forest','','',axe)
deeper_in_forest = Room('Deeper in Forest','you are deeper in the forest',wolf_2,'','')
along_forest = Room('Along Path','You are following a path',bear,traveler,'')
deep_forest = Room('Deep Forest','You are in a deep dark forest',spider,'','')
hut_in_forest = Room('Hut in Forest','you are on a hut along the path','',hermit,'')
meadow = Room('meadow','You are in a wide open meadow',goblin_scout,'','')
cross_road = Room('Cross Roads','You are at a cross roads their is a sign pointing west it says village of {}',bandit,'','')
village = Room('The village','You are in a village',thug,villiger,pitch_folk)
along_ridge = Room('Along the Ridge','You are along a ridge',goblin,'','')
tall_ridge = Room('Tall Ridge','You are at a tall ridge',goblin_scout_2,'','')
path_in_meadow = Room('Path Along Meadow','you are on a path in a meadow',goblin_scout_3,'','')
keep = Room('The Keep','you are in the keep of {}','',lord,lords_sword)
cave_entrance_2 = Room('Cave Entrance','You are in a cave entrance',goblin_runt,'','')
cave_entrance = Room('Cave Entrance','You are in a cave entrance',goblin_brute,'','')
deep_cave = Room('Deeper in cave','You are in a deep cave',troll,'','')
cave_cavern = Room('Cave Cavern','You are in a large open cavern','','','')

Boss_Room = Room('Open Cavern','',dragon,'',magic_sword)

# Room connections dict
room_connections = {
    forest_clearing : {'north' : forest},
    forest : {'north' : deeper_in_forest, 'west' : path_in_forest, 'south' : forest_clearing},
    deeper_in_forest : {'north' : deep_forest, 'west' : along_forest, 'south' : forest},
    along_forest : {'north' : hut_in_forest, 'east' : deeper_in_forest, 'south' : path_in_forest},
    deep_forest : {'north' : meadow, 'south' : deeper_in_forest},
    hut_in_forest : {'north' : cross_road, 'south' : along_forest},
    meadow : {'north' : tall_ridge, 'south' : deep_forest},
    cross_road : {'north' : path_in_meadow, 'west' : village, 'south' : hut_in_forest},
    village : {'north' : keep, 'east' : cross_road},
    along_ridge : {'north' : cave_entrance_2, 'west' : tall_ridge},
    tall_ridge : {'north' : cave_entrance, 'east' : along_ridge, 'west' : path_in_meadow, 'south' : meadow},
    path_in_meadow : {'east' : along_ridge, 'west' : keep, 'south' : cross_road},
    keep : {'east' : path_in_meadow, 'south' : village},
    cave_entrance_2 : {'north' : deep_cave, 'south' : along_ridge},
    cave_entrance : {'north' : cave_cavern, 'south' : tall_ridge},
    deep_cave : {'west' : cave_cavern, 'south' : cave_entrance_2},
    cave_cavern : {'east' : deep_cave, 'east' : Boss_Room, 'south' : cave_entrance},
    Boss_Room : {'east' : cave_cavern}
}

hero.inventory = [sword] # remove
hero.inventory.append(health_potion) # remove 
boss = dragon
forest_clearing.npcs = hermit
hero.gold = 10000000
monster = ''
# Main game loop function
def Main_loop():
    # Start Storys
    hero.room = forest_clearing
    print('(type help to get a list of actions) ')
    print(hero.name, 'Your story begins' ,hero.room.description)
    # Game loop
    while hero.isAlive and boss.isAlive:
        if hero.status == 'Confronted':
            # Force fight
            hero.fight(monster)
        elif hero.status == 'Encountered':
            # Force encounter with FriendlyNPC's
            hero.friendlyencounter(hero.room.npcs)
        else:
            # User inputs
            print(hero.room.description)
            line = input('What do you want to do \n>> ')
            if hero.rest_cooldown < 0:
                hero.rest_cooldown = 0
            if line in Commands.keys():
                Commands[line](hero, monster)
            else:
                print(hero.name, 'does not understand this suggestion.')

# Run main loop
Main_loop()

# Ending options
if hero.isAlive:
    print('You Win! Game Over')
else:
    print('Game Over. you lost :(')

# roll credits 
credits()
