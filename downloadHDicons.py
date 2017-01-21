#!/usr/bin/python

##############################################
##  Author: MinionAttack                    ##
##  GitHub: https://github.com/MinionAttack ##
##############################################

import sys
import errno
import urllib
from os import makedirs
from os.path import expanduser


DOWNLOAD_FOLDER = '/PokemonHDicons'
BASE_URL = 'https://silphroad-s3-xika4hn.netdna-ssl.com/img/pokemon/icons/'
START_INDEX = 1
FINISH_INDEX = 650
SIZE_A = '96'
SIZE_B = '96'
SIZE_SEPARATOR = 'x'
SEPARATOR = '/'
FILE_EXTENSION = '.png'

def createFolder(path):
    try:
        makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def dowloadIcons(path):
    for pokemonNumber in range(START_INDEX,FINISH_INDEX):
        url = BASE_URL + SIZE_A + SIZE_SEPARATOR + SIZE_B + SEPARATOR + str(pokemonNumber) + FILE_EXTENSION
        name = str(pokemonNumber) + FILE_EXTENSION
        output = path + SEPARATOR + name
        print 'Downloading Pokemon icon: ' + str(pokemonNumber)
        urllib.urlretrieve(url, output)
    

def main(argv):
    userHome = expanduser("~")
    path = userHome + DOWNLOAD_FOLDER
    createFolder(path)
    try:
        dowloadIcons(path)
    except KeyboardInterrupt:
        print 'Download process interrupted.'
    

if __name__ == "__main__":
    main(sys.argv[1:])
