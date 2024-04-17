from pathlib import Path
import json

path = Path("favorite.json")
content = path.read_text()
favorite = json.loads(content)
print(f"{favorite} is your favorite number")