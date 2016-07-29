import requests
import json

def print_pokemon(pokemon):
    print('Name: ' + pokemon['name'].capitalize())
    print('Height: ' + str(pokemon['height']))
    print('Weight: ' + str(pokemon['weight']))

    type_string = ''
    for index, current_type in enumerate(pokemon['types']):
        type_string += current_type['type']['name'].capitalize()
        if index < (len(pokemon['types']) - 1):
            type_string += ", "
    print('Types: ' + type_string)

def main():
    response = requests.get('http://pokeapi.co/api/v2/pokemon/').json()
    pokemon_list = response['results']

    for index, pokemon in enumerate(pokemon_list):
        print(str(index) + " - " + pokemon['name'])

    while True:
        try:
            pokemon_selection = int(input("Which pokemon would you like to learn more about? "))

        except ValueError:
            print("WATTTTTT")
            #better try again... Return to the start of the loop
            continue
        else:
            if pokemon_selection > 19 or pokemon_selection < 0:
                print('Number not in range. Please try again.')
                continue

            print(" ")
            # ze pokemon has been selected
            break

    chosen_pokemon_data = requests.get(pokemon_list[pokemon_selection]['url']).json()
    print_pokemon(chosen_pokemon_data)


main()
