

from io import BytesIO
from urllib import request

from PIL import Image


def download_image(url):
    """
    This function downloads images from a URI
    """
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    """
    This function converts images to RBG
    """
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def prepare_input(x):
    return x / 255.0
