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
from card_model import CardModel, create_card
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

        self.desc_group_box = QGroupBox()
        self.main_layout.addWidget(self.desc_group_box)

        self.id_label = QLabel(self.model.id)
        self.id_label.alignment(Qt.AlignLeft)
        self.main_layout.addWidget(self.id_label)
