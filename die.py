import random
rollhistory = []
i = 0 
while i <= 50 : 
        diceroll =random.randint (1,6)   
        input("Roll The Dice")
        print(f"You rolled {diceroll}")
        i+= diceroll
        rollhistory.append(diceroll)
        print (rollhistory)
