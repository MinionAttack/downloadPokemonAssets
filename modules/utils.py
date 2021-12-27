# -*- coding: utf-8 -*-

import sys
import urllib.request
from pathlib import Path
from typing import List, Dict, Tuple
from urllib.error import HTTPError, ContentTooShortError, URLError

from tqdm import tqdm


def create_folder(path: Path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except OSError as exception:
        print(f"Error creating download folder: {exception.errno}")
        sys.exit(1)


def get_single_result(url: str, extension: str, headers: List[Tuple[str, str]], local_pokemons: List[Dict[str, str]], region: str,
                      region_folder: Path) -> None:
    for local_pokemon in tqdm(local_pokemons, desc=f"Downloading Pokémon assets from the {region} region"):
        get_asset(url, extension, headers, local_pokemon, region_folder)


def get_multiple_result(url: str, extension: str, headers: List[Tuple[str, str]], regional_pokemons: Dict[str, List[Dict[str, str]]],
                        region: str, region_folder: Path) -> None:
    for form, local_pokemons in regional_pokemons.items():
        if form == "Local":
            get_single_result(url, extension, headers, local_pokemons, region, region_folder)
        else:
            for local_pokemon in tqdm(local_pokemons, desc=f"Downloading Pokémon assets for {form} from the {region} region"):
                get_asset(url, extension, headers, local_pokemon, region_folder)


def get_asset(url: str, extension: str, headers: List[Tuple[str, str]], local_pokemon: Dict[str, str], region_folder: Path) -> None:
    pokemon_id = local_pokemon.get("id")
    name = local_pokemon.get("name")
    number = local_pokemon.get("number")

    pokemon_url = f"{url}{pokemon_id}.{extension}"
    asset_path = region_folder.joinpath(f"#{number} - {name}.{extension}")

    opener = urllib.request.build_opener()
    opener.addheaders = headers
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(pokemon_url, asset_path)
    except HTTPError:
        print(f"\nAsset ID {pokemon_id} not available for #{number} - {name}\r")
    except ContentTooShortError:
        print(f"\nAn error occurred while trying to download the asset with the identifier {pokemon_id} for #{number} - {name}\r")
    except URLError:
        print(f"\nAn error occurred while trying to store the asset with the identifier {pokemon_id} for #{number} - {name}\r")
