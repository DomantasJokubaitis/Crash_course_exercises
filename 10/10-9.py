from pathlib import Path


def printing(filenames):
    try:
        contents = path.read_text()
        contents = contents.splitlines()
    except FileNotFoundError:
        pass
    else:
        for animal_name in contents:
            print(f"{animal_name}")

filenames = ["dog_names.txt", "cat_names.txt"]

for filename in filenames:
    path = Path(f"text_files/{filename}")
    printing(path)