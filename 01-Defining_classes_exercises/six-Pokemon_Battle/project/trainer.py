class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = list()

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        # if pokemon_name in [p.name for p in self.pokemon]:
        #     self.pokemon = [poke for poke in self.pokemon if not poke.name == pokemon_name]
        #     return f"You have released {pokemon_name}"
        # return "Pokemon is not caught"
        for pokemon in self.pokemon:
            if pokemon.name == pokemon_name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        result += "\n".join([f"- {pokeball.pokemon_details()}\n" for pokeball in self.pokemon])
        return result

