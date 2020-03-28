#!/usr/bin/python3
# -*- coding: utf-8 -*-

#############################################
## Author: MinionAttack                    ##
## GitHub: https://github.com/MinionAttack ##
#############################################

import os
import sys
import urllib.request
from pathlib import Path

DOWNLOAD_FOLDER = 'PokemonHDicons'
BASE_URL = 'https://assets.thesilphroad.com/img/pokemon/icons'
START_INDEX = 1
FINISH_INDEX = 650
SIZE_A = '96'
SIZE_B = '96'
SIZE_SEPARATOR = 'x'
SEPARATOR = '/'
FILE_EXTENSION = '.png'


def create_folder(path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except (OSError, FileNotFoundError) as exception:
        print('Error creating download folder: {}.'.format(exception.errno))
        sys.exit(1)


def dowload_icons(path):
    for pokemon_number in range(START_INDEX, FINISH_INDEX):
        url = BASE_URL + SEPARATOR + SIZE_A + SIZE_SEPARATOR + SIZE_B + SEPARATOR + str(pokemon_number) + FILE_EXTENSION
        name = str(pokemon_number) + FILE_EXTENSION
        output = os.path.join(path, name)
        print('Downloading Pokemon icon: {}.'.format(pokemon_number))
        urllib.request.urlretrieve(url, output)


def main():
    user_home = os.path.expanduser("~")
    path = os.path.join(user_home, DOWNLOAD_FOLDER)
    create_folder(path)
    try:
        dowload_icons(path)
    except KeyboardInterrupt:
        print('Download process interrupted.')


if __name__ == "__main__":
    main()
