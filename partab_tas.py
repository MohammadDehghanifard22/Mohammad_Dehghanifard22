import random as r

def partab_tas():
    print("welcom in game,i hope you are lucky..!")
    while 1:
     tas=r.randint(1,6)
     game_m=input("for countinu game write:(D) or close the game write:(G)..?")
     if game_m =="G":
         print("i,m happy you played the game good bye.!!")
         break
     elif game_m== "D" :
         print("your tas is.." , tas)
         print("lets play  more...!")
         continue
     else:
         print("please write a correct letters (G) or (D) ?")
         continue
     
partab_tas()    