import os
import csv

CSV_PATH = os.path.join("pobank2.csv")


Pokemon = []
HP = []
Defense = []
Atack = []
Moves = []

# example output
# [0] charizard 
# [1] pidgey
#dunderfile 
print(__file__)
os.chdir(os.path.dirname(os.path.realpath(__file__))) # adjust path

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    caracter_data = list(csvreader)   # save all data to caracter_data


 
for i, caracter in enumerate(caracter_data):
   
    caracter_name = caracter[0]
    caracter_display = f"[{i}] {caracter_name}"
    print(caracter_display)