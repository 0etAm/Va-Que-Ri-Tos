Va-Que-Ri-Tos:

A duel between two players. VA-QUE-RI-TOS is a 2 player turn based game that has two modes: “Normal mode” and “Powers mode”. In both modes each player has three actions available to do: reload, shield and shoot. Similar to “rock, paper, scissors”, reload works to “reload” your weapon up to three times in a row, “shield” protects the player who used it from the other player “shoot”, and “shoot” is for shooting the person the user decides.

Normal mode:

In “Normal mode” each player has a total of 100hp, (for example) if a player1 shoots player2, and the player2 does not have a shield, player2 hp will come down to 0 and automatically and player1 win, and player2 lose. There is a case where both players shoot each other without any shield and finish in a draw.

Powers mode:

In “Powers mode” the normal rules, actions and interactions from “Normal mode” stay, and powers are added. Every three rounds each player will receive 3 random powers, and their function will be displayed next to the actions. If after the three next rounds the first power displayed isn’t used, it will disappear and a new one will be added instead. 

The powers are the next:

1: "White album (Double Shield)"

2: "Sex pistols (Double shot)"

3: "Hol horse (Double reload)"

4: "Mountain tim (Steal a shield from the other player)"

5: "King crimson (Gives you a free turn shield)"

6: "C moon (The opponent's next shot will be directed to itself)"

7: "Metallica (The opponent's shot will be cancelled)"

8: "The World (The opponent can't act next turn)"

9: "Killer queen (Eliminates all the opponent's shields)"

10: "Kars (Become invincible for 1 turn)"

The powers will have interactions amongst the actions and between them.
After ending each match, the user will be asked to accept or decline play again.

Algorithms:

Normal mode instructions:

-Reload: Use it to reload your weapon as many times you want   

-Shield: Use it to protect you from another player shooting

-Shoot: Use it to shoot any player and defeat them

Inputs:

 1.- Player's 1 action (1,2 or 3)
 
 2.- Player's 2 action (1,2 or 3)
 
Process:

1.- Check if both players HP is higher to 0 to start the round

2.- Ask both players their actions

3.- Depending on the selected action, execute a conditional to create the interaction 

4.- Check if the reloads or shields are greater than 3 to set them to 0

5.- Continue the rounds until one or both players hp becomes 0 or lower

6 .- Ask if user want to play again

Outputs: 

1.- Display the rules, the interactions and the controls

2.- Display of the current players turn, current round and their stats(quantity of bullets and shield)

3.- Display a message for each player action and interaction

4.- If a player HP becomes 0 or lower, display a winning message for the winner

5.- Ask if user want to play again (If yes repeat, if not end the program)

Powers mode instructions:

-Reload: Use it to reload your weapon as many times you want

-Shield: Use it to protect you from another player shooting

-Shoot: Use it to shoot any player and defeat them

Inputs:

 1.- Player's 1 action (1,2 or 3)
 
 2.- Player’s 1 power (power assigned number or pass)
 
 3.- Player's 2 action (1,2 or 3)
 
 4.- Player’s 2 power (power assigned number or pass)
 
 3.- Play again input (1 or 2)

Process:

 1.- Check if both players HP is higher to 0 to start the round
 
 2.- Ask both players their actions and powers 
 
 3.- Depending on the selected action and power, execute a conditional to create the interaction 
 
 4.- Check if the reloads or shields are greater than 3 to set them to 0
 
 5.- Every three rounds check if the quantity of powers is greater than 3 to eliminate first and add another
 
 6.- Continue the rounds until one or both players hp becomes 0 or lower
 
 7 .- Ask if user want to play again
 
Outputs: 

1.- Display the rules, the interactions and the controls

2.- Display of the current players turn, current round and their stats(quantity of bullets, shield and powers)

3.- Display a message for each action and interaction between players actions and powers

4.- If a player HP becomes 0 or lower, display a winning message for the winner

5.- Ask if user want to play again (If yes repeat, if not end the program)

How to play:

In order to play VA-QUE-RI-TOS from your terminal (assuming python is already installed) you must follow the next steps in order:

1.-Open the terminal from the search bar or by pressing the Windows key and writing terminal and then pressing enter.

2.-Once in the terminal, write ‘pip install colorful’ and once the message that says colorful has been successfully installed open a new tab in the terminal.

3.-Search in the files where the VA-QUE-RI-TOS folder is and enter it, then right click the VA-QUE-RI-TOS file and select copy path as route.

4.-Go back to the terminal and paste the path, press enter and write ‘py VA-QUE-RI-TOS.py’ and press enter again.

5.-You are ready to play.
