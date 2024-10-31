import json


ANIMALS_FILE = "animals_data.json"
HTML_FILE = "animals_template.html"


def load_json(FILE):
    with open(FILE, "r") as handle:
        return json.load(handle)


def read_html(FILE):
    with open(FILE, "r") as handle:
        return handle.read()


def write_html(new_html):
    with open("animals.html","w") as handle:
        handle.write(new_html)


def get_animal_string(animals_data):
    animal_repository = ""
    for animal in animals_data:
        if "name" in animal:
            animal_repository += f"Name: {animal["name"]}\n"
        if "diet" in animal["characteristics"]:
            animal_repository += f"Diet: {animal["characteristics"]["diet"]}\n"
        if "locations" in animal:
            animal_repository += f"Location: {animal["locations"][0]}\n"
        if "type" in animal["characteristics"]:
            animal_repository += f"Type: {animal["characteristics"]["type"]}\n"
        animal_repository += "\n"
    return animal_repository


def main():
    animals_data = load_json(ANIMALS_FILE)
    animals_string = get_animal_string(animals_data)
    html = read_html(HTML_FILE)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_html(new_html)


if __name__ == "__main__":
    main()