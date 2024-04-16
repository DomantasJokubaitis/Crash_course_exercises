from pathlib import Path

path = Path("text_files/The outermost house.txt")
content = path.read_text(encoding="utf-8")

word = "the "
x = 0
for lines in content.splitlines():
    x += lines.count(word)

print(x)