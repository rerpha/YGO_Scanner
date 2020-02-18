from src.card_model import create_card, SpellCard, TrapCard
import pytest


@pytest.mark.parametrize(
    "test_input,card_type,attr",
    [("Spell Card", SpellCard, "SPELL"), ("Trap Card", TrapCard, "TRAP")],
)
def test_GIVEN_card_type_WHEN_creating_card_THEN_correct_type_of_card_is_created(
    test_input, card_type, attr
):
    card_details = {
        "type": test_input,
        "name": "test",
        "desc": "desc",
        "race": "race",
        "id": 12345678,
        "card_images": [{"image_url": "test"}],
    }
    card = create_card(card_details)

    assert isinstance(card, card_type)
    assert card.attr == attr
