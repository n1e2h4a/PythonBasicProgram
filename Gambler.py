import random
Stake = int(input('How many stake do you have:--'))
Goal = int(input("what are the goals you want to achieve:--"))
Turn = int(input("how many times you want to bet"))
win = 0
loss = 0
count = 0
while Stake >= 0:
    if Stake == Goal:
        break
    number = random.randint(0, 1)
    if number > .5:
        Stake = Stake+1
        win = win+1
        count = count+1
    else:
        Stake = Stake-1
        loss = loss+1
        count = count+1
WinPercent = win * 100 / count
LossPercent = loss * 100 / count

print(WinPercent)
print(LossPercent)