# TrumpsPython

At the end of the Python & Apps short course, we were tasked with creating a mini-project in group. We were given several project ideas to choose from, and we decided to build a simple game similar to Top Trumps. The objective of our game was for players to pick a stat from their Pokémon card and compare it with the computer's Pokémon card to see who wins.

**Key Steps in the Project:**
 1. Importing Modules: We started by importing two important modules:
- random: This allows us to generate random numbers, which we used to select random Pokémon IDs.
- requests:  This module lets the code ask websites for information and get data from the internet
3. Generating Random Pokémon IDs: Next, we generated two random Pokémon IDs between 1 and 151, corresponding to the original 151 Pokémon.
4. Fetching Pokémon Data: We created a function that takes a Pokémon ID and retrieves data about the Pokémon using the Pokémon API. The function returns key details about the Pokémon, such as:
  -name: The Pokémon's name.
  -id: The Pokémon's ID number.
  -height: The Pokémon's height.
  -weight: The Pokémon's weight.
5.	Player's Choice: The game then prompts Player 1 to choose which stat they want to use for comparison. The available options are:
  -id
  -height
  -weight
The script retrieves the chosen stat for both Player 1's Pokémon and Player 2's Pokémon based on the player's input.
6. Comparing Stats: We created another function to compare the selected stat (either id, height, or weight) between Player 1's Pokémon and Player 2's Pokémon. The function works as follows:
	- If Player 1's stat is greater than Player 2's stat, Player 1 wins.
	- If Player 2's stat is greater than Player 1's stat, Player 1 loses.
  	- If both stats are equal, the result is a draw.
7. Using if __name__ == "__main__":: In this project, I used the if __name__ == "__main__": construct to control the execution flow of the program. This ensures that certain parts of the code are only executed when the script is run directly, rather than when it is imported as a module into another script.

**Testing**
In this project, I wrote unit tests to ensure the correct functionality of the core features. Specifically, I focused on the comparison logic between two Pokémon statistics. The tests check for three scenarios:
 1. Player loses – When the player’s stat is lower than the opponent’s.
 2. Player wins – When the player’s stat is higher than the opponent’s.
 3. Draw – When both players have the same stat value.
I used Python's built-in assert statement to test the functions and verify that the expected outputs match the actual results.


