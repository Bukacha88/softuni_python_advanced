import os


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


def add_content(file_name, content):
    with open(file_name, "a") as file:
        file.write(content+"\n")


def replace_content(file_name, old_string, new_string):
    try:
        with open(file_name, "r+") as file:
            text = "".join(file.readlines())
            new_text = text.replace(old_string, new_string)
            file.seek(0)
            file.write(new_text)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


mapper = {
    "Create": create_file,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file,
}

data = input().split("-")

while not data[0] == "End":
    command, rest_of_data = data[0], data[1:]

    mapper[command](*rest_of_data)
    data = input().split("-")