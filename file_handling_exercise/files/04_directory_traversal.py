import os


def extract_files(directory):
    return [el for el in directory if os.path.isfile(el)]


def file_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = file_extensions(files)

result = ""

for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result += f"{extension}\n"
    for name in file_names:
        result += f"- - - {name}{extension}\n"

path_to_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop', "report.txt")

with open(path_to_desktop, "w") as file:
    file.write(result)
