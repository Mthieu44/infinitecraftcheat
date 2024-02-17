import pytesseract as pt
from PIL import ImageGrab


def extract_text(x: int, y: int, w: int, h: int) -> str:
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    t = pt.image_to_string(img, config="--psm 7", lang="eng")
    nt = ""
    for c in range(len(t)):
        if c != 0:
            if t[c] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and t[c - 1] == " ":
                nt = t[c:-1]
                break
        else:
            if t[c] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and t[c+1] in "abcdefghijklmnopqrstuvwxyz":
                nt = t[c:-1]
                break
    return nt
