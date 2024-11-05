from random import randint
player = input('choose rock, paper or scissors')
bot = randint(0,2)
if bot == 0:
    bot = 'rock'
elif bot == 1:
    bot = 'paper'
else:
    bot = 'scissors'
while player != 'rock' and player != 'scissors' and player != 'paper':
    print('Choose again')
    player = input('choose rock, paper or scissors')

if player == bot:
    print('Draw')
if player == 'scissors':
    if bot == 'paper':
        print('You win')
if player == 'scissors':
    if bot == 'rock':
        print('You lose')
if player == 'rock':
    if bot == 'scissors':
        print('You win')
if player == 'rock':
    if bot == 'paper':
        print('You lose')
if player == 'paper':
    if bot == 'rock':
        print('You win')
if player == 'paper':
    if bot == 'scissors':
        print('You lose')
print('You choose:' + player)
print('Bot choose:' + bot)
