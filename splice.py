#import mods
import random
import os
import csv

#used pokemon variables
pokemon1 = 0          #users pokemon
p1hp =0                 # hit points
p1df = 0               # Defense
p1ak = 0               # Attack
p1move = []             # moves
pusedmove = []
pokemon2 = 0           # computer pokemon stats
p2hp = 0
p2df =0
p2ak =0
p2move = []


                                                        # Import pokemons stats from pokebanl csv file

CSV_PATH = os.path.join("pobank2.csv")


Pokemon = []
HP = []
Defense = []
Atack = []
Moves = []

# example output
# [0] charizard 
# [1] pidgey
 
os.chdir(os.path.dirname(os.path.realpath(__file__))) # adjust path

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    caracter_data = list(csvreader)   # save all data to caracter_data


 
for i, caracter in enumerate(caracter_data):
   
    caracter_name = caracter[0]
    caracter_display = f"[{i}] {caracter_name}"
    print(caracter_display) 


                                                         #     Select   user Pokemon and import stats                                                     
selected_pokemon = input("enter the number of your pokemon") 
pokestats1 = caracter_data[int(selected_pokemon)]  # create array of chosen pokemon stats
pokemon1 = pokestats1[0]               ## assign pokemon stats to active pokemon variable
p1hp =pokestats1[1]                 
p1df = pokestats1[2]              
p1ak = pokestats1[3]               
#p1 move =
CSV_PATH = os.path.join("pobank2.csv") # set path 
os.chdir(os.path.dirname(os.path.realpath(__file__))) #adjust path
with open(CSV_PATH) as csvfile:         # open pokebank
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    caracter_data = list(csvreader)   # save all data to caracter_data 
 #asighn index [4]  to variable                          
pokestats1 = caracter_data[int(selected_pokemon)]   # importing pokemons stats
move = pokestats1[4]   # capture the move value(index 4) of pokemon stats
p1move = move.split(".")   # Split index4 into l
print(p1move)  
                                                 # Select random pokemon for pc
pokestats2 = caracter_data[random.randrange(9)]  # random selected from csv file
pokemon2 = pokestats2[0]          # assign variables for selected pokemon
p2hp = pokestats2[1]
p2df = pokestats2[2]
p2ak = pokestats2[3]
#computer pokemon moves importation
CSV_PATH = os.path.join("pobank2.csv") # set path 
os.chdir(os.path.dirname(os.path.realpath(__file__))) #adjust path
with open(CSV_PATH) as csvfile:         # open pokebank
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    caracter_data = list(csvreader)   # save all data to caracter_data 
 #asighn index [4]  to variable  
print(pokestats2)                        
move2 = pokestats2[4]
p2move = move2.split(".")
print(p2move)
   


                                                 #impot move atributes 
CSV_PATH = os.path.join("moves.csv")


 
print(__file__)
os.chdir(os.path.dirname(os.path.realpath(__file__))) # adjust path

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    moves_data = list(csvreader)   # save all data to caracter_data


 
for i, movstat in enumerate(moves_data):
   
    move_name = movstat[0]
    move_display = f"[{i}] {move_name}"
    print(moves_data)
    
                                             # enter combat while loop           
while (int(p2hp) > 0) and (int(p1hp) > 0):              # while loop continues while hp is over zero
    print(str(pokemon1) + str(p1hp) + "_____________" + str(pokemon2) + str(p2hp) )  # state turns starting hp values
    print(str(pokemon1) +  "  turn")
    print(str(pokemon1 + "  moves"))
 # print moves and pick   
    for moves in p1move:
         print(f'[{str(p1move.index(moves))}] {moves}')
    movechoice = input("pick move 1 or 0")
    pusedmove.append(movechoice)
    print("pica used.... " + p1move[int(movechoice) ] )
  #  move results calculation
    if movechoice == "0":
        results = tackle - onyxd
        print("onyx looses" + str(results) + " health" )
        if (results > 0):
            onyxhp = onyxhp - results
        print("onyx health is now  " + str(onyxhp) + " points")
    if movechoice == "1":
        results = onyxd - tailwip
        print("onyx looses " + str(results) + " defense")
        onyxd = onyxd - results
        print(onyxd)
    print("onyx's Turn")
# Pick random move for other pokemon
    movechoice = random.randrange(2)

    pusedmove.append(movechoice)
    print("onyx used.... " + onyxmove[int(movechoice) ] )
 # Clculate move results  
    if movechoice == 0:
        print("onyx gains" + str(harden) + " defense" )
        onyxd = onyxd + harden
        print("onyx defense is now  " + str(onyxd) + " points")
    if movechoice == 1:
        results = tackle - picad
        print("pica looses " + str(results) + " health")
        picahp = picahp - results
        print("pica health is now  " + str(picahp) + " points")
# when while loop is complete anounce victor
if (picahp < 0):
        print("Pica looses")
if (onyxhp < 0):
     print("onyx looses")                                                    