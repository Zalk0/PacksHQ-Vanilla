import subprocess
from pathlib import Path


images = list(Path('16x-textures').rglob('*.png')) + list(Path('32x-textures').rglob('*.png')) + [Path('16x-pack.png'), Path('32x-pack.png')]

for image in images:
    subprocess.run(['optipng', '-o7', str(image), '-fix'])
