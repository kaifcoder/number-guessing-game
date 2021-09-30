import random
print('Hello what is your name?')
name=input()
secretnumber = random.randint(1,20)
print('Well, '+name+', I am thinking of a number between 1 and 20')

for guesstaken in range(1,7):
    print('take a guess.')
    guess = int(input())
    if guess<secretnumber:
        print('your guess is low.')
    elif guess>secretnumber:
        print('your guess is high.')
    else:
        break

if  guess == secretnumber:
    print('good job, '+name+'! you guessed my number')
else:
    print('Nope,the number i was thinking was '+str(secretnumber))