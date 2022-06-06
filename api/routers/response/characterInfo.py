import importlib
from typing import List
import core.set as set
from core.calc import calc_set, calc_single_set


def get_character_info(character: str):
    module_name = "core.characters." + character
    character = importlib.import_module(module_name)
    classChangeInfo = character.classChange().getinfo()
    return classChangeInfo
