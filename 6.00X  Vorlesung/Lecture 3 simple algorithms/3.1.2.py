numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10 :
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops-=1
print("number of apples:"+str(numberOfApples))