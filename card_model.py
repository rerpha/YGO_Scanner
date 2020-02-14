from abc import ABC
from typing import Dict, Any


def create_card(card_details: Dict[str, Any]):
    card = None
    type = card_details["type"]
    if type == "Spell Card":
        card = SpellCard()
    elif type == "Trap Card":
        card = TrapCard()
    elif "Monster" in type:
        card = MonsterCard()
        card.attr = card_details["attribute"]
        card.attack = card_details["atk"]
        card.defence = card_details["def"]
        card.level = card_details["level"]
        card.type = card_details["type"]  # may need to do something clever with this

    card.name = card_details["name"]
    card.desc = card_details["desc"]
    card.race = card_details["race"]
    card.id = str(card_details["id"])

    card.img_url = card_details["card_images"][0]["image_url"]
    return card


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
