import os
import csv

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