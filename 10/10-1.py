from pathlib import Path

path = Path("text_files/learning_python.txt")
contents = path.read_text()
print(f"\n{contents}\n")
lines = contents.splitlines()

for line in lines:
    print(f"{line}\n")