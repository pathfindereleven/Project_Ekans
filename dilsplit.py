import csv
import os

                                 # this module will import pokebank.csv and sepperate "moves" into an array with interger values
CSV_PATH = os.path.join("pobank2.csv") # set path 
os.chdir(os.path.dirname(os.path.realpath(__file__))) #adjust path
with open(CSV_PATH) as csvfile:         # open pokebank
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    caracter_data = list(csvreader)   # save all data to caracter_data

print(caracter_data) 

 #asighn index [4]  to variable                          
pokestats1 = caracter_data[0]   # importing pokemons stats
 
                                 # isolate last value and split by "."
print(pokestats1)
                                                
move = pokestats1[4]   # capture the move value(index 4) of pokemon stats
print(move)
p1move = move.split(".")   # Split index4 into list of moves
print(p1move)