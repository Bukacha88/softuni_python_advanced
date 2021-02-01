import re

letter_path = r"[a-z]"
punctuation_path = r"[-,.!?']"


def get_n(line, path):
    return len(re.findall(path, line, re.IGNORECASE))


with open("text.txt", "r") as file:
    with open("output.txt", "w") as file_to_write:
        lines = file.readlines()
        counter = 1
        for line in lines:
            n_letters = get_n(line, letter_path)
            n_punctuations = get_n(line, punctuation_path)
            file_to_write.write(f"Line {counter}: {line.strip()} ({n_letters})({n_punctuations})\n")
            counter += 1
