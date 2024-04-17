from pathlib import Path
import json

path = Path("favorite2.json")

if path.exists():
    content = path.read_text()
    favorite = json.loads(content)
    print(f"{favorite} is your favorite number")

else:
    favorite = input("Input your favorite number")
    path = Path("favorite2.json")
    contents = json.dumps(favorite)
    path.write_text(contents)