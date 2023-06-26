import os
import csv

bank = os.path.join("..", "pythonstuff", "pobank.cvs")

Pokemon = []
HP = []
Defense = []
Atack = []
Moves = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # with open(udemy_csv, encoding='utf-8') as csvfile:
with open(bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        # Add place
        Pokemon.append(row[0])

        # Add population
        HP.append(row[1])

        # Add per capita income
        Defense.append(row[2])

        # Add poverty count
        Atack.append(row[3])

        Moves.append(row[4])

        # Zip lists together
cleaned_csv = list(zip(Pokemon, HP, Defense, Atack, Moves, ))

# Set variable for output file
output_file = os.path.join("pobank2.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Pokemon", "HP", 'defense', "atack", "Move"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)




       