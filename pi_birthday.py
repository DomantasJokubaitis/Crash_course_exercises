from pathlib import Path

path = Path("text_files/one-million.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line.strip()


x = input("ddmmyy")
if x in pi_string:
    print("Congrats")
else:
    print("Womp womp")