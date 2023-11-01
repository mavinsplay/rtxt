from cv2 import imread
from pytesseract import image_to_string
from PIL.ImageGrab import grab


def screenshot(filepath='perem.png', coordinates=(0, 0, 1920, 1080)):
    # функция для создания скриншота нужной области
    image = grab(bbox=coordinates)
    image.save(filepath)


def processimage(filepath, lang='eng'):
    # функция для извлечения текста из картинки
    img = imread(filepath)
    txt = image_to_string(img, lang)
    return txt