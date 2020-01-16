import json
from io import BytesIO
import requests
from PIL import Image
from picamera import PiCamera
import pytesseract
from time import sleep


def get_id_from_card() -> str:
    """
    Detect and return the current ID of the card being used
    """
    my_stream = BytesIO()
    camera = PiCamera()
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, "jpeg")
    id = pytesseract.image_to_string(my_stream)
    return id


def get_card_image(id: str):
    response = requests.get(f"https://db.ygoprodeck.com/api/v5/cardinfo.php?name={id}")
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
