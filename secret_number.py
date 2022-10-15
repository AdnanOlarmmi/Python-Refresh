secretNumber = 5
i = 0
while i < 3:
    guess = int(input('Guess: '))
    i += 1
    if guess == secretNumber:
        print("You are right")
        break
else:
    print('You used up all trial')