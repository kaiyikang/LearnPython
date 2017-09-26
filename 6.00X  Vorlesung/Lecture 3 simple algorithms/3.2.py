#Find the cube root of a perfect cube
x1 = input('Enter an integer:')
x = int(x1)
ans = 0
while ans**3 < x:
    ans += 1
if ans **3 !=x:
    print(str(x)+' is not a perfect cube')
else:
    print('Cuble root of '+ str(x)+' is '+str(ans))