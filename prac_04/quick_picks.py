import random

how_many = int(input("How many quick picks? "))
quick_picks = []
for i in range(0,how_many,1):
    pick = []
    while len(pick) < 6:
        number = random.randint(1, 45)
        if number not in pick:
            pick.append(number)
    pick.sort()
    quick_picks.append(pick)
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(pick[0],pick[1],pick[2],pick[3],pick[4],pick[5]))
