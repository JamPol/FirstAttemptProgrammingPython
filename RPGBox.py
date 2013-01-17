import random
import time

#Gets character name
print ('Welcome to Broken Crystal')
print ('Please input character name: ')
char_name = input('>')
if len(char_name) < 1:
    while len(char_name) < 1:
        print ("Your name isn't long enough, please try again: ")
        char_name = input('>')
print ('Welcome to your story, ' + char_name)

time.sleep(1)

#Gets race
print ("\nOf which race were you born:")
print (' (1)Human\n (2)Elf\n (3)Dragonborn')
choice = input('>')

if choice == '1':
    char_race = 'Human'
elif choice == '2':
    char_race = 'Elf'
elif choice == '3':
    char_race = 'Dragonborn'

time.sleep(1)

#Gets class
print ('\nWhich path will you follow:')
print (' (1)Fighter\n (2)Ranger\n (3)Wizard')
choice = input('>')

if choice == '1':
    char_class = "Fighter"
elif choice == '2':
    char_class = "Ranger"
elif choice == '3':
    char_class = "Wizard"

time.sleep(1)

#Gets character stats
count = 0
print ("\nI will now roll stats for your character")
while count <= 6:
    dice1 = random.randint (1,6)
    dice2 = random.randint (1,6)
    dice3 = random.randint (1,6)
    dice4 = random.randint (1,6)
    dice_total = dice1 + dice2 + dice3 + dice4
    dice_total = dice_total - min(dice1, dice2, dice3, dice4)

    if count == 0:
        char_str = dice_total
    if count == 1:
        char_dex = dice_total
    if count == 2:
        char_con = dice_total
    if count == 3:
        char_int = dice_total
    if count == 4:
        char_wis = dice_total
    if count == 5:
        char_chr = dice_total

    count += 1

    if count == 6:

        print ("\nStats:")
        print ("Strength: " + str(char_str) + "\nDexterity: " + str(char_dex) + "\nConstitution: " + str(char_con))
        print ("Intelligence: " + str(char_int) + "\nWisdom: " + str(char_wis) + "\nCharisma: " + str(char_chr))
        print ("\nWould you like to accept these stats(y/n)?: ")
        user_input = input('>')
        if user_input == ("y"):
            break
        if user_input != ("y"):
            count = 0

#Adjusts for racial bonuses
if char_race == "Dragonborn":
    char_str += 2
    char_chr += 2
    print ("\nYour stats have been adjusted for Dragonborn (+2 Charisma, +2 Strength)")
if char_race == "Elf":
    char_dex += 2
    char_wis += 2
    print ("\nYour stats have been adjusted for your Elven race (+2 Dexterity, +2 Wisdom)")
if char_race == "Human":
    print ("\nAs a Human you can choose which ability score you'd like to add +2 to:")
    print ("(1)Strength\n(2)Dexterity\n(3)Constitution\n(4)Intelligence\n(5)Wisdom\n(6)Charisma")
    user_input = input('>')
    user_input = int(user_input)

time.sleep(1)

if char_race == "Human":
    if user_input > 6:
        while user_input > 6:
            print ("That value is too high, please enter another: ")
            user_input = input ('>')
            user_input = int (user_input)
        
    if user_input == 1:
        char_str += 2
        print ("Your Strength has been increased by 2")
    if user_input == 2:
        char_dex += 2
        print ("Your Dexterity has been increased by 2")
    if user_input == 3:
        char_con += 2
        print ("Your Constitution has been increased by 2")
    if user_input == 4:
        char_int += 2
        print ("Your Intelligence has been increased by 2")
    if user_input == 5:
        char_wis += 2
        print ("Your wisdom has been increased by 2")
    if user_input == 6:
        char_chr += 2
        print ("Your Charisma has been increased by 2")

#Get skills
count = 0
char_skills = []
choice_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Intimidate", "Perception", "Streetwise"] 

print ("\nYou may choose three of the following skills:")
print ("(1)Acrobatics\n(2)Athletics\n(3)Endurance\n(4)Heal\n(5)Intimidate\n(6)Perception\n(7)Streetwise")
while count < 2:
    user_input = input('>')
    user_input = int(user_input)
    if user_input > 7:
        print ("Sorry please pick another: ")
    elif choice_skills[user_input -1] in char_skills:
        print ("Sorry please pick another: ")
    else:
        char_skills.append(choice_skills[user_input -1])
        count += 1
        if count <= 2:
            print ("An excellent choice, and for your next choice: ")

time.sleep(1)

#Game locations
def intro():
    global pos_down
    pos_down = True
    
    print ("\nYou awake to the sun rising and the sound of the roosters cock-a-doodle-doo.")
    input ('Press any key to continue')
    print ('You hear a shout from downstairs "' + char_name + " it's time to help your father!" + '"')
    input ('Press any key to continue')
    print ("In order to move downstairs type 'down'")
    
def home():
    global inv
    global pos_north
    pos_north = True

    print ('\nAs you move downstairs you hear your mother greeting you')
    input ('Press any key to continue')
    print ('\n"Good morning ' + char_name + '"')
    print ('"Your father needs you to clear the cave north of here"')
    print ('"Here, take this dagger with you"')
    input ('Press any key to continue')
    print ('\n-You have acquired a dagger-')
    input ('Press any key to continue')
    input ("\nIn order to move to the fields type 'north'")
    input ('Press any key to continue')

    inv.append("dagger")

def field():
    global pos_north
    pos_north = True

    print ("\nYou move towards your father working the fields")
    print ("Morning! I need you to go clear out the caves up north")
    print ("It shouldn't be any problem for you! Be sure to use your dagger")
    print ("\nTo equip your dagger type 'equip dagger'")
    print ("\nOnce you have your dagger equipped, continue north to the caves enterance")

#Game main

def check_pos():
    global pos_x
    global pos_y
    global pos_z
    if pos_x == 0 and pos_y == 0 and pos_z == 1:
        intro()
    if pos_x == 0 and pos_y == 0 and pos_z == 0:
        home()
    if pos_x == 0 and pos_y == 1 and pos_z == 0:
        field()

def main():
    global pos_x
    global pos_y
    global pos_z
    
    global pos_west
    global pos_east
    global pos_north
    global pos_south
    global pos_up
    global pos_down
    global move_count

    
    game = True
    while game == True:
        command = input(">")

        if command == "quit":
            game = False

        if command[:5] == "equip":
            selected_item = command[6:]
            if selected_item in inv:
                inv.remove(selected_item)
                equipped.append(selected_item)
                print ("You have equipped", selected_item)
                
        if pos_west == True:
            if command == "west":
                pos_x -= 1
                pos_west = False
                move_count += 1
        elif pos_east == True:
            if command == "east":
                pos_x += 1
                pos_east = False
                move_count += 1
        elif pos_north == True:
            if command == "north":
                pos_y += 1
                post_north = False
                move_count += 1
        elif pos_south == True:
            if command == "south":
                pos_y -= 1
                pos_south = False
                move_count += 1
        elif pos_down == True:
            if command == "down":
                pos_z -= 1
                pos_down = False
                move_count += 1
        elif pos_up == True:
            if command == "up":
                pos_z += 1
                pos_up = False
                move_count +=1
        if move_count == 1:
            move_count -= 1
            check_pos()

#Starting variable for game

inv = ["apple"]
equipped = []

move_count = 1
pos_x = 0
pos_y = 0
pos_z = 1
pos_west = False
pos_east = False
pos_north = False
pos_south = False
pos_down = False
pos_up = False
main()
