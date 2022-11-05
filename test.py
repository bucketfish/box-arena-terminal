#box arena remake

import random
import os
import pickle
from sys import exit

#loot tables
loot = {
    1:['wooden stick', 'healing drop', 'cookie'],
    2:['wooden sword', 'health pot', 'choco cookie', 'clothes'],
    3:['stone sword', 'leather padding', 'apple pie'],
    4:['stone axe', 'health potion'],
    5:['sharp flint', 'steak', 'iron armor'],
    6:['battle axe', 'golden apple', 'grilled porkchop'],
    7:['spiked mace', 'chainmail armor', 'pumpkin pie'],
    8:['iron rapier', 'iron heart', 'nano-vest', 'cake'],
    9:['silver katana', 'diamond hoe', 'golden carrot'],
        }

items = {
    #level 1 itms
    'wooden stick':{
                    'damage': 1,
                    'energy': -1,
                    'weapon': True,
                    'fusion': 'wooden sword',
                    'desc': 'it’s just about as effective as a slightly more polished branch.',
                    },

    'healing drop':{
                    'health': 1,
                    'desc': 'a drop of this might just be what you need for a small cut on your finger!',
                    },

    'cookie':      {
                    'energy': 2,
                    'desc': 'it’s a cookie. congrats. you now have a cookie.',
                    },


    #level 2 items
    'wooden sword':{
                    'damage': 2,
                    'energy': -2,
                    'weapon': True,
                    'fusion': 'stone sword',
                    'desc': 'it’s more useful than a stick, but that doesn’t make it useful.',
                    },

    'health pot':  {
                    'health': 2,
                    'desc': 'an ENTIRE POT? OF HEALTH? what a GEM! a pity it only heals two hp.',
                    },

    'choco cookie':{
                    'energy': 3,
                    'desc': 'it\'s a cookie, just that it has chocolate on it. congrats. you now have a choco cookie.',
                    },

    'clothes':     {
                    'plural': 'clothes',
                    'total_health': 1,
                    'desc': 'maybe if you put some of this on people would stop attacking you.',
                    },


    #level 3 items
    'stone sword': {
                    'damage': 3,
                    'energy': -5,
                    'weapon': True,
                    'fusion':'stone axe',
                    'desc': 'now we’re getting somewhere! ‘somewhere’ is probably a fiery pit of lava, but, y\'know, it’s somewhere.',
                    },

    'leather padding':{
                    'total_health': 2,
                    'desc': 'call it whatever you like - we all know it\'s a fursuit.',
                    },

    'apple pie':    {
                    'energy': 3,
                    'health':2,
                    'desc': 'it might just smell vaguely of happiness if you just hold your breath.',
                    },


    #level 4 items
    'stone axe':    {
                    'damage': 4,
                    'energy': -4,
                    'weapon': True,
                    'fusion':'sharp flint',
                    'desc': 'if you\'ve an axe to grind with someone, give them this axe.',
                    },

    'health potion':{
                    'health': 3,
                    'desc': 'I hear drinking this is good for your health.',
                    },


    #level 5 items
    'sharp flint':{
                    'damage': 4,
                    'energy': -3,
                    'weapon': True,
                    'fusion': 'battle axe',
                    'desc': 'trust me, paper cuts are NOTHING compared to devastation you get from trying to hold this. don\'t hold it. don\'t put it in your pocket. all it does is cause pain. just...trust us on this.',
                    },

    'steak':{
                    'energy': 5,
                    'desc': 'finally, some good ol\' overcooked steak.',
                    },

    'iron armor':   {
                    'total_health': 5,
                    'desc': 'sure, it\'s clunky, and loud, and heavy, but it\'s also very shiny if you polish it often! by \'often\', we mean every ten seconds.',
                    },


    #level 6 items
    'battle axe':   {
                    'damage': 6,
                    'energy':-5,
                    'weapon': True,
                    'fusion': 'spiked mace',
                    'desc': 'this is the axe you use to lightly graze your mortal enemy with. just be grateful it\'s made of something better than stone.',
                    },

    'golden apple': {
                    'health': 5,
                    'desc': 'it\'s shiny. you could probably attract a crow with it. the crow would probably be a better source of food.',
                    },

    'grilled porkchop':{
                    'energy': 6,
                    'desc': 'it\'s grilled, it\'s pork, and it\'s a chop. pretty self-explanatory, if you ask me.',
                    },


    #level 7 items
    'spiked mace':  {
                    'damage': 10,
                    'energy': -15,
                    'weapon': True,
                    'fusion': 'iron rapier',
                    'desc': 'there\'s probably a sound argument to be made on its usefulness, but I don\'t want to hear it.',
                    },

    'chainmail armor':{
                    'total_health': 7,
                    'desc': 'how are the endless string of texts you forwarded helping you now, huh? HUH? probably more than this ever will, but that\'s besides the point.',
                    },

    'pumpkin pie':  {
                    'energy': 8,
                    'desc': 'if the taste of apple pies doesn\'t suit you, this definitely won\'t!',
                    },


    #level 8 items
    'iron rapier':  {
                    'damage': 12,
                    'energy': -7,
                    'weapon': True,
                    'fusion': 'silver katana',
                    'desc': 'look how it gleams! look how COOL and AWESOME it is! look how it stabs - hang on - look how it stabs! look. okay. look how it - y\'know what? just...look away.',
                    },

    'iron heart':   {
                    'health': 7,
                    'desc': 'don\'t think about where it came from and you\'ll be fine - if you’re fine living as an accomplice to MURDER, you MURDERER.',
                    },

    'nano-vest':    {
                    'total_health': 10,
                    'desc': 'it\'s pretty impressive...that such a vest made with nanotechnology could be this useless.',
                    },

    'cake':         {
                    'energy': 10,
                    'health': 7,
                    'desc': 'is a lie and marie antoinette is the liar.',
                    },


    #level 9 items
    'silver katana':{
                    'damage': 20,
                    'energy': -17,
                    'weapon': True,
                    'fusion': 'emerald greatsword',
                    'desc': 'now you look like a ninja - just worse!',
                    },

    'diamond hoe':  {
                    'damage': 10,
                    'energy': 0,
                    'weapon': True,
                    'desc': 'till your crops with this for extra damage to your soul!',
                    },

    'golden carrot':{
                    'energy': 15,
                    'health': 10,
                    'desc': 'oink oink you capitalist pig. bring back the guillotine.',
                    },


    #fusion only items
    'emerald greatsword':{
                    'damage': 25,
                    'energy': -20,
                    'weapon': True,
                    'fusion': 'sapphire saber',
                    'desc': 'villagers won\'t be able to get ENOUGH of this!',
                    },

    'sapphire saber':{
                    'damage':30,
                    'energy': -30,
                    'weapon': True,
                    'fusion': 'axe of perun',
                    'desc': 'it\'s just like a light saber - just...less.',
                    },

    'axe of perun': {
                    'plural': 'axes of perun',
                    'damage':40,
                    'energy': -35,
                    'weapon': True,
                    'desc': 'you really didn\'t need to flex this hard on us.',
                    },


    #boss drops
    'ruby scythe':  {
                    'damage': 15,
                    'energy': -10,
                    'weapon': True,
                    'desc': 'you killed someone. now you have a scythe. and the scent of death.',
                    },

    'blade of fire':{
                    'plural': 'blades of fire',
                    'damage': 35,
                    'energy': -30,
                    'weapon': True,
                    'desc': 'do you know why it\'s so hot in here? because you decided to carry a blade of FIRE into this room, that\'s why.',
                    },


    #elemental blade
    'elemental blade':{
                    'damage': 100,
                    'energy': 0,
                    'weapon': True,
                    'desc': 'it kept balance between the elements...but all that changed when the fire nation attacked...',
                    },


    #misc
    'fishcow':      {
                    'health': -10,
                    'energy': 10,
                    'desc': 'why.',
                    }
}

