from PySide2.QtGui import QPixmap
from src.card import Card
from pytestqt.qtbot import QtBot  # noqa: F401
from src.card_type import CardColours, CardType


def test_GIVEN_spell_card_details_WHEN_creating_card_THEN_ui_is_filled_in_correctly(
    qtbot, monkeypatch
):
    name = "test"
    desc = "desc"
    id = 12345678
    card_details = {
        "type": "Spell Card",
        "name": name,
        "desc": desc,
        "id": id,
        "race": "Equip spell",
        "card_images": [{"image_url": "test"}],
    }

    monkeypatch.setattr("src.card.Card._get_card_image", lambda x: QPixmap())

    card = Card(None, card_details)
    qtbot.addWidget(card)

    assert card.palette().color(card.backgroundRole()) == CardColours[CardType.SPELL]
    assert card.name_label.text() == name
    assert card.desc_label.text() == desc
    assert card.id_label.text() == str(id)


def test_GIVEN_trap_card_details_WHEN_creating_card_THEN_ui_is_filled_in_correctly(
    qtbot, monkeypatch
):
    name = "test"
    desc = "desc"
    id = 12345678
    card_details = {
        "type": "Trap Card",
        "name": name,
        "desc": desc,
        "id": id,
        "race": "Continuous Trap",
        "card_images": [{"image_url": "test"}],
    }

    monkeypatch.setattr("src.card.Card._get_card_image", lambda x: QPixmap())
    card = Card(None, card_details)
    qtbot.addWidget(card)

    assert card.palette().color(card.backgroundRole()) == CardColours[CardType.TRAP]
    assert card.name_label.text() == name
    assert card.desc_label.text() == desc
    assert card.id_label.text() == str(id)
