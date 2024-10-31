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
        animal_repository += '<li class="cards__item">'
        if "name" in animal:
            animal_repository += f' <div class="card__title">{animal["name"]}</div>\n<p class="card__text">\n'
        if "diet" in animal["characteristics"]:
            animal_repository += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]}\n<br/>"
        if "locations" in animal:
            animal_repository += f"<strong>Location:</strong> {animal["locations"][0]}\n<br/>"
        if "type" in animal["characteristics"]:
            animal_repository += f"<strong>Type:</strong> {animal["characteristics"]["type"]}\n<br/>"
        animal_repository += "</p>\n</li>"
    return animal_repository


def main():
    animals_data = load_json(ANIMALS_FILE)
    animals_string = get_animal_string(animals_data)
    html = read_html(HTML_FILE)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_html(new_html)


if __name__ == "__main__":
    main()