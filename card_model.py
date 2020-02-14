from abc import ABC

from typing import Dict, Any, List


def create_card(card_details: List[Dict[str, Any]]):
    card = None
    type = card_details[0]["type"]
    if type == "Spell Card":
        card = SpellCard()
    elif type == "Trap Card":
        card = TrapCard()
    elif "Monster" in type:
        card = MonsterCard()
        card.attr = card_details[0]["attribute"]
        card.attack = card_details[0]["atk"]
        card.defence = card_details[0]["def"]
        card.level = card_details[0]["level"]
        card.type = card_details[0]["type"]  # may need to do something clever with this

    card.desc = card_details[0]["description"]
    card.race = card_details[0]["race"]
    card.id = str(card_details[0]["id"])

    card.img_url = card_details[0]["card_images"][0]["image_url"]


class CardModel(ABC):
    """Used for storing the card data retrieved from JSON"""

    attr = ""
    name = ""
    id = ""
    desc = ""
    level = ""
    race = ""
    img_url = ""


class SpellCard(CardModel):
    attr = "SPELL"


class TrapCard(CardModel):
    attr = "TRAP"


class MonsterCard(CardModel):
    type = ""
    attack = 0
    defence = 0
