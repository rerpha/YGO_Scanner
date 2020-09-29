from typing import Dict, Any
import attr


def create_card(card_details: Dict[str, Any]):
    card = None
    card_type = card_details["type"]
    name = card_details["name"]
    desc = card_details["desc"]
    race = card_details["race"]
    id = str(card_details["id"])

    img_url = card_details["card_images"][0]["image_url"]

    if card_type == "Spell Card":
        card = SpellCard(
            desc=desc, name=name, level=0, race=race, img_url=img_url, id=id
        )
    elif card_type == "Trap Card":
        card = TrapCard(
            desc=desc, name=name, level=0, race=race, img_url=img_url, id=id
        )
    elif "Monster" in card_type:
        attribute = card_details["attribute"]
        attack = int(card_details["atk"])
        defence = int(card_details["def"])
        level = int(card_details["level"])
        type = card_details["type"]  # may need to do something clever with this
        card = MonsterCard(
            desc=desc,
            name=name,
            race=race,
            img_url=img_url,
            id=id,
            attack=attack,
            attribute=attribute,
            defence=defence,
            level=level,
            type=type,
        )

    return card


@attr.s
class CardModel:
    """Used for storing the card data retrieved from JSON"""

    attribute = attr.ib(type=str)
    name = attr.ib(type=str)
    id = attr.ib(type=str)
    desc = attr.ib(type=str)
    level = attr.ib(type=int)
    race = attr.ib(type=str)
    img_url = attr.ib(type=str)


@attr.s
class SpellCard(CardModel):
    attribute = attr.ib(type=str, default="SPELL")


@attr.s
class TrapCard(CardModel):
    attribute = attr.ib(type=str, default="TRAP")


@attr.s
class MonsterCard(CardModel):
    type = attr.ib(type=str)
    attack = attr.ib(type=int)
    defence = attr.ib(type=int)
