import random
Flip = int(input("Enter the number, you want to flip the coin:--"))
Turn = Flip
Head = 0
Tail = 0
Base = 2
Result = 1
while Flip != 0:
    Result = Result * Base
    Flip = Flip-1
for i in range(Result):
    Coin = random.randint(0,1)
    if Coin == 1:
        Head = Head + 1
    else:
        Tail += 1
HeadPercent = Head / Turn
TailPercent = Tail / Turn
print(Head)
print(Tail)
print(HeadPercent)
print(TailPercent)