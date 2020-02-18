from src.card_model import create_card, SpellCard, TrapCard, MonsterCard
import pytest


@pytest.mark.parametrize(
    "test_input,card_type,attr",
    [
        ("Spell Card", SpellCard, "SPELL"),
        ("Trap Card", TrapCard, "TRAP"),
        ("Normal Monster", MonsterCard, "LIGHT"),
    ],
)
def test_GIVEN_card_type_WHEN_creating_card_THEN_correct_type_of_card_is_created(
    test_input, card_type, attr
):
    card_details = {
        "type": test_input,
        "name": "test",
        "desc": "desc",
        "race": "race",
        "attribute": "LIGHT",
        "id": 12345678,
        "card_images": [{"image_url": "test"}],
        "atk": "3000",
        "def": "2500",
        "level": "8",
    }
    card = create_card(card_details)

    assert isinstance(card, card_type)
    assert card.attr == attr
