import json
from typing import List, Tuple

import core.set as set
from core.baseClass.equipment import equ
from core.equipment.avatar import 装扮, 装扮集合
from core.equipment.emblems import get_emblems_setinfo
from core.equipment.enchanting import get_enchanting_setinfo
from core.equipment.jade import get_jade_setinfo
from core.equipment.sundry import get_sundries_setinfo
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from utils.apiTools import Return, response

from .response import characterInfo, equipmentInfo
from .token import AlterState, authorize, createToken

infoRouter = APIRouter()


class adventureinfo(BaseModel):
    name: str
    alters: List[str]


@infoRouter.get('/adventure')
async def get_adventure_info():
    adventure_info = {}
    with open("./dataFiles/adventure-info.json", encoding='utf-8') as fp:
        adventure_info = json.load(fp)
    return response(data=adventure_info)


class notice(BaseModel):
    time: str
    info: str


class characterSkillInfo(BaseModel):
    # 技能信息
    skillInfo: dict
    # 个性化设置，技能选项等
    individuation: dict
    # 护石及符文信息
    # 药剂等相关信息设置


@infoRouter.get('/character')
async def get_character_info(state: AlterState = Depends(authorize)):
    return response(data=characterInfo.get_character_info(state.alter))


@infoRouter.get('/equips')
async def get_equipment(state: AlterState = Depends(authorize)):
    return response(data=equipmentInfo.get_equipment_info(state.alter))


@infoRouter.get("/dress")
async def get_dress(state: AlterState = Depends(authorize)):
    if(state is None or state.alter is None):
        raise Exception("无效token")
    character = characterInfo.get_character_info(state.alter)
    infolist = {}
    i = 0
    for dress in 装扮集合:
        部位 = dress.部位
        if 部位 not in infolist:
            infolist[部位] = []
        选项集合 = dress.选项集合
        if dress.部位 == '上衣':
            选项集合 = 选项集合 + tuple(character['clothes_coat'])
        elif dress.部位 == '下装':
            选项集合 = 选项集合 + tuple(character['clothes_pants'])
        data = {}
        data['id'] = i
        data['options'] = 选项集合
        data['part'] = 部位
        data['rarity'] = dress.品质
        data['suit'] = dress.套装
        data['name'] = "{品质}装扮{部位}".format(品质=dress.品质, 部位=dress.部位)
        i += 1
        infolist[部位].append(data)
    return response(data=infolist)


@infoRouter.get('/enchanting')
async def get_enchanting(state: AlterState = Depends(authorize)):
    return response(data=get_enchanting_setinfo(state.character))


@infoRouter.get('/equip/{equID}')
async def get_equipment_detail_info(equID):
    return response(data=equipmentInfo.get_equipment_detail_info(equID))


@infoRouter.get('/token/{alter}', response_model=Return[str])
async def getToken(alter: str, version: str = None):
    if version is not None and version != 'default' and version != '':
        alter = version + '.' + alter
    token = createToken(alter)
    return response(data=token)


@infoRouter.get("/emblem")
async def get_emblem(state: AlterState = Depends(authorize)):
    return response(data=get_emblems_setinfo(state.character))


@infoRouter.get("/jade")
async def get_jade():
    return response(data=get_jade_setinfo())


@infoRouter.get("/sundries")
async def get_sundries():
    return response(data=get_sundries_setinfo())


@infoRouter.get("/triggers")
async def get_triggers():
    return response(data=equ.get_chose_set())


@infoRouter.get("/entries")
async def get_entry_info():
    return response(data=equ.entry_info)


@infoRouter.get("/config/{name}")
async def get_config(name, state: AlterState = Depends(authorize)):
    return response(data=set.get(state.origin, name))


@infoRouter.get("/configs")
async def get_config(state: AlterState = Depends(authorize)):
    return response(data=set.get_set_list(state.origin))

