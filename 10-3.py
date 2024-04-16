from pathlib import Path

path = Path("text_files/learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(f"{line}\n")

"""
from pathlib import Path

path = Path("text_files/learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(f"{line.replace("python", "C")}\n")
"""
