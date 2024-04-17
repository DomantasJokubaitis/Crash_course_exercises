from pathlib import Path
import json


favorite = input("Input your favorite number")
path = Path("favorite.json")
contents = json.dumps(favorite)
path.write_text(contents)
