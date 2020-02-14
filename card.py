from typing import Dict, Any, List
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QPalette, QColor
from PySide2.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QVBoxLayout,
    QGroupBox,
    QFrame,
)
from card_model import CardModel, create_card, TrapCard, SpellCard, MonsterCard
from urllib import request


def get_attr_icon(attr: str):
    url_data = request.urlopen(
        f"https://www.db.yugioh-card.com/yugiohdb/external/image/parts/attribute/attribute_icon_{attr.lower()}.png"
    ).read()
    pixmap = QPixmap()
    pixmap.loadFromData(url_data)
    return pixmap


def get_card_background_colour():
    return QColor("ffffff")


class Card(QWidget):
    def __init__(self, parent: QWidget, card_details: List[Dict[str, Any]]):
        super.__init__(Card)
        self.setParent(parent)
        self.model = create_card(card_details)

    def setupUi(self):

        pal = QPalette()
        pal.setColor(QPalette.Background, get_card_background_colour())
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.main_layout = QHBoxLayout()

        self.name_attr_layout = QFormLayout()
        self.name_label = QLabel(self.model.name)

        self.attr_icon = QIcon(get_attr_icon(self.model.attr_icon))
        self.main_layout.addLayout(self.name_attr_layout)

        self.level_layout = QVBoxLayout()
        self.main_layout.addLayout(self.level_layout)

        self.picture_frame = QFrame()
        self.main_layout.addWidget(self.picture_frame)

        # Card sets here?

        self.desc_group_box = QGroupBox()
        self.set_up_group_box()
        self.main_layout.addWidget(self.desc_group_box)

        self.id_label = QLabel(self.model.id)
        self.id_label.alignment(Qt.AlignLeft)
        self.main_layout.addWidget(self.id_label)

    def set_up_group_box(self):
        self.desc_group_box.layout().addWidget(QLabel(self.model.desc))
        if isinstance(self.model, (MonsterCard)):
            self.desc_group_box.setTitle(self.get_group_box_title())
            line = QFrame()
            line.setFrameShape((QFrame.HLine))
            line.setFrameShadow(QFrame.Sunken)
            self.desc_group_box.layout().addWidget(line)
            label = QLabel(f"ATK/{self.model.defence}  DEF/{self.model.attack}")
            label.setAlignment(Qt.AlignRight)
            self.desc_group_box.layout().addWidget(label)

    def get_group_box_title(self):
        return f"[TEST/TEST]"
