from listeObjets import ListeObjets
from objet import Objet
from listeCrafts import ListeCrafts, Craft
import pyautogui as pa
import time
import mouse

ListeObjets([
    Objet("Water"),
    Objet("Fire"),
    Objet("Wind"),
    Objet("Earth"),
]).export_to_json("liste.json")

ListeCrafts().export_to_json("crafts.json")


def get_crafts_todo(liste: ListeObjets, act: ListeCrafts):
    l = []
    for o1 in liste.objets:
        for o2 in liste.objets:
            if (o1.mot, o2.mot) not in l and (o2.mot, o1.mot) not in l and Craft(o1.mot, o2.mot, "") not in act.liste:
                l.append((o1.mot, o2.mot))
    return l


def exe():
    currListe = ListeObjets([])
    currListe.import_from_json("liste.json")
    act = ListeCrafts()
    act.import_from_json("crafts.json")
    pa.moveTo(1620, 1050)
    pa.click()
    for m1, m2 in get_crafts_todo(currListe, act):
        t = mouse.create_new_object(m1, m2)
        currListe.ajouter(t, m1, m2)
        act.ajouter(Craft(m1, m2, t))

    mouse.wipe_and_write("")
    currListe.export_to_json("liste.json")
    act.export_to_json("crafts.json")

for i in range(2):
    time.sleep(5)
    exe()