import json
from operator import ifloordiv
from plistlib import loads

ANIMALS_FILE = "animals_data.json"

def load_data(ANIMALS_FILE):
    with open(ANIMALS_FILE, "r") as handle:
        return json.load(handle)


def print_data(animals_data):
    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal["name"]}")
        if "diet" in animal["characteristics"]:
            print(f"Diet: {animal["characteristics"]["diet"]}")
        if "locations" in animal:
            print(f"Location: {animal["locations"][0]}")
        if "type" in animal["characteristics"]:
            print(f"Type: {animal["characteristics"]["type"]}")
        print()

def main():
    animals_data = load_data(ANIMALS_FILE)
    print_data(animals_data)



if __name__ == "__main__":
    main()