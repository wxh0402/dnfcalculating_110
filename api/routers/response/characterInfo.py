import importlib
from core.set import save
from core.calc.calc import calc_set


def get_character_info(character: str):
    module_name = "core.characters." + character
    character = importlib.import_module(module_name)
    classChangeInfo = character.classChange()
    return classChangeInfo


def save_set(alter: str, setName: str, setInfo):
    return save(alter, setName, setInfo)


def calc(alter: str, setName: str):
    return calc_set(alter, setName)