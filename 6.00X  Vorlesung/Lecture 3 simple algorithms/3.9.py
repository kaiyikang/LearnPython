print('Please think of a number between 0 and 100!')

high = 100
low = 0
ans = int((high +low )/2)

while True:
    print('Is your secret number ' + str(ans) + '?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    i = input()


    if i == 'l': # GuessNumber is lower
        low = ans
        ans = int((low + high) / 2)
    elif i == 'h':
        high = ans
        ans = int((low + high) / 2)
    elif i =='c':
        print('Game over. Your secret number was: ' + str(ans))
        break
    else:
        print('Sorry, I did not understand your input.')








