from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


path_assets = [Path('pack.mcmeta')] + list(Path('assets').rglob('*'))
path_textures = Path('assets', 'packshq', 'textures')
path_16x = Path('16x-textures')
path_32x = Path('32x-textures')

with ZipFile(Path('PacksHQ-16x.zip'), 'w', compression=ZIP_DEFLATED) as zip_16x:
	zip_16x.write(Path('16x-pack.png'), 'pack.png')
	for x in path_assets:
		zip_16x.write(x)
	for x in path_16x.rglob('*'):
		zip_16x.write(x, path_textures.joinpath(x.relative_to(path_16x)))

with ZipFile(Path('PacksHQ-32x.zip'), 'w', compression=ZIP_DEFLATED) as zip_32x:
	zip_32x.write(Path('32x-pack.png'), 'pack.png')
	for x in path_assets:
		zip_32x.write(x)
	for x in path_32x.rglob('*'):
		zip_32x.write(x, path_textures.joinpath(x.relative_to(path_32x)))