seenitems = []

bosslist = {
    2:[
        'nyam',
        'sol',
        'pionk'],

    6:[
        'flickflack',
        'ticktack',
        'kickee'],

    10:[
        'slurpydoo',
        'conkydonk',
        'tictactoe',
        'fishymoo'],

    'end':[
        'poinkydirtie', #earth
        'swooshymooshy', #water
        'foofeefoofee', #fire
        "puffpuffiepuff" #air
         ]
    }
bosses = {
    #level 3 bosses
    'nyam':{
                'damage': 2,
                'health': 5,
                'level': 1,
                'drop':['steak', 'steak', 'steak', 'steak', 'choco cookie'],
                'desc': 'it eats a lot. not that we\'re judging, or anything.'},

    'sol':{
                'damage': 4,
                'health': 2,
                'level': 1,
                'drop':['golden apple', 'golden apple'],
                'desc': 'its future is almost blinding. a pity you have to cut it short.'},

    'pionk':{
                'damage': 1,
                'health': 7,
                'level': 1,
                'drop':['wooden stick', 'wooden stick', 'wooden stick', 'wooden stick', 'wooden stick', 'wooden stick', 'wooden stick', 'wooden stick'],
                'desc': 'just... be nice and pretend its hits hurt.'},


    #level 6 bosses
    'flickflack':{
                'damage':5,
                'health': 8,
                'level': 2,
                'drop':['sharp flint', 'sharp flint', 'sharp flint'],
                'desc': 'you... don\'t want to be anywhere near it about five seconds after you\'ve defeated it. trust me.'},

    'ticktack':{
                'damage':7,
                'health': 4,
                'level': 2,
                'drop':['nano-vest', 'nano-vest', 'iron heart'],
                'desc': 'its skin is sharp enough to be made into armour (for the masochist).'},

    'kickee':{
                'damage': 2,
                'health': 15,
                'level': 2,
                'drop':['cake', 'cake', 'cake'],
                'desc': 'its legs are entirely made out of cake. don\'t ask me how i know this.'},


    #level 10 bosses
    'slurpydoo':{
                'damage':10,
                'health':12,
                'level':3,
                'drop':['silver katana','silver katana','silver katana','silver katana','silver katana','silver katana','silver katana','ruby scythe'],
                'desc': 'consuming metal you can\'t digest probably isn’t the best of ideas, but neither is consuming swords that could slice you in half. it does both.'},

    'conkydonk':{
                'damage':15,
                'health':6,
                'level':3,
                'drop':['emerald greatsword','ruby scythe'],
                'desc': 'if you beat it up, it\'ll help you beat other monsters up. beat it up.'},

    'tictactoe':{
                'damage':3,
                'health':20,
                'level':3,
                'drop':['ruby scythe', 'golden carrot', 'golden carrot'],
                'desc': 'it\'s won ten carrot-eating competitions, and the fame\'s really gotten to his head.'},

    'fishymoo':{
                'damage':42,
                'health': 11,
                'level': 3,
                'drop':['fishcow', 'fishcow', 'fishcow'],
                'desc': 'this is the worst thing you will ever have the misfortune of meeting.'},


    #endgame
    'poinkydirtie':{
                'damage':30,
                'health':70,
                'level':'endgame',
                'desc':'incomplete description owo'},

    'swooshymooshy':{
                'damage':30,
                'health':50,
                'level':'endgame',
                'desc':'incomplete description owo'},

    'foofeefoofee':{
                'damage':50,
                'health':50,
                'level':'endgame',
                'drop':['blade of fire'],
                'desc':'incomplete description owo'},

    'puffpuffiepuff':{
                'damage':30,
                'health':50,
                'level':'endgame',
                'desc':'incomplete description owo'}
    }

