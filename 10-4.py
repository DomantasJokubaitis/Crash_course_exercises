from pathlib import Path

path = Path("guest.txt")
answer = input("Input your name: ")
path.write_text(answer)
