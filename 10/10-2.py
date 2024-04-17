from pathlib import Path

path = Path("text_files/learning_python.txt")
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    print(f"{line.replace("python", "C")}\n")