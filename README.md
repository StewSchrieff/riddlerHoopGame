# Riddler August 24, 2018 - Hoop Game

This repository hosts some code that can be used to simulate and analyze the hoop game described in this week's [Riddler](https://fivethirtyeight.com/features/how-many-hoops-will-kids-jump-through-to-play-rock-paper-scissors/).

## Rule Interpretations

There is some ambiguity regarding the exact rules of this game. Well...ambiguity regarding how to translate this game into a simulation.

- In real life, it is intuitive that you just keep hopping as soon as you beat another player in rock paper scissors. However,
when simulating a game, it is not clear whether the game of rock paper scissors and the winning hop are made at the same 'time'.
For this simulation, this is deemed allowable. 

- Another rule that doesn't translate well - when is the game over? Of course, the game is over when one team reaches the 'base' 
hoop of the other team. However, this is also not so clear. Must you win a game of Rock Paper Scissors in the last hoop? 
Or is the last hoop good enough to win? 
  - This simulation regards arriving in the last hoop as winning the game. 
  - This is made easier by also assuming that winning a game of rock paper scissors allows you to progress.



## Method
The simulation is housed in [rockPaperScissors.py](rockPaperScissors.py). 

In general, [rockPaperScissors.py](rockPaperScissors.py) very quickly simulates games of rock-paper-scissors-hop. For each game,
we record the number of steps it took to end the game and the winner. We repeat this process for a given number of hoops.
We then record the mean and median of this set of games with the same number of hoops. We repeat this process up to 600 
times to simulate games with hoops up to 600. 



## Conclusions

With the assumptions that my version of rock-paper-scissors-hop suppose, the average number of hoops required to make a game last 30 minutes (1800 steps) is about 112 hoops.

Of note - as you increase in number of hoops, the variability of the game increases. This causes the simulation to become 
less accurate as hoops increase. 

This is illustrated by plotting the number of hoops vs the number of steps required to resolve the game.
![alt text](https://github.com/StewSchrieff/riddlerHoopGame/blob/master/justMean_steps.png "Increasing")

Also of note - the length of time required to resolve a game is not a linear function of the number of hoops. Rather, it is a 3rd degree function.

This is highlighted by the following graph.
![alt text](https://github.com/StewSchrieff/riddlerHoopGame/blob/master/smallerFitLine.png "Not-Linear")

Throughout all number of hoops in a game, the median is less than the mean. This is due to the right-skewedness of each game. 
There is a defined minimum number of steps that each game can take - where one team wins all of their rock paper scissors games. 
There is no maximum number of steps that each game can take. It is possible that a game could take infinitely many steps to resolve.
This causes the game to be right skewed, which drags the mean out to be higher than the median. Could be worth thinking about using the median
if you are betting on a game taking exactly 30 minutes. 

## Loose Ends

- If you don't have time to run the data, you can read in the mean/median datasets from [df_mean.csv](df_mean.csv) and [df_median.csv](df_median.csv).
These contain fairly accurate data. 

- [rockPaperScissors.py](rockPaperScissors.py) contains a lot of extraneous code to just running a simulation. 
Feel free to comment-nuke as needed. 

- Feel free to contact me on [twitter](https://twitter.com/Schrewart) with any suggestions or other thoughts. 

## Built With
- [seaborn](https://seaborn.pydata.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](http://www.numpy.org/)