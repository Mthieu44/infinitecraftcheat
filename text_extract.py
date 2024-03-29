import pytesseract as pt
from PIL import ImageGrab


def extract_text(x: int, y: int, w: int, h: int, tname: str) -> str:
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save(f"temp/{tname}.jpg")
    d = pt.image_to_data(img, output_type=pt.Output.DICT, config="--psm 7")
    
    n_boxes = len(d['text'])
    t = ""
    for i in range(n_boxes):
        if int(d['conf'][i]) > 90 and len(d['text'][i]) > 2:
            t += d['text'][i] + " "
    print(t)
    if t == "":
        t = " ".join([i for i in d['text'] if i != ""])
    nt = ""
    print(tname)
    print(t)
    print(d)
    for c in range(len(t)):
        if t[c] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if t[c+1] in "abcdefghijklmnopqrstuvwxyz":
                nt = t[c:]
                break
    print(nt)
    nt = nt.strip()
    if nt != "":
        while nt[-1] not in "abcdefghijklmnopqrstuvwxyz":
            nt = nt[:-1]
    else:
        nt = t.strip()
    print(nt)
    if nt == nt.lower():
        nt = nt.capitalize()
    print(nt)
    print("=========")
    
    return "".join([i for i in nt if i in "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
