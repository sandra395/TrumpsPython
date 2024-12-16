# TrumpsPython

At the end of the Python & Apps short course, we were tasked with creating a mini-project in group. We were given several project ideas to choose from, and we decided to build a simple game similar to Top Trumps. The objective of our game was for players to pick a stat from their Pokémon card and compare it with the computer's Pokémon card to see who wins.

Key Steps in the Project:
1.	Importing Modules: We started by importing two important modules:
- random: This allows us to generate random numbers, which we used to select random Pokémon IDs.
- requests:  This module lets the code ask websites for information and get data from the internet
3.	Generating Random Pokémon IDs: Next, we generated two random Pokémon IDs between 1 and 151, corresponding to the original 151 Pokémon.
4.	Fetching Pokémon Data: We created a function that takes a Pokémon ID and retrieves data about the Pokémon using the Pokémon API. The function returns key details about the Pokémon, such as:
  -name: The Pokémon's name.
  -id: The Pokémon's ID number.
  -height: The Pokémon's height.
  -weight: The Pokémon's weight.
5.	Player's Choice: The game then prompts Player 1 to choose which stat they want to use for comparison. The available options are:
  -id
  -height
  -weight
The script retrieves the chosen stat for both Player 1's Pokémon and Player 2's Pokémon based on the player's input.
6.	Comparing Stats: We created another function to compare the selected stat (either id, height, or weight) between Player 1's Pokémon and Player 2's Pokémon. The function works as follows:
	- If Player 1's stat is greater than Player 2's stat, Player 1 wins.
- If Player 2's stat is greater than Player 1's stat, Player 1 loses.
  - If both stats are equal, the result is a draw.
7.	Displaying the Result: After the comparison, the game displays the result, showing whether Player 1 won, lost, or if it was a draw based on the chosen stat.
