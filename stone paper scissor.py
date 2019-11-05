import random
a=['stone','paper','scissor']
player=0
n=0
computer=0
while n<4:

    player_option=input('stone ,paper, scissor')
    computer_option=random.choice(a)
    print('you have entered',player_option)
    print('computer has selected',computer_option)
    if player_option=='stone' and computer_option=='paper':
        computer+=1
        n+=1
    elif player_option=='paper' and computer_option=='stone':
        player+=1
        n+=1
    elif player_option=='stone' and computer_option=='scissor':
        player+=1
        n+=1
    elif player_option=='scissor' and computer_option=='stone':
        computer+=1
        n+=1
    elif player_option=='scissor' and computer_option=='paper':
        player+=1
        n+=1
    elif player_option=='paper' and computer_option=='scissor':
        player+=1
        n+=1
    elif player_option==computer_option:
        print('both have entered same option')
        print('try again')
        n+=1
    else:
        print('wrong option entered')
print()
print()
print('------Game over--------')
print('=======Scores are====== ')
print('player : ',player,' points')
print('computer : ',computer,' points')
if player>computer:
    print('player won by ',player-computer,'points')
    print('--congratulations--')
elif computer>player:
    print('sorry computer wins by ',computer-player,'points')
    print('--better luck next time--')
else:
    print('--game tied--')
