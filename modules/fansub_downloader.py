# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from modules.utils import create_folder, get_single_result, get_multiple_result
from resources.the_silph_road_data import get_region

HEADERS = [('Host', 'assets.thesilphroad.com'),
           ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'),
           ('Accept-Language', 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'),
           ('Accept-Encoding', 'gzip, deflate, br'),
           ('DNT', '1'),
           ('Connection', 'keep-alive'),
           ('Upgrade-Insecure-Requests', '1'),
           ('Sec-Fetch-Dest', 'document'),
           ('Sec-Fetch-Mode', 'navigate'),
           ('Sec-Fetch-Site', 'cross-site'),
           ('Cache-Control', 'max-age=0'),
           ]

URL = "https://assets.thesilphroad.com/img/pokemon/icons/96x96/"

EXTENSION = "png"


def download_icons(regions: List[str]) -> None:
    download_folder = Path().home().joinpath("Pokémon Assets").joinpath("Icons")

    for region in regions:
        region_folder = download_folder.joinpath(region)
        create_folder(region_folder)
        regional_pokemons = get_region(region)
        if regional_pokemons:
            if region in ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unova"]:
                local_pokemons = regional_pokemons.get("Local")
                get_single_result(URL, EXTENSION, HEADERS, local_pokemons, region, region_folder)
            elif region in ["Kalos", "Alola", "Galar"]:
                get_multiple_result(URL, EXTENSION, HEADERS, regional_pokemons, region, region_folder)
            else:
                print(f"The {region} region is not available.")
        else:
            print(f"No Pokémons found for region {region}.")

    print(f'\nAvailable assets downloaded at: {download_folder.resolve().__str__()}')
