import argparse
import json
from io import BytesIO
from typing import Any

import requests
from PIL import Image
import pytesseract
from time import sleep
from PySide2.QtWidgets import QApplication
from src.card import Card

parser = argparse.ArgumentParser(
    description="Get card information from scanned yugioh cards"
)
parser.add_argument("-f", help="fake a raspberry pi instance", action="store_true")
args = parser.parse_args()

if args.f:
    import sys
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules["smbus"] = fake_rpi.smbus  # Fake smbus (I2C)
    from fake_rpi import picamera
else:
    import picamera


def get_id_from_card() -> str:
    """
    Detect and return the current ID of the card being used
    """
    my_stream = capture_image()
    card_id = pytesseract.image_to_string(my_stream, config="digits")
    return card_id


def capture_image():
    my_stream = BytesIO()
    camera = picamera.PiCamera()
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, "jpeg")
    my_stream.seek(0)
    # TODO: we are going to need to crop it here for performance and clarity
    return my_stream


def get_card_image(id: str):
    json_dict = pull_card_data(id)
    image_url = json_dict["card_images"][0]["image_url"]
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    image.show()


def pull_card_data(id):
    response = requests.get(f"https://db.ygoprodeck.com/api/v5/cardinfo.php?name={id}")
    json_dict = json.loads(response.content)[0]
    return json_dict


def capture_and_detect():
    card_id = get_id_from_card()
    if len(card_id) == 8:
        data = pull_card_data(get_id_from_card())
        qt_window = Card(None, data)
        qt_window.show()


def basic_usage(card_id: str, parent: Any = None):
    """Basic usage of the application, minus the card recognition bits"""
    data = pull_card_data(card_id)
    qt_window = Card(parent, data)
    qt_window.setWindowTitle("YGO Scanner")
    qt_window.show()
    return qt_window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = basic_usage(95286165)

    sys.exit(app.exec_())
