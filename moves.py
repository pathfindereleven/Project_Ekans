import os
import csv

CSV_PATH = os.path.join("moves.csv")

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header
    move_data = list(csvreader)   # save all data to move_data
for i, move in enumerate(move_data):
   
    move_name = move[0]
    move_display = f"[{i}] {move_name}"
    print(move_display)