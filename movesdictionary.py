Move_dictionary = {"ember" :"hp.20", "smoke_screen": "ac.4",
"sand_attack": "ac.4",
"growl": "at.4",
"takle": "hp.20",
"harden": "df.4",
"scratch": "hp.20",
"tailwhip": "df.4",
"peck": "hp.20",
"bite": "hp.20",
"wrap": "ac.4"}

print(Move_dictionary.get("bite"))
move_stat1 = Move_dictionary.get("bite")
move_stat2 = move_stat1.split(".")
print(move_stat2)