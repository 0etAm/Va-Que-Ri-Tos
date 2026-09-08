# Va-Que-Ri-Tos
Va-Que-Ri-Tos:

A confrontation of cowboys to decide the fate of a decission. 
A simple game that is fun and can be used to take a decission between two persons. It has three actions the user can do: reload, shield and shoot. Similar to rock, paper, scissors, reload works to reload your weapon the times the user wants to, shield is for  being protected by the shooting action, shoot is for shooting the person the user decides.

Instructions:

-Reload: Use it to reload your weapon as meny times you want

-Shield: Use it to protect you from another player shooting

-Shoot: Use it to shoot any player and defeat them

Inputs:
1.- Player's 1 action (1,2 or 3)
2.- Player's 2 action (1,2 or 3)

Process:
1.- Check if both players HP is higher to 0 to start the round
2.- Ask both players their actions
3.- Depending on the selected action, execute a conditional to create the interaction
4.- Check if the reloads or shields are greater than 0 to set them to 0 
5.- Continue the rounds until a player's hp becomes 0 or lower

Outputs:
1.- Display the rules, the interactions and the controls
2.- Display of the current players turn, current round and their stats(quantity of bullets and shield)
3.- Display a message if a player shoots without bullets
4.- If a player HP becomes 0 or lower, display a winning message for the winner
