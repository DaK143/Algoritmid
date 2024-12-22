
from collections import defaultdict

class Graaf:
    def __init__(self):
        # Graafi andmestruktuur, kus võtmed on tipud ja väärtused on naabrid
        self.kaared = defaultdict(list)

    def lisa_kaar(self, algus, lopp):
        # Lisa suunatud kaar graafi
        self.kaared[algus].append(lopp)

    def DFS_abi(self, tipp, kulastatud):
        # Märgime tipu külastatuks
        kulastatud.add(tipp)
        print(tipp, end=" ")

        # Käime läbi kõik naabrid, mida pole veel külastatud
        for naaber in self.kaared[tipp]:
            if naaber not in kulastatud:
                self.DFS_abi(naaber, kulastatud)

    def sygavuti_otsing(self, algus):
        # Hulka kasutamine külastatud tippude jälgimiseks
        kulastatud = set()
        self.DFS_abi(algus, kulastatud)

# Näidis kasutamine
g = Graaf()

g.lisa_kaar(0, 1)
g.lisa_kaar(0, 2)
g.lisa_kaar(1, 2)
g.lisa_kaar(2, 0)
g.lisa_kaar(2, 3)
g.lisa_kaar(3, 3)

g.sygavuti_otsing(2)