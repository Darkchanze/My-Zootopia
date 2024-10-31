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


def get_animal_string(animal_obj):
    output = ""
    output += '<li class="cards__item">'
    if "name" in animal_obj:
        output += f' <div class="card__title">{animal_obj["name"]}</div>\n<p class="card__text"><ul class="no_dots">\n'
    if "diet" in animal_obj["characteristics"]:
        output += f"<li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n"
    if "locations" in animal_obj:
        output += f"<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n"
    if "type" in animal_obj["characteristics"]:
        output += f"<li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n"
    if "type" in animal_obj["characteristics"]:
        output += f"<li><strong>Life span:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n"
    output += "</ul></p>\n</li>"
    return output


def main():
    animals_data = load_json(ANIMALS_FILE)
    animal_string = ''
    for animal_obj in animals_data:
        animal_string += get_animal_string(animal_obj)
    html = read_html(HTML_FILE)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", animal_string)
    write_html(new_html)


if __name__ == "__main__":
    main()