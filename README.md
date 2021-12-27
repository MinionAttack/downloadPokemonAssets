# Download Pokémon Assets

![build](https://img.shields.io/badge/build-passing-brightgreen) ![license](https://img.shields.io/badge/license-MIT-brightgreen) ![python](https://img.shields.io/badge/python-3.8%2B-blue) ![platform](https://img.shields.io/badge/platform-linux--64%20%7C%20win--64-lightgrey)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MinionAttack_downloadHDicons&metric=alert_status)](https://sonarcloud.io/dashboard?id=MinionAttack_downloadHDicons)

Table of contents.

1. [Introduction](#introduction)
2. [Requisites](#requisites)
3. [Project structure](#project-structure)
4. [Installation](#installation)
5. [How to use](#how-to-use)
6. [Examples](#examples)
7. [Licensing agreement](#licensing-agreement)

## Introduction

This tool allows you to download different types of Pokémon resources.

On the one hand, you can download Pokémon icons in *PNG* format with transparent background. These icons are taken from the biggest Pokémon
fansub, **The Silph Road**.

On the other hand, you can also download the Pokémon images (in detail and full size) in *PNG* format with transparent background which are
ideal for posting as a user photo on social networks. These images are taken from the Pokédex of the official Pokémon website.

**Important note**:

The images do not contain all possible forms of all Pokémon as the official *Pokédex* is missing forms, so it may be the case that some
forms are available as icons but not as images.

The same applies to *The Silph Road* icons, some forms are not available or could not be found but those forms are available as images.

## Requisites

In order to use this tool it is necessary to have a compatible environment:

- **Operative system**: A *Linux* or *Windows* based system where the tool will run.
- **Python version**: The tool has been developed with version *3.8.9*. It may work with older versions, but this has not been tested.

## Project structure

In this section you can have a quick view of the project structure.

```
.
├── download_pokemon_assets.py
├── LICENSE
├── modules
│  ├── fansub_downloader.py
│  ├── official_downloader.py
│  └── utils.py
├── README.md
├── requirements.txt
└── resources
    ├── pokemon_data.py
    └── the_silph_road_data.py
```

## Installation

This section expects the requirements stated in the previous section to be met and this is how this section has been written.

- **Program dependencies**: The tool has some dependencies that must be installed in order to work. Those dependencies can be installed with
  the _requirements.txt_ file:
  - `$ pip install -r requirements.txt`
- It is highly recommended to use a **virtual environment** (*venv*), so the tool dependencies installation will not conflict with the
  packages installed on the system.

If you want to run the tool in a *venv*, open a terminal in the project's root folder and run:

```
$ source path_to_your_virtual_environment/bin/activate
$ pip install -r requirements.txt
```

If you do not want to run the tool in a *venv*, open a terminal in the project's root folder and run:

`$ pip install -r requirements.txt`

**Note**: If you have both **Python 2** and **Python 3** installed on your system, use **pip3** instead of **pip**.

## How to use

To run the tool, from a terminal in the root directory, type:

`$ ./download_pokemon_assets.py`

This will show the usage:

```
usage: download_pokemon_assets.py [-h] {icons,images} ...

A tiny program to dowload HD Pokémon Icons from The Silph Road

optional arguments:
  -h, --help      show this help message and exit

Commands:
  {icons,images}
    icons         Download Pokémon icons from the specified region(s).
    images        Download Pokémon images from the specified region(s).
```

If you want to know how to use a specific command, for example the icons command, type:

`$ ./download_pokemon_assets.py icons --help`

And it will show the help:

```
usage: download_pokemon_assets.py icons [-h] --region {Kanto,Johto,Hoenn,Sinnoh,Unova,Kalos,Alola,Galar} [{Kanto,Johto,Hoenn,Sinnoh,Unova,Kalos,Alola,Galar} ...]

optional arguments:
  -h, --help            show this help message and exit
  --region {Kanto,Johto,Hoenn,Sinnoh,Unova,Kalos,Alola,Galar} [{Kanto,Johto,Hoenn,Sinnoh,Unova,Kalos,Alola,Galar} ...]
                        Region of the Pokémon. To indicate several at the same time, they must be separated by spaces.
```

**Note**: If you get a permission denied error, open a terminal and grant execute permissions to the tool with the following command:

`$ chmod +x download_pokemon_assets.py`

## Examples

**Note 1**: All downloaded assets will be saved in the personal folder of the user running the tool. The structure looks like this:

```
Pokémon Assets
├── Icons
│  ├── Alola
│  ├── Galar
│  ├── Hoenn
│  ├── Johto
│  ├── Kalos
│  ├── Kanto
│  ├── Sinnoh
│  └── Unova
└── Images
    ├── detail
    │  ├── Alola
    │  ├── Galar
    │  ├── Hoenn
    │  ├── Johto
    │  ├── Kalos
    │  ├── Kanto
    │  ├── Sinnoh
    │  └── Unova
    └── full
        ├── Alola
        ├── Galar
        ├── Hoenn
        ├── Johto
        ├── Kalos
        ├── Kanto
        ├── Sinnoh
        └── Unova
```

To download the icons of a region, type:

`./download_pokemon_assets.py icons --region Kanto`

To indicate several regions at the same time, they must be separated by spaces:

`./download_pokemon_assets.py icons --region Kanto Johto`

**Note 2**: At the time of writing, some assets are missing or could not be found:

- **KALOS**:
  - Nº 666 - Vivillon (High Plains Pattern)
  - Nº 666 - Vivillon (Icy Snow Pattern)
  - Nº 710 - Pumpkaboo (Large Size)
  - Nº 710 - Pumpkaboo (Small Size)
  - Nº 710 - Pumpkaboo (Super Size)
- **ALOLA**:
  - Nº 800 - Dawn Wings Necrozma
  - Nº 800 - Dusk Mane Necrozma
- **GALAR**:
  - Nº 555 - Galarian Darmanitan (Zen Mode)
  - Nº 849 - Toxtricity (Low Key Form)
  - Nº 892 - Urshifu (Rapid Strike Style)
  - Nº 892 - Urshifu (Single Strike Style)
  - Nº 892 - Gigantamax Urshifu (Rapid Strike Style)
  - Nº 892 - Gigantamax Urshifu (Single Strike Style)
  - Nº 898 - Ice Rider Calyrex
  - Nº 898 - Shadow Rider Calyrex

To download the images of a region (for a certain size), type:

`./download_pokemon_assets.py images --size full --region Kanto`

To indicate several regions at the same time, they must be separated by spaces:

`./download_pokemon_assets.py images --size full --region Kanto Johto`

**Note 3**: At the time of writing, some *detail* assets are missing or could not be found:

- **SINNOH**:
  - Nº 423 - Gastrodon (East Sea)

## Licensing agreement

Copyright © 2021 MinionAttack

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
