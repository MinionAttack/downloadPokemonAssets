#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from typing import List

from modules.fansub_downloader import download_icons
from modules.official_downloader import download_images


def main():
    parser = ArgumentParser(description='A tiny program to download HD Pokémon Icons from The Silph Road')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    subparser = subparsers.add_parser('icons', help='Download Pokémon icons from the specified region(s).')
    subparser.add_argument('--region', type=str, choices=['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Galar', 'Hisui'],
                           nargs='+', required=True, help="Region of the Pokémon. To indicate several at the same time, they must be "
                                                          "separated by spaces.")
    subparser = subparsers.add_parser('images', help='Download Pokémon images from the specified region(s).')
    subparser.add_argument('--size', type=str, choices=['detail', 'full'], required=True, help="Size of the image.")
    subparser.add_argument('--region', type=str, choices=['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Galar', 'Hisui'],
                           nargs='+', required=True, help="Region of the Pokémon. To indicate several at the same time, they must be "
                                                          "separated by spaces.")

    arguments = parser.parse_args()
    if arguments.command:
        process_arguments(arguments)
    else:
        parser.print_help()


def process_arguments(arguments: Namespace) -> None:
    command = arguments.command
    if command == "icons":
        regions = arguments.region
        download_icons_handler(regions)
    elif command == "images":
        size = arguments.size
        regions = arguments.region
        download_image_handler(size, regions)
    else:
        print(f"Command {command} is not recognised.")


def download_icons_handler(regions: List[str]) -> None:
    download_icons(regions)


def download_image_handler(size: str, regions: List[str]) -> None:
    download_images(size, regions)


if __name__ == "__main__":
    main()
