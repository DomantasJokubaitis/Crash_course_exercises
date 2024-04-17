from pathlib import Path

path = Path("guest2.txt")

contents = ""

while True:
    answer = input("Input your name: ")
    if answer == "stop":
        break
    else: 
        contents += f"{answer}\n"


path.write_text(contents.strip())
    