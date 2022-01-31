import random
times_guess = 0
guess_limit = 10
c = random.randrange(1, 100)
while times_guess < guess_limit:
    times_guess += 1
    n = input(f'Guess the number 1-100: ')
    print(n)
    if int(n) < c:
        print(f'Is higher number')
    elif int(n) > c:
        print(f'Is lower number')
    else:
        print(f'You win')
        break
if n != c:
    print(f'You lose! the number: {c}! Your last guess was: {n}')