cowardmessage = [
                'huh. I thought you were braver than that.',
                'c\'mon, you could’ve handled that.',
                'what\'s the point of coming in here if you\'re just running away?',
                'okay. this is getting on my nerves now. last chance. don\'t let me down.',
                'i guess you aren\'t who i wanted you to be. well. goodbye.\nthe values of all chests have been reduced.',
                'typical.']

#values
directions = ['up', 'down', 'left', 'right']
take = ['take', 'retrieve', 'collect']
usage =  ['use', 'do', 'eat','fight']
look = ['look', 'lookaround', 'observe']
inventory = ['i', 'inventory', 'carrying']
bossstats = ['boss', 'stats', 'stat', 'statistics', 'status']
fuse = ['fuse','fusion','f']
fightplaces = [2, 6, 10]
endgames = []

ycoord = 0
xcoord = 0
coord = '0 0'
chest = []
places = {
            '0 0' :[],
            '1 0': ['cookie'],
            '1 1': ['wooden stick'],
            '0 1': ['cookie'],
            '0 -1': ['wooden stick'],
            '-1 -1': ['wooden stick'],
            '-1 0': ['healing drop'],
            '-1 1':['cookie'],
            '1 -1':['healing drop']}

beenplaces  = ['0 0']
genbosses = {
                '10 -10': {'name': 'poinkydirtie', 'alive': True},
                '10 10': {'name': 'swooshymooshy', 'alive': True},
                '-10 10': {'name': 'foofeefoofee', 'alive': True},
                '-10 -10': {'name': 'puffpuffiepuff', 'alive': True}}
seenbosses = []

current_boss = ''
isFighting = False
carrying = []
health = 5
energy = 5
damage = 0
total_health = 5
defeated = False

coward = 0
isCoward = False
prestige = 0

run = True

#before while true code
def start():
    print()
    enter = input('the gate is hanging loosely off its hinges [press enter/return to continue]')
    enter = input('leading into dark stairs into darker rooms')
    enter = input('into doors hiding darker secrets')
    enter = input('the door is wide open - the only question that remains')
    enter = input('adventurer, is whether you will step through it')
    enter = input('and into the box arena.')

    print('''
-=+=- box arena -=+=-
-+- made by ty and g -+-

(type \'help\' for a list of what you can do!)

you are in box 0x, 0y.
there is nothing here.''')

