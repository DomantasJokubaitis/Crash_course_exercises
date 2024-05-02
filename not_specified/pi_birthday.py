from pathlib import Path

path = Path("text_files/one-million.txt")
contents = path.read_text().splitlines()
pi_string = ""

for line in contents:
    pi_string += line.strip()


x = input("Input your birthday date as DDMMYY: ")
if x in pi_string:
    print("Congrats, your date is in pi! ")
    print(f"Starting at index {pi_string.find(x)}")
else:
    print("Womp womp")