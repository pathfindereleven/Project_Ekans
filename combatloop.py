import random
#onyx's stats
onyxhp = 101
onyxd = 18
onyxa = 5
#pichacu stats
picahp = 100
picad = 5
picaa = 7
# move variables
tackle = 20
tailwip = 4
harden = 10
picamove = ["tackle","tailwip"]
pusedmove = []
onyxmove = ["Harden","tackle"]
ousedmove = []
# while loop to cycle turns til health hit zero
while (onyxhp > 0) and (picahp > 0):
    print("picachu " + str(picahp) + "          onyx" + str(onyxhp) )
    print("pica turn")
    print("pica moves")
 # print moves and pick   
    for moves in picamove:
         print(f'[{str(picamove.index(moves))}] {moves}')
    movechoice = input("pick move 1 or 0")
    pusedmove.append(movechoice)
    print("pica used.... " + picamove[int(movechoice) ] )
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