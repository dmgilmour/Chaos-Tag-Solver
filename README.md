# Chaos-Tag-Solver

## Problem:

There are N players of Chaos Tag. Whenever a player is tagged, they become inactive and can no longer play. A player becomes active again when the player who tagged them is tagged. The game ends when there is only one player remaining. Find the pattern for average number of tags needed to complete and number of players. (Note: if there are two players left and one is tagged, the players rendered inactive by the last tagged player become active before the game ends)

## Solution

The pattern is: Average number of tags = (2^(N - 1)) - 1

Eg:  
2 : 1  
3 : 3  
4 : 7  
5 : 15  
6 : 31  
7 : 63  
... 
