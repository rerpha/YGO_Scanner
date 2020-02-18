from io import BytesIO
from typing import Dict, Any
import requests
from PIL import Image
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont, QImage
from PySide2.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QGroupBox,
    QFrame,
    QGridLayout,
)
from card_model import create_card, TrapCard, SpellCard, MonsterCard
from urllib import request
from card_type import CardColours, CardType


def get_attr_icon(attr: str):
    url_data = request.urlopen(
        f"https://www.db.yugioh-card.com/yugiohdb/external/image/parts/attribute/attribute_icon_{attr.lower()}.png"
    ).read()
    pixmap = QPixmap()
    pixmap.loadFromData(url_data)
    return pixmap


class Card(QWidget):
    def __init__(self, parent: QWidget, card_details: Dict[str, Any]):
        super().__init__()
        self.setParent(parent)
        self.model = create_card(card_details)
        self.setupUi()

    def get_card_background_colour(self):
        if isinstance(self.model, SpellCard):
            return QColor(CardColours[CardType.SPELL])
        elif isinstance(self.model, TrapCard):
            return QColor(CardColours[CardType.TRAP])
        else:
            pass

    def setupUi(self):

        self.main_layout = QVBoxLayout()

        self.name_attr_layout = QHBoxLayout()
        self.name_label = QLabel(self.model.name)
        font = self.name_label.font()
        font.setBold(True)
        font.setCapitalization(QFont.AllUppercase)
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setMargin(5)
        pixmap = get_attr_icon(self.model.attr)
        self.attr_icon = QLabel()
        self.attr_icon.setPixmap(pixmap)
        self.attr_icon.setAlignment(Qt.AlignRight)
        self.name_attr_layout.addWidget(self.name_label)
        self.name_attr_layout.addWidget(self.attr_icon)
        self.main_layout.addLayout(self.name_attr_layout)

        self.level_layout = QHBoxLayout()
        self.main_layout.addLayout(self.level_layout)

        self.picture_frame = QFrame()
        self.picture_frame.setFixedSize(250, 250)
        self.picture_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.picture_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.picture_frame.setLineWidth(1)
        self.picture_frame.setContentsMargins(0, 0, 0, 0)
        self.picture_frame.setLayout(QGridLayout())
        self.image_holder = QLabel()

        pixmap = self._get_card_image()
        self.image_holder.setPixmap(
            pixmap.scaled(
                self.picture_frame.width(),
                self.picture_frame.height(),
                Qt.KeepAspectRatio,
            )
        )

        self.picture_frame.layout().addWidget(self.image_holder)

        self.main_layout.addWidget(self.picture_frame)

        # Card sets here?

        self.desc_group_box = QGroupBox()
        self.desc_group_box.setMaximumWidth(250)
        self.set_up_group_box()
        self.main_layout.addWidget(self.desc_group_box)

        self.id_label = QLabel(self.model.id)
        self.id_label.setAlignment(Qt.AlignLeft)
        self.id_label.setMargin(5)
        self.main_layout.addWidget(self.id_label)

        self.setLayout(self.main_layout)

        pal = QPalette()
        pal.setColor(QPalette.Background, self.get_card_background_colour())
        self.setAutoFillBackground(True)
        self.setPalette(pal)

    def _get_card_image(self):
        image_data = requests.get(self.model.img_url).content
        image = Image.open(BytesIO(image_data))
        image = image.crop((44, 106, 380, 438))  # this is about correct
        data = image.tobytes("raw", "RGB")
        qimage = QImage(data, image.size[0], image.size[1], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def set_up_group_box(self):
        self.desc_group_box.setLayout(QVBoxLayout())
        desc_label = QLabel(self.model.desc)
        desc_label.setWordWrap(True)
        self.desc_group_box.layout().addWidget(desc_label)
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
