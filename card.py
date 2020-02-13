from typing import Dict, Any
from PySide2.QtWidgets import QWidget


class Card(QWidget):
    def __init__(self, parent: QWidget, card_details: Dict[str, Any]):
        super.__init__()

        self.show()
