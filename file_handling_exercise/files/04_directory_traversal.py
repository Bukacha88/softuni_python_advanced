import os
from pathlib import Path


def extract_files(directory):
    return [el for el in directory if "." in el]


def file_extensions(files):
    ext = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in ext:
            ext[extension] = []
        ext[extension].append(file_name)
    return ext


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = file_extensions(files)

result = ""

for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result += f"{extension}\n"
    for name in file_names:
        result += f"- - - {name}{extension}\n"


home = str(Path.home())
path = os.path.join(home, "report.txt")

with open(os.path.expanduser(path), "w") as file:
    file.write(result)