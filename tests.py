import pytest

from listeObjets import ListeObjets
from objet import Objet


@pytest.fixture
def liste():
    return ListeObjets([
        Objet("Water"),
        Objet("Fire"),
        Objet("Wind"),
        Objet("Earth"),
    ])


def test_trouver(liste):
    assert liste.trouver("Water") == Objet("Water")
    assert liste.trouver("Fire") == Objet("Fire")
    assert liste.trouver("Wind") == Objet("Wind")
    assert liste.trouver("Earth") == Objet("Earth")


def test_trouver2(liste):
    liste.ajouter("Steam", "Water", "Fire")
    liste.ajouter("Plant", "Water", "Earth")
    assert liste.trouver("Steam") == Objet("Steam", Objet("Water"), Objet("Fire"))
    assert liste.trouver("Plant") == Objet("Plant", Objet("Water"), Objet("Earth"))


def test_trouver3(liste):
    assert liste.trouver("Steam") is None
    assert liste.trouver("Plant") is None


def test_profondeur(liste):
    liste.ajouter("Steam", "Water", "Fire")
    liste.ajouter("Plant", "Water", "Earth")
    liste.ajouter("Tea", "Steam", "Plant")
    assert liste.profondeur("Water") == 0
    assert liste.profondeur("Fire") == 0
    assert liste.profondeur("Steam") == 1
    assert liste.profondeur("Plant") == 1
    assert liste.profondeur("Tea") == 2


def test_profondeur2(liste):
    with pytest.raises(ValueError):
        liste.profondeur("Steam")


def test_get_craft(liste):
    liste.ajouter("Steam", "Water", "Fire")
    liste.ajouter("Plant", "Water", "Earth")
    assert liste.get_craft("Steam") == "Water + Fire = Steam"
    assert liste.get_craft("Plant") == "Water + Earth = Plant"
    assert liste.get_craft("Water") == "Water"


def test_get_craft2(liste):
    with pytest.raises(ValueError):
        liste.get_craft("Steam")


def test_get_craft_tree(liste):
    liste.ajouter("Dust", "Wind", "Earth")
    liste.ajouter("Sand", "Dust", "Dust")
    liste.ajouter("Glass", "Sand", "Fire")
    liste.ajouter("Hourglass", "Sand", "Glass")
    assert liste.get_craft_tree("Hourglass") == "Wind + Earth = Dust\nDust + Dust = Sand\nSand + Fire = Glass\nSand + Glass = Hourglass"


def test_get_craft_tree2(liste):
    with pytest.raises(ValueError):
        liste.get_craft_tree("Hourglass")


def test_ajouter(liste):
    liste.ajouter("Water2", "Water", "Water")
    liste.ajouter("Water3", "Water2", "Water")
    liste.ajouter("Water5", "Water3", "Water2")
    liste.ajouter("Water8", "Water5", "Water3")
    assert liste.profondeur("Water8") == 4
    assert liste.get_craft("Water8") == "Water5 + Water3 = Water8"
    liste.ajouter("Water8", "Water", "Water3")
    assert liste.profondeur("Water8") == 3
    assert liste.get_craft("Water8") == "Water + Water3 = Water8"


def test_ajouter2(liste):
    with pytest.raises(ValueError):
        liste.ajouter("Sand", "Dust", "Water")
    with pytest.raises(ValueError):
        liste.ajouter("Glass", "Fire", "Sand")
