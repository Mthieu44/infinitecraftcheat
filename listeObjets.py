from typing import List, Optional
import json
from objet import Objet


class ListeObjets:
    def __init__(self, objets: List[Objet]):
        self.objets = objets

    def __str__(self) -> str:
        return str([str(objet) for objet in self.objets])

    def trouver(self, mot: str) -> Optional[Objet]:
        for objet in self.objets:
            if objet.mot == mot:
                return objet
        return None

    def ajouter(self, mot: str, p1: str, p2: str) -> None:
        parent1 = self.trouver(p1)
        parent2 = self.trouver(p2)
        if parent1 is None:
            raise ValueError(f"Le mot {p1} n'est pas dans la liste")
        if parent2 is None:
            raise ValueError(f"Le mot {p2} n'est pas dans la liste")
        objet_dans_liste = self.trouver(mot)
        if objet_dans_liste is None:
            objet = Objet(mot, parent1, parent2)
            self.objets.append(objet)
        else:
            if objet_dans_liste.profondeur() > Objet(mot, parent1, parent2).profondeur():
                objet_dans_liste.parent1 = parent1
                objet_dans_liste.parent2 = parent2

    def profondeur(self, mot: str) -> int:
        objet = self.trouver(mot)
        if objet is None:
            raise ValueError(f"Le mot {mot} n'est pas dans la liste")
        return objet.profondeur()

    def get_craft(self, mot: str) -> str:
        objet = self.trouver(mot)
        if objet is None:
            raise ValueError(f"Le mot {mot} n'est pas dans la liste")
        if objet.parent1 is None and objet.parent2 is None:
            return str(objet)
        return str(objet.parent1) + " + " + str(objet.parent2) + " = " + str(objet)

    def get_craft_tree(self, mot: str) -> str:
        objet = self.trouver(mot)
        if objet is None:
            raise ValueError(f"Le mot {mot} n'est pas dans la liste")
        l = self._get_craft_tree(objet, [])
        return "\n".join([self.get_craft(mot) for mot in l])

    def _get_craft_tree(self, objet: Objet, found: List[str]) -> List[str]:
        if objet.parent1 is None and objet.parent2 is None or objet.mot in found:
            return []
        else:
            found.append(objet.mot)
            return self._get_craft_tree(objet.parent1, found) + self._get_craft_tree(objet.parent2, found) + [objet.mot]

    def export_to_json(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump([
                {
                    "mot": objet.mot,
                    "parent1": objet.parent1.mot if objet.parent1 is not None else None,
                    "parent2": objet.parent2.mot if objet.parent2 is not None else None
                }
                for objet in self.objets
            ], f)

    def import_from_json(self, path: str) -> None:
        self.objets = []
        with open(path, "r") as f:
            for o in json.load(f):
                parent1 = self.trouver(o["parent1"]) if o["parent1"] is not None else None
                parent2 = self.trouver(o["parent2"]) if o["parent2"] is not None else None
                objet = Objet(o["mot"], parent1, parent2)
                self.objets.append(objet)
