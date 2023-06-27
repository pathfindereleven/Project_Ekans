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
x = "y"                                                       # Import pokemons stats from pokebanl csv file
while x == "y":
    CSV_PATH = os.path.join("Poke_bank.csv")
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
    CSV_PATH = os.path.join("Poke_Bank.csv") # set path 
    os.chdir(os.path.dirname(os.path.realpath(__file__))) #adjust path
    with open(CSV_PATH) as csvfile:         # open pokebank
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip header
        caracter_data = list(csvreader)   # save all data to caracter_data 
    #asighn index [4]  to variable                          
    pokestats1 = caracter_data[int(selected_pokemon)]   # importing pokemons stats
    move = pokestats1[4]   # capture the move value(index 4) of pokemon stats
    p1move = move.split(".")   # Split index4 into l
                                                    # Select random pokemon for pc
    pokestats2 = caracter_data[random.randrange(9)]  # random selected from csv file
    pokemon2 = pokestats2[0]          # assign variables for selected pokemon
    p2hp = pokestats2[1]
    p2df = pokestats2[2]
    p2ak = pokestats2[3]
    #computer pokemon moves importation
    CSV_PATH = os.path.join("Poke_Bank.csv") # set path 
    os.chdir(os.path.dirname(os.path.realpath(__file__))) #adjust path
    with open(CSV_PATH) as csvfile:         # open pokebank
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip header
        caracter_data = list(csvreader)   # save all data to caracter_data                         
    move2 = pokestats2[4]
    p2move = move2.split(".")
                                                    #impot move atributes 
    CSV_PATH = os.path.join("moves.csv")
    os.chdir(os.path.dirname(os.path.realpath(__file__))) # adjust path
    with open(CSV_PATH) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip header
        moves_data = list(csvreader)   # save all data to moves_data
    for i, movstat in enumerate(moves_data):
        move_name = movstat[0]
        move_display = f"[{i}] {move_name}"
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
        print(str(pokemon1) + "  used..")
        print( p1move[int(movechoice) ] )
        for i in moves_data:
            if i[0] == p1move[int(movechoice) ]: # match used move to move data
                attack_value = i[2]
                attack_target = i[1]       
        if attack_target == "hp":
            p2hp = int(p2hp) - ((int(attack_value) + int(p1ak)) - int(p2df))           # calculate combat results for uced pokemon
            print( str(pokemon2) + "   looses" + str(attack_value) + "  HP")
        if attack_target == "df":
            p2df = int(p2df) - int(attack_value)
            print( str(pokemon2) + "   looses" + str(attack_value) + "  defense")
        if attack_target == "at":
            p2ak = int(p2ak) - int(attack_value)
            print( str(pokemon2) + "   looses" + str(attack_value) + "  attack")
        movechoice2 = random.randrange(2)    # pic random move for pc pokemon
        move2 = pokestats2[4]   # capture the move value(index 4) of pokemon stats
        p2move = move2.split(".")   # Split index4 into l
        print(pokemon2 + " used...") 
        print( str(p2move[int(movechoice2) ]))
        for i in moves_data:
            if i[0] == p2move[int(movechoice2) ]: # match used move to move data
                attack_value = i[2]
                attack_target = i[1]
        if attack_target == "hp":
            p1hp = int(p1hp) - ((int(attack_value) + int(p2ak)) - int(p1df))           # calculate combat results for uced pokemon
            print( str(pokemon1) + "   looses" + str(attack_value) + "  HP")
        if attack_target == "df":
            p1df = int(p1df) - int(attack_value)
            print( str(pokemon1) + " lost " + str(attack_value) + "  defense")
        if attack_target == "at":
            p1ak = int(p1ak) - int(attack_value)
            print( str(pokemon1) + " lost  " + str(attack_value) + "  attack")
        print("_______________________________________________________________________________")
    if int(p1hp) < 0:
        print(str(pokemon1) + " Fainted")
    if int(p2hp) < 0:
        print(str(pokemon2) + " Fainted")
    x = input("play agian ? (y/n)")