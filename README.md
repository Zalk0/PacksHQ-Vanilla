# PacksHQ-Vanilla

This is the repository of the vanilla version of the resource pack for Hypixel Skyblock.

It is organized to be able to store the 16x and the 32x variant.
The [16x-textures](16x-textures) and [32x-textures](32x-textures) are in their respective folder
which correspond to the `textures` folder in `assets/packshq/textures`.
The [assets](assets) folder is the `assets` folder used for the 2 variants.

You need to install [pre-commit](https://pre-commit.com/) so that some checks are run before you can commit.
It also applies some fixes automatically. I can recommend to install it as a tool with
[uv](https://docs.astral.sh/uv/getting-started/installation/).
uv also allows you to install Python as it is required for pre-commit.  
Once you have uv installed you can do these commands:

```bash
uv python install
uv tool install pre-commit
```

There are scripts in the folder of the same name.
The [format-json](scripts/format-json.py) one is meant to be called with pre-commit.

The others are:

- [optipng](scripts/optipng.py) which calls the OptiPNG program on all png files.
- [compile](scripts/compile.py) to compile the pack in the 2 zips.

You need to install OptiPNG before running the associated script,
you can do so [here](https://optipng.sourceforge.net/).
You can also find it in most package managers.  
To use a script, just call it like this:

```bash
# With Python installed through uv
uv run scripts/optipng.py
# Using system Python
python scripts/optipng.py
```
