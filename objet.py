from typing import Optional


class Objet:
    def __init__(self, mot: str, parent1: Optional['Objet'] = None, parent2: Optional['Objet'] = None):
        self.mot = mot
        self.parent1 = parent1
        self.parent2 = parent2

    def __str__(self) -> str:
        return self.mot

    def __eq__(self, other: 'Objet') -> bool:
        return self.mot == other.mot

    def profondeur(self) -> int:
        if self.parent1 is None and self.parent2 is None:
            return 0
        return 1 + max(self.parent1.profondeur(), self.parent2.profondeur())