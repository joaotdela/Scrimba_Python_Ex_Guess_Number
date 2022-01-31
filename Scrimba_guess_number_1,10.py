# Scrimba Guess the number code 1...10


import random
times_guess = 0
guess_limit = 3
while times_guess < guess_limit:
    times_guess += 1
    n = input('Guess the number 1-10: ')
    print(n)
    c = random.randrange(1, 10)
    if int(n) != int(float(c)):
        print('the number was wrong')
    else:
        print('You win')
        times_guess = guess_limit
if n != c:
    print(f'You lose! the number: {c}! Your last guess was: {n}')
