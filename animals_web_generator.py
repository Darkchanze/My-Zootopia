import json


ANIMALS_FILE = "animals_data.json"
HTML_FILE = "animals_template.html"


def load_json(FILE):
    """Load json ANIMALS_FILE and returns the file as a list of dictionarys."""
    with open(FILE, "r") as handle:
        return json.load(handle)


def read_html(FILE):
    """Reads the HTML_FILE and returns it as a sting."""
    try:
        with open(FILE, "r") as handle:
            return handle.read()
    except FileNotFoundError:
        print("The ANIMALS_FILE was not found.")
    except PermissionError:
        print("You do not have permission to read ANIMALS_FILE.")
    except UnicodeDecodeError:
        print("Could not decode the ANIMALS_FILE content.")
    except IOError:
        print("An I/O error occurred.")

def write_html(new_html):
    """Write a new_html file based on HTML_FILE. Contains the changes made to the html in the program."""
    with open("animals.html","w") as handle:
        handle.write(new_html)


def get_animal_string(animal_obj):
    """Animal_obj contains the list of dictionarys from ANIMALS_FILE. Here we create the output which
    will be displayed later in the new_html. We check if dictionary info for each animal contains certain
    data like the location, if so we add it to output. The gathered information is thn returned"""
    output = ""
    output += '<li class="cards__item">'
    characteristics = animal_obj["characteristics"]
    if "name" in animal_obj:
        output += f' <div class="card__title">{animal_obj["name"]}</div>\n<p class="card__text"><ul class="no_dots">\n'
    if "diet" in characteristics:
        output += create_html_list_sections("Diet", characteristics["diet"])
    if "locations" in animal_obj:
        output += create_html_list_sections("Location", animal_obj["locations"][0])
    if "type" in characteristics:
        output += create_html_list_sections("Type", characteristics["type"])
    if "lifespan" in characteristics:
        output += create_html_list_sections("Life span", characteristics["lifespan"])
    output += "</ul></p>\n</li>"
    return output


def create_html_list_sections(attributes, data):
    """Gets the infos for the HTML line and puts it into the HTML string and then returns it."""
    return f"<li><strong>{attributes}:</strong> {data}</li>\n"


def print_list_of_skin_types(animals_data):
    """From the data of the ANIMALS_FILE we print hair types available for the user_input by checking which
    skin types are available from the searched animals."""
    list_of_hairtypes = set()
    for animal in animals_data:
        if "skin_type" in animal["characteristics"]:
            list_of_hairtypes.add(animal["characteristics"]["skin_type"])
    for hairtype in list_of_hairtypes:
        print(hairtype)

def get_skin_type_user():
    """Get the skin type from user input. Try to get input as long as it is correct."""
    while True:
        skin_type = input("Enter a skin type form above: ")
        if skin_type == "Fur" or skin_type == "Scales" or skin_type == "Hair":
            return skin_type


def main():
    animals_data = load_json(ANIMALS_FILE)
    animal_string = ''
    print_list_of_skin_types(animals_data)
    skin_type = get_skin_type_user()
    for animal_obj in animals_data:
        if animal_obj["characteristics"]["skin_type"] == skin_type:
            animal_string += get_animal_string(animal_obj)
    html = read_html(HTML_FILE)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", animal_string)
    write_html(new_html)


if __name__ == "__main__":
    main()