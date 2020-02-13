import argparse

parser = argparse.ArgumentParser(
    description="Get card information from scanned yugioh cards"
)
parser.add_argument("-f", help="fake a raspberry pi instance")
args = parser.parse_args()

if args.f:
    import sys
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules["smbus"] = fake_rpi.smbus  # Fake smbus (I2C)
    from fake_rpi import picamera
else:
    import picamera


import json
from io import BytesIO
import requests
from PIL import Image
import pytesseract
from time import sleep


def get_id_from_card() -> str:
    """
    Detect and return the current ID of the card being used
    """
    my_stream = capture_image()
    id = pytesseract.image_to_string(my_stream, config="digits")
    return id


def capture_image():
    my_stream = BytesIO()
    camera = picamera.PiCamera()
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, "jpeg")
    my_stream.seek(0)
    return my_stream


def get_card_image(id: str):
    response = requests.get(f"https://db.ygoprodeck.com/api/v6/cardinfo.php?name={id}")
    json_dict = json.loads(response.content)[0]
    image_url = json_dict["card_images"][0]["image_url"]
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    image.show()


def button_callback():
    id = get_id_from_card()
    get_card_image(id)


if __name__ == "__main__":
    # Basic example for de-fusion
    get_card_image(95286165)
