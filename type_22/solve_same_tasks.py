from os import listdir
from os.path import join, isfile
from pathlib import Path


files_dir = join(Path(__file__).parent, 'files')
root = Path(__file__).parent
print(join(files_dir, "files"))
ids = [f.replace(".csv", '') for f in listdir(files_dir) if isfile(join(files_dir, f)) if Path(f).suffix == ".csv"]
with open("47226.py", 'rt') as f:
    text = f.read()
for id in ids:
    with open(f"{id}.py", 'wt', encoding="utf-8") as f:
        f.write(text.replace("47226.csv", f"{id}.csv"))