#general, simple commands
def save_obj(obj, name):
    with open('saves/'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name, new = True):
    if new:
        with open('saves/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)

    elif not new:
        os.chdir('..')
        with open('saves/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)


def info():
    print("-+- information -+-")
    print("box arena is a game created by ty and g.")
    print("you spawn in box 0x, 0y. use directions to move around and pick up items from chests.")
    print("the further from spawn you move, the better the items will get.")
    print("there will be bosses to fight. if you die, the game ends.")
    print("that's it. good luck and have fun!")
    print('type \'help\' for commands you can use.')
    print("-+- --- -+-")
    print('ty and g - if you can dream it, we can do it.')

def helpmenu():
    print("-+- help menu -+-")
    print("inventory (i) - check stats and inventory")
    print("up/down/left/right - move around")
    print('use [item] - use item')
    print('take [all] [item] - take item from chest')
    print('look - look around the room you\'re in')
    print('map - look at the map')
    print('info - information about the game')
    print("fuse [all] [item] - fuse 3 of the same item to get a better item")
    print('[item] - see stats of that item')
    print('save - save your progress')
    print('load - load your saved progress from last time')
    print('peek [direction] - check what\'s in that box')
    print('-+- --- -+-')


def resetAll():
    global current_chest
    global ycoord
    global xcoord
    global coord
    global chest
    global places
    global seenplaces
    global genbosses
    global seenbosses
    global carrying
    global health
    global energy
    global damage
    global total_health

    current_chest=[]
    ycoord = 0
    xcoord = 0
    coord = 0
    chest = []
    places = {'0 0' :[],
                '1 0': ['cookie'],
                '1 1': ['wooden stick'],
                '0 1': ['cookie'],
                '0 -1': ['wooden stick'],
                '-1 -1': ['wooden stick'],
                '-1 0': ['healing drop'],
                '-1 1':['cookie'],
                '1 -1':['healing drop']}
    genbosses = {'10 -10': {'name': 'poinkydirtie', 'alive': True},
                    '10 10': {'name': 'swooshymooshy', 'alive': True},
                    '-10 10': {'name': 'foofeefoofee', 'alive': True},
                    '-10 -10': {'name': 'puffpuffiepuff', 'alive': True}}
    seenbosses = []
    beenplaces = []

    carrying = []
    health = 5
    energy = 5
    damage = 0
    total_health = 5

def gameOver():
    global run
    print("-+- game over -+-")
    print("you died!")
    print("restart the game to try again.")
    run = False
def ended():
    global endgames
    allend = ['foofeefoofee', 'swooshymooshy', 'poinkydirtie', 'puffpuffiepuff']
    global seenbosses
    global genbosses
    global carrying
    global defeated
    if all(elem in endgames for elem in allend) and not defeated:
            return True
    else:
        return False
def endGame():
    global carrying
    global prestige
    global run

    carrying.append('elemental blade')
    carrying.remove('blade of fire')

    one = ['1', 1, 'one', 'again', 'play again']
    two = ['2',2, 'two', 'continue','keep playing', 'continue playing']
    three = ['3', 3, 'three', 'next', 'prestige']
    four = ['4', 4, 'four', 'quit', 'exit']

    print()
    print("-+- the end -+-")
    print("congratulations! you have beaten the game and collected the 4 Elemental Blades!")
    print("they fused together to form an Elemental Blade.")

    print("would you like to:")
    print("1: play again")
    print("2: continue playing")
    print('3: prestige to next level')
    print("4: quit")
    answer = 'yeehaw placeholderr'

    while answer not in one and answer not in two and answer not in three and answer not in four:
        answer = input(">>>").lower()

        if answer in one:
            print("restarting game! have fun!")
            resetAll()
            return

        elif answer in two:
            print("continuing game! have fun!")
            print("tip: use your elemental blade - it's overpowered!")
            return

        elif answer in three:
            prestige += 1
            print('you have prestiged to level ' + str(prestige) + '.')
            return

        elif answer in four:
            print("sad to see you go. come back again!")
            run = False
            return

        else:
            print("-+- error -+-")
            print("we could not understand what you said")
def pickValue(Xcoord, Ycoord): #return number
    global fightplaces


    if abs(Ycoord) in fightplaces or abs(Xcoord) in fightplaces:
        if abs(Ycoord) > abs(Xcoord):

            if abs(Ycoord) in fightplaces:
                return abs(Ycoord)

            else:
                return abs(Xcoord)

        else:
            if abs(Xcoord) in fightplaces:
                return abs(Xcoord)

            else:
                return abs(Ycoord)
def splittable(String):
    try:
        test = String.split()[1]
    except:
        return False

    return True
def plural(Item):
    global items
    if 'plural' in items[Item].keys():
        return items[Item]['plural']
    else:
        return Item + 's'

def next():
    print('-+- prestige ' + prestige + " -+-")
    print("all your physical progress has been lost. enjoy your new world.")
    print("ps: check your prestige level anytime by typing 'prestige'. ")
    resetAll()

#okay actual stuff
def move(direction): #none, loot, boss?
    global xcoord
    global ycoord
    global coord
    global places
    global beenplaces
    global fightplaces
    global genbosses
    global seenbosses

    #return none
    if direction.lower() == 'up':
        ycoord += 1
        if ycoord >= 11:
            ycoord = 10
            print("you can't move past the edge of the map.")
            return 'none'

    elif direction.lower() == 'down':
        ycoord -= 1
        if ycoord <= -11:
            ycoord = -10
            print("you can't move past the edge of the map.")
            return 'none'
    elif direction.lower() == 'right':
        xcoord += 1
        if xcoord >= 11:
            xcoord = 10
            print("you can't move past the edge of the map.")
            return 'none'
    else:
        xcoord -= 1
        if xcoord <= -11:
            xcoord = -10
            print("you can't move past the edge of the map.")
            return 'none'

    #arrow
    if direction == 'up':
        print("you move up ↑")
    elif direction == 'down':
        print("you move down ↓")
    elif direction == 'left':
        print("you move left ←")
    else:
        print("you move right →")

    print("you are in box " + str(xcoord) + "x, " + str(ycoord) + "y.")
    coord = str(xcoord) + ' ' + str(ycoord)
    contents = []

    if abs(xcoord) in fightplaces or abs(ycoord) in fightplaces:
        if coord in genbosses.keys():
            if genbosses[coord]['alive']:
                return 'boss'
            else:
                return 'none'
        else:
            return 'boss'

    else:
        return 'loot'

def peek(direction):
    global xcoord
    global ycoord
    global coord
    global places
    global beenplaces
    global fightplaces
    global genbosses
    global seenbosses

    #return none
    if direction.lower() == 'up':
        peeky = ycoord + 1
        peekx = xcoord
        if ycoord + 1 >= 11:
            print("you can't move past the edge of the map.")
            return 'none', ''

    elif direction.lower() == 'down':
        peeky = ycoord - 1
        peekx = xcoord
        if ycoord - 1 <= -11:
            print("you can't move past the edge of the map.")
            return 'none', ''

    elif direction.lower() == 'right':
        peeky = ycoord
        peekx = xcoord + 1
        if xcoord + 1 >= 11:
            print("you can't move past the edge of the map.")
            return 'none', ''
    else:
        peeky = ycoord
        peekx = xcoord - 1
        if xcoord - 1 <= -11:
            print("you can't move past the edge of the map.")
            return 'none', ''

    #arrow
    if direction == 'up':
        print("you peek up ↑")
    elif direction == 'down':
        print("you peek down ↓")
    elif direction == 'left':
        print("you peek left ←")
    else:
        print("you peek right →")

    print("it is box " + str(peekx) + "x, " + str(peeky) + "y.")
    peekcoord = str(peekx) + ' ' + str(peeky)

    if abs(peekx) in fightplaces or abs(peeky) in fightplaces:
        if peekcoord in genbosses.keys():
            if genbosses[peekcoord]['alive']:
                return 'boss', peekcoord
            else:
                print('Ttere is nothing there.')
                return 'none', ''
        else:
            return 'boss', peekcoord
    else:
        return 'loot', peekcoord

def fight(value, coord): #boss name
    global bosslist
    global bosses
    global carrying
    global health
    global stength
    global total_health
    global usage
    global inventory
    global genbosses

    if coord in genbosses.keys():
        chosen = genbosses[coord]['name']
    else:
        chosen = random.choice(bosslist[value])

    return chosen

def generateLoot(xcoord,ycoord,isCoward):#contents
    global loot
    global carrying
    if isCoward:
        xcoord = xcoord - 1 if xcoord != 1 else xcoord
        ycoord = ycoord - 1 if ycoord != 1 else ycoord

    if abs(xcoord) > abs(ycoord):
        price = abs(xcoord)
    else:
        price = abs(ycoord)
    contents = []
    while price > 0:
        randomnum = random.randint(1,price)
        item = random.choice(loot[randomnum])
        price -= randomnum
        contents.append(item)

    return contents
def mapit():
    global ycoord
    global xcoord
    global coord
    global beenplaces
    global fightplaces
    global seenbosses
    global genbosses

    coord1 = -10
    coord2 = 10
    totcoord = '-10 10'
    coord = str(xcoord) + ' ' + str(ycoord)
    print('key:')
    print(chr(9608) + ' - chest room')
    print(chr(9679) + ' - fight')
    print('x - player')
    print(chr(9633) + ' - places you\'ve been to already')
    print(chr(9733) + ' - bosses you\'ve seen that are still alive')
    print(chr(9654) + ' - endgame bosses')
    print('s - spawn')
    print()

    for x in range(0, 21):

        for x in range(0, 21):
            if totcoord == coord:
                print('x', end = ' ')

            elif totcoord in seenbosses and genbosses[totcoord]['alive']:
                print(chr(9733), end = ' ')

            elif totcoord in seenbosses and not genbosses[totcoord]['alive']:
                print(chr(9633), end = ' ')

            elif totcoord == '0 0':
                print('s', end = ' ')

            elif totcoord in beenplaces:
                print(chr(9633), end = ' ')

            elif abs(coord1) in fightplaces:
                print(chr(9679), end = ' ')

            elif abs(coord2) in fightplaces:
                print(chr(9679), end = ' ')

            else:
                print(chr(9608), end = ' ')

            coord1 += 1
            totcoord = str(coord1) + ' ' + str(coord2)


        coord2 -= 1
        coord1 = -10
        totcoord = str(coord1) + ' ' + str(coord2)
        print()
def next():
    pass
def lookinventory():
    global carrying
    global health
    global total_health
    global energy

    thingstuff = {i:carrying.count(i) for i in carrying}
    if thingstuff:
        print('-+- your inventory -+-')
        for key, value in thingstuff.items():
            print(str(value) + 'x ' + key)
        print('-+- --- -+-')

    else:
        print("-+- your inventory -+-")
        print("your inventory is empty!")
        print("-+- --- -+-")

    print("health: " + str(health) + '/' + str(total_health) + '.')
    print("energy: " + str(energy))
def knowabout(item):
    global items

    print('-+- ' + item + ' -+-')

    print(items[item]['desc'])
    print()
    if 'weapon' in items[item].keys():
        print(item + ", when used, deals " + str(items[item]['damage']) + ' damage.')
        print(item + " uses " + str(abs(items[item]['energy'])) + ' energy.')

    if 'total_health' in items[item].keys():
        print(item + ", when used, adds " + str(items[item]['total_health']) + ' to your health capacity.')

    if 'energy' in items[item].keys() and 'weapon' not in items[item].keys():
        print(item + ", when used, gives " + str(items[item]['energy']) + ' energy.')

    if 'fusion' in items[item].keys():
        print(item + ' can be fused to give ' + items[item]['fusion'] + '.')

    else:
        print(item + ' cannot be fused.')

    if 'health' in items[item].keys():
        print(item + ", when used, gives " + str(items[item]['health']) + ' health.')


def fusion(thing):
    global carrying
    global items

    thingstuff = {i:carrying.count(i) for i in carrying}
    try:
        item = str(items[thing]['fusion'])

        if thingstuff[thing] > 2:
            carrying.remove(thing)
            carrying.remove(thing)
            carrying.remove(thing)
            carrying.append(item)

            return True

        else:
            return False
    except:
        return False

def save():
    try:
        os.makedirs('box arena files')
    except:
        pass
    os.chdir('box arena files')
    try:
        os.makedirs('saves')
    except:
        pass

    global coord
    global places
    global beenplaces
    global genbosses
    global seenbosses

    global carrying
    global health
    global energy
    global total_health

    global coward
    global prestige

    save_obj(coord, 'coord')
    save_obj(places, 'places')
    save_obj(beenplaces,'beenplaces')
    save_obj(genbosses, 'genbosses')
    save_obj(seenbosses,'seenbosses')

    save_obj(carrying, 'carrying')
    save_obj(health, 'health')
    save_obj(energy, 'energy')
    save_obj(total_health, 'total_health')

    save_obj(coward, 'another')
    save_obj(prestige, 'prestige')

    os.chdir('..')

def load(old = True):
    global coord
    global xcoord
    global ycoord
    global places
    global beenplaces
    global genbosses
    global seenbosses

    global carrying
    global health
    global energy
    global total_health

    global coward
    global prestige

    coord = str(load_obj('coord', old))
    xcoord = int(coord.split()[0])
    ycoord = int(coord.split()[1])

    places = load_obj('places', old)

    try:
        beenplaces = load_obj('beenplaces', old)
    except:
        alist = load_obj('places', old)
        beenplaces = list(alist.keys())

    try:
        genbosses = load_obj('genbosses', old)
    except:
        genbosses = load_obj('seenbosses', old)
        seenbosses = list(genbosses.keys())
    else:
        seenbosses = load_obj('seenbosses', old)

    carrying = load_obj('carrying', old)
    health = int(load_obj('health', old))

    try:
        energy = int(load_obj('energy', old))
    except:
        energy = int(load_obj('strength', old))

    total_health = int(load_obj('total_health', old))

    try:
        coward = int(load_obj('another', old))
    except:
        coward = 0
    try:
        prestige = int(load_obj('prestige', old))
    except:
        prestige = 0

    print("loaded!")

    if not old:
        save()

start()
#actual code
while run:
    try:
        boss_damage = bosses[genbosses[coord]['name']]['damage']

    except:
        pass

    if isFighting:
        if not fightPause:
            print()
            boss_health -= damage
            if boss_health < 1:
                print('boss health: 0/' + str(bosses[genbosses[coord]['name']]['health']))

            else:
                print('boss health: ' + str(boss_health) + '/' + str(bosses[genbosses[coord]['name']]['health']))


        if boss_health < 1 and genbosses[coord]['alive']:
            print(genbosses[coord]['name']  + " is dead.")
            print("congratulations!")
            genbosses[coord]['alive'] = False
            if 'drop' in bosses[genbosses[coord]['name']]:
                print("the drops are added to your inventory: " + ', '.join(bosses[genbosses[coord]['name']]['drop']))
                carrying += bosses[genbosses[coord]['name']]['drop']

            if genbosses[coord]['name'] == 'swooshymooshy':
                health += 50
                print('you gained 50 health from killing swooshymooshy!')
                endgames.append('swooshymooshy')

            if genbosses[coord]['name'] == 'poinkydirtie':
                total_health += 50
                print('you increased your health capacity by 50 for killing poinkydirtie!')
                endgames.append('poinkydirtie')

            if genbosses[coord]['name'] == 'puffpuffiepuff':
                energy += 50
                print('you gained 50 energy from killing puffpuffiepuff!')
                endgames.append('puffpuffiepuff')

            if genbosses[coord]['name'] == 'foofeefoofee':
                endgames.append('foofeefoofee')


            isFighting = False
            boss_health = 0

        elif not fightPause:
            print('The boss hits you.')
            health -= bosses[genbosses[coord]['name']]['damage']
            if health < 1:
                print()
                gameOver()
                break

            else:
                print('Your health: ' + str(health) + '/' + str(total_health) +  '.')

    if ended():
        defeated = True
        endGame()

    if prestige > 0:
        next()

    fightPause = False
    damage = 0

 #commands
    print()
    enter = input(">>>")
    #print("\x1b[2J\x1b[H", end="")
    #print(">>>" + enter)

    try:
        if enter.lower() in items.keys():
            command = enter.lower()
            thingy = ''
            every = []

        else:
            command = enter.lower().split()[0]
            thingy = ' '.join(enter.lower().split()[1:])
            every = enter.lower().split()

    except:
        command = enter.lower()
        thingy = enter.lower()
        every = [enter.lower()]

    #placeholder + easter eggs
    if enter.lower() == 'yeet':
        print('-tus feetus self deletus')
        fightPause = True

    elif enter.lower() == 'sexy boot animation':
        health = 69
        total_health = 420
        print('*chef kiss*')
        fightPause = True
    elif enter.lower() == 'i am a banana':
        print('fool. you are not a banana and this isn\'t going to open your inventory.')
        fightPause = True

    #move
    elif command in directions:
        place = move(command)

        #type of place: been, loot, boss, none
        if place == 'none':
            print('there is nothing here.')
            fightPause = True

        elif isFighting:
            coward += 1
            print("-+- leave boss fight -+-")
            print()
            if coward <= 5:
                print(cowardmessage[coward - 1])
                if coward == 5:
                    isCoward = True
            else:
                print(cowardmessage[5])
                isCoward = True
            print()

        if place == 'boss':
            beenplaces.append(coord)
            seenbosses.append(coord)
            if coord in genbosses.keys():
                places[coord] = []
                beenplaces.append(coord)
                current_boss = genbosses[coord]['name']
            else:
                current_boss = fight(pickValue(xcoord, ycoord), coord)
                genbosses[coord] = {}
                genbosses[coord]['name'] = current_boss
                genbosses[coord]['alive'] = True

            isFighting = True
            fightPause = True
            boss_health = bosses[genbosses[coord]['name']]['health']

            print("-+- fight time! -+-")
            print("you see a level " + str(bosses[current_boss]['level']) + " boss: " + current_boss)
            print("- " + current_boss + "'s stats -")
            print("boss health: " + str(boss_health) + '/' + str(bosses[current_boss]['health']))
            print("boss damage: " + str(bosses[current_boss]['damage']))
            print(bosses[current_boss]['desc'])


        elif place == 'loot':
            beenplaces.append(coord)
            if coord in places.keys():
                pass
            else:
                places[coord] = generateLoot(xcoord,ycoord,isCoward)
            isFighting = False

        elif place == 'been':
            print('you\'ve been here before.')
            isFighting = False

        if coord in places.keys() and place != 'none':
            if places[coord]:
                print('there is a chest. In it, you find:')
                thingstuff = {i:places[coord].count(i) for i in places[coord]}
                for key, value in thingstuff.items():
                    print(str(value) + 'x ' + key)
            elif place == 'boss':
                pass
            else:
                print('there is nothing here.')

    #map
    elif command == 'map':
        print("-+- map -+-")
        mapit()
        print("-+- --- -+-")
        fightPause = True

    #take
    elif command in take and coord in places.keys():
        if thingy == 'all':
            if places[coord]:
                print("you took the " + ', '.join(places[coord]))
                carrying += places[coord]
                places[coord] = []
            else:
                print('there is nothing to take.')

        elif thingy in places[coord]:
            carrying.append(thingy)
            places[coord].remove(thingy)
            print("you took the " + thingy + '.')
            if thingy not in seenitems:
                seenitems.append(thingy)
                print(thingy + ' - ' + items[thingy]['desc'])


        elif splittable(thingy):
            if thingy.split(None, 1)[1] in places[coord] and thingy.split()[0] == 'all':
                numberOfItem = places[coord].count(thingy.split(None, 1)[1])
                for i in range(numberOfItem):
                    places[coord].remove(thingy.split(None, 1)[1])
                    carrying.append(thingy.split(None, 1)[1])
                print("you took " + str(numberOfItem) + 'x ' + thingy.split(None, 1)[1])

            else:
                print('you don\'t have that.')
        else:
            print("-+- error -+-")
            print("what you said could not be understood")
            print("help for commands!")

    #use item
    elif command in usage:
        use = False
        if thingy in carrying:
            usething = items[thingy]
            if 'weapon' in usething.keys():
                if isFighting:
                    if abs(usething['energy']) > energy:
                        print("you don't have enough energy to do that. Eat some food!")
                        use = False
                    else:
                        print("you hit the boss with your " + thingy + '.')
                        energy += usething['energy']
                        damage += usething['damage']
                        use = True
                        isFighting = True

                else:
                    print("you can only use a weapon in combat.")
                    use = False

            if 'health' in usething.keys():
                if health == total_health and abs(usething['health']) == usething['health']:
                    print("you are already at max health.")
                    use = False

                if abs(usething['health']) == usething['health']:
                    for i in range(usething['health']):
                        if health < total_health:
                            health += 1
                            use = True
                        else:
                            pass

                else:
                    health += usething['health']
                    use = True
                    if health <= 0:
                        gameOver()
                        break

            if 'total_health' in usething.keys():
                total_health += usething['total_health']
                use = True

            if 'energy' in usething.keys():
                if abs(usething['energy']) == usething['energy']:
                    energy += usething['energy']
                    use = True

        elif splittable(thingy):
            if thingy.split()[0] == 'all' and thingy.split(None,1)[1] in carrying:
                usething = items[thingy.split(None,1)[1]]
                numberOfItem = carrying.count(thingy.split(None, 1)[1])
                if 'weapon' in usething.keys():
                    print('you can\'t do that.')
                    use = False

                if 'health' in usething.keys():
                    if health == total_health and abs(usething['health']) == usething['health']:
                        print("you are already at max health.")
                        use = False

                    if abs(usething['health']) == usething['health']:
                        for i in range(usething['health'] * numberOfItem):
                            if health < total_health:
                                health += 1
                                use = True
                            else:
                                pass

                    else:
                        health += usething['health']
                        use = True
                        if health <= 0:
                            gameOver()
                            break

                if 'total_health' in usething.keys():
                    total_health += usething['total_health'] * numberOfItem
                    use = True

                if 'energy' in usething.keys():
                    if abs(usething['energy']) == usething['energy']:
                        energy += usething['energy'] * numberOfItem
                        use = True
            else:
                print('you don\'t have that.')
        else:
            print('you don\'t have that.')

        if not isFighting and use:
            try:
                carrying.remove(thingy)
                print("you used the " + thingy + '.')
            except:
                print('you used all of your ' + thingy.split(None, 1)[1])
                for i in range(numberOfItem):
                    carrying.remove(thingy.split(None, 1)[1])

        if not use:
            fightPause = True

        else:
            print("health: " + str(health) + '/' + str(total_health) + '.')
            print("energy: " + str(energy))

    #inventory
    elif enter.lower() in inventory:
        lookinventory()
        fightPause = True

    #knowabout
    elif enter.lower() in items.keys():
        knowabout(command)
        fightPause = True

    #look around
    elif enter.lower() in look:
        fightPause = True
        print("you are in box " + str(xcoord) + "x, " + str(ycoord) + "y.")

        if coord in places.keys() and not isFighting:
            if places[coord]:
                print("there is a chest. In it, you find:")
                print(', '.join(places[coord]))

            else:
                print("there is nothing here.")

        else:
            if isFighting:
                if genbosses[coord]['alive']:
                    current_boss = genbosses[coord]['name']
                    print("you see a level " + str(bosses[current_boss]['level']) + " boss: " + current_boss)
                    print("- " + current_boss + "'s stats -")
                    print("boss health: " + str(boss_health) + '/' + str(bosses[current_boss]['health']))
                    print("boss damage: " + str(bosses[current_boss]['damage']))
                    print(bosses[current_boss]['desc'])

                else:
                    print('there is nothing here.')
            else:
                print('there is nothing here.')

    #fusion
    elif command in fuse:
        if thingy in carrying:
            if fusion(thingy):
                print("you fused 3 of your " + thingy + ' into a ' + items[thingy]['fusion'] + '.')
            elif 'fusion' not in items[thingy]:
                print('that item cannot be fused.')
            else:
                print('you need 3 of that item to fuse it!')


        elif splittable(thingy):
            if thingy.split(None, 1)[1] in carrying and thingy.split()[0] == 'all' and carrying.count(thingy.split(None, 1)[1]) > 2:
                numberOfItem = carrying.count(thingy.split(None, 1)[1])
                for i in range(numberOfItem // 3):
                    if fusion(thingy.split(None, 1)[1]):
                        pass

                if (numberOfItem // 3) > 1:
                    print('you fused ' + str((numberOfItem // 3) * 3) + ' of your ' + plural(thingy.split(None, 1)[1]) + ' into ' + str(numberOfItem // 3) + ' ' + plural(items[thingy.split(None, 1)[1]]['fusion']) + '.')
                else:
                    print('you fused ' + str((numberOfItem // 3) * 3) + ' of your ' + thingy.split(None, 1)[1] + ' into ' + str(numberOfItem // 3) + ' ' + items[thingy.split(None, 1)[1]]['fusion'] + '.')

            elif thingy.split(None, 1)[1] not in items.keys():
                print("-+- error -+-")
                print("what you said could not be understood")
                print("help for commands!")

            elif 'fusion' not in items[thingy.split(None, 1)[1]].keys():
                print('that item cannot be fused.')

            else:
                print('you need 3 of that item to fuse it!')
        else:
            print("-+- error -+-")
            print("what you said could not be understood")
            print("help for commands!")
        fightPause = False

    #save + load
    elif enter.lower() == 'save':
        save()
        fightPause = True
        print("saved! do not delete the 'saves' file and the 'box arena files' file!")

    elif enter.lower() == 'load':
        try:
            os.chdir('box arena files')
        except:
            pass
        try:
            load()
        except:
            try:
                load(False)
            except:
                print('you don\'t have any saves!')

        os.chdir('..')

        fightPause = True

    #help menu
    elif enter.lower() == 'help':
        helpmenu()
        fightPause = True

    #prestige
    elif enter.lower() == 'prestige':
        print("your prestige level is " + prestige + ".")
        fightPause = True

    #troubleshoot
    elif command == 'tbs':
        if thingy.split()[0] == 'energy':
            try:
                energy += int(thingy.split()[1])
            except:
                print('failed did you type something wrong?')

        if thingy.split()[0] == 'health':
            try:
                health += int(thingy.split()[1])
            except:
                print('failed did you type something wrong?')

        if thingy.split()[0] == 'total':
            try:
                total_health += int(thingy.split()[1])
            except:
                print('failed did you type something wrong?')


        if thingy.split()[0] == 'give':
            carrying.append(thingy.split(None, 1)[1])

        fightPause = True

    #peek
    elif command == 'peek':
        if thingy in directions:
            if isFighting:
                fightPause = False
            else:
                fightPause = True
            place, peekcoord = peek(thingy)
            if place == 'none':
                pass
            if place == 'boss':
                seenbosses.append(peekcoord)
                if peekcoord in genbosses.keys():
                    seen_boss = genbosses[peekcoord]['name']
                else:
                    seen_boss = fight(pickValue(int(peekcoord.split()[0]), int(peekcoord.split()[1])), peekcoord)
                    genbosses[peekcoord] = {}
                    genbosses[peekcoord]['name'] = seen_boss
                    genbosses[peekcoord]['alive'] = True
                print("you see a level " + str(bosses[seen_boss]['level']) + " boss: " + seen_boss)
                print("- " + seen_boss + "'s stats -")
                print("boss health: " + str(bosses[seen_boss]['health']) + '/' + str(bosses[seen_boss]['health']))
                print("boss damage: " + str(bosses[seen_boss]['damage']))
                print(bosses[seen_boss]['desc'])
                if peekcoord in places.keys():
                    print('yhere are items on the ground.')
                else:
                    pass
            if place == 'loot':
                if peekcoord in places.keys():
                    pass
                else:
                    places[peekcoord] = generateLoot(int(peekcoord.split()[0]), int(peekcoord.split()[1]), isCoward)

            elif place == 'been':
                print('you\'ve been there before.')

            if peekcoord in places.keys() and place != 'none':
                if places[peekcoord]:
                    print('there is a chest.')
                elif place == 'boss':
                    pass
                else:
                    print('there is nothing here.')

        else:
            fightPause = True
            print("-+- error -+-")
            print("what you said could not be understood")
            print("help for commands!")

    #info menu
    elif command == 'info':
        info()

    #error message
    else:
        print("-+- error -+-")
        print("what you said could not be understood")
        print("help for commands!")

        fightPause = True
