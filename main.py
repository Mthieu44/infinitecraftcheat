from listeObjets import ListeObjets
from listeCrafts import ListeCrafts

lo = ListeObjets([])
lo.import_from_json("liste.json")
print(lo)
print(len(lo.objets))

#print(lo.get_craft_tree("Fiord"))

lc = ListeCrafts()
lc.import_from_json("crafts.json")

print(lc.get_result("Water", "Fire"))
