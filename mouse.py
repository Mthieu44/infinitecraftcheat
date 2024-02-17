import pyautogui as pa
from text_extract import extract_text
import time


def move_to_objet():
    pa.moveTo(1620, 130)


def drag_object():
    pa.mouseDown()
    pa.moveTo(1400, 300, duration=0.2)
    pa.mouseUp()


def wipe_and_write(s: str):
    pa.hotkey('ctrl', 'a')
    pa.press('del')
    pa.write(s)


def create_new_object(s1: str, s2: str) -> str:
    wipe_and_write(s1)
    move_to_objet()
    drag_object()
    wipe_and_write(s2)
    move_to_objet()
    drag_object()
    time.sleep(0.4)
    t = extract_text(1320, 270, 200, 70)
    pa.rightClick()
    return t
