import random
import requests



def get_pokemon_data(pokemon_id):
    pokemon_number = pokemon_id
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(url)
    data = response.json()

    return {"name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"]
            }


def compare_stats(stat, stat_player, stat_opponent):
    if stat_player > stat_opponent:
        return (f"Congratulations! You won based on {stat}. "
                f"Your {stat} is {stat_player} "
                f"and your opponents {stat} is {stat_opponent}")
    elif stat_player < stat_opponent:
        return (f"Better luck next time :( You lost based on {stat}. "
                f"Your {stat} is {stat_player} "
                f"and your opponents {stat} is {stat_opponent}")
    elif stat_player == stat_opponent:
        return (f"It's a draw! You drew based on {stat}. "
                f"Your {stat} is the same as your opponent's")
    


if __name__ == "__main__":

    pokemon_id_1 = random.randint(1, 151)
    pokemon_id_2 = random.randint(1, 151)


    pokemonPlayer1 = get_pokemon_data(pokemon_id_1)
    pokemonPlayer2 = get_pokemon_data(pokemon_id_2)

    print(f"Player 1, your Pokemon is: {pokemonPlayer1}")

    stat_to_compare = input("Which stat would you like to use? Please pick id, height or weight: ")
    assert stat_to_compare in ["id", "height", "weight"]

    stat_player_1 = pokemonPlayer1[stat_to_compare]
    stat_player_2 = pokemonPlayer2[stat_to_compare]

    print(f"Player 2's Pokemon is: {pokemonPlayer2}")

    result = compare_stats(stat_to_compare, stat_player_1, stat_player_2)
    print(result)

