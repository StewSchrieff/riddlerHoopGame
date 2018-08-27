import math
import random

import seaborn
import matplotlib.pyplot as plt

def get_A_score_by_pos(playerApick):

    # playerApick = 0
    playerBpick = 0
    playerCpick = 0

    playerAscore = 0
    playerBscore = 0
    playerCscore = 0


    stage = range(1,11)
    # for link in stage:
    #     print(link)


    # avail = range(1,11)


    # playerApick = random.choice(stage)
    print('Player A Chose: ' + str(playerApick))
    if(playerApick != 10):
        playerBChoiceUp = playerApick + 1
    else:
        # if there is not a choice greater than A's choice
        playerBChoiceUp = -1
    if(playerApick != 1):
        playerBChoiceDown = playerApick -1
    else:
        # if there is not a choice less than
        playerBChoiceDown = -1

    playerBChoiceUpValue = 0
    playerBChoiceDownValue = 0
    for val in stage:
        if (val < playerApick):
            playerBChoiceUpValue = playerBChoiceUpValue + val
            chooseBUp = True
        if (val > playerApick):
            playerBChoiceDownValue = playerBChoiceDownValue + val
            chooseBUp = False

    playerBScore = max(playerBChoiceUpValue, playerBChoiceDownValue)
    playerAScore = playerApick + min(playerBChoiceUpValue, playerBChoiceDownValue)
    # print(playerBChoiceUpValue)
    # print(playerBChoiceDownValue)

    # if(chooseBUp):
    #     print('Player B Chose: ' + str(playerApick + 1))
    # else:
    #     print('Player B Chose: ' + str(playerApick - 1))

    # print('Player Bs score is ' + str(playerBScore))
    # print('Player As score is ' + str(playerAScore))
    return playerAScore


list = []
for i in range(1,11):
    list.append(get_A_score_by_pos(i))


print(list)
# with two players, the second player always wins, i guess
plt.scatter(x=range(1,11), y=list)
plt.show()





