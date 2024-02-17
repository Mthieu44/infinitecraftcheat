from typing import Optional, List
import json


class Craft:
    def __init__(self, p1, p2, r):
        self.parent1 = p1
        self.parent2 = p2
        self.result = r

    def __str__(self):
        return self.parent1 + " + " + self.parent2 + " = " + self.result

    def __eq__(self, other):
        return self.parent1 == other.parent1 and self.parent2 == other.parent2 or \
               self.parent1 == other.parent2 and self.parent2 == other.parent1


class ListeCrafts:
    def __init__(self):
        self.liste = []

    def ajouter(self, craft: Craft):
        self.liste.append(craft)

    def get_result(self, p1: str, p2: str) -> Optional[str]:
        for craft in self.liste:
            if craft.parent1 == p1 and craft.parent2 == p2:
                return craft.result
            elif craft.parent1 == p2 and craft.parent2 == p1:
                return craft.result
        return None

    def export_to_json(self, filename: str) -> None:
        with open(filename, "w") as f:
            json.dump([
                {
                    "parent1": craft.parent1,
                    "parent2": craft.parent2,
                    "result": craft.result
                }
                for craft in self.liste
            ], f)

    def import_from_json(self, filename: str) -> None:
        self.liste = []
        with open(filename, "r") as f:
            data = json.load(f)
            for craft in data:
                self.ajouter(Craft(craft["parent1"], craft["parent2"], craft["result"]))
