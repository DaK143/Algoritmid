from collections import defaultdict

class Graaf:
    def __init__(self):
        # Graafi andmestruktuur, kus võtmed on tipud ja väärtused on naabrid
        self.kaared = defaultdict(list)
        self.kulastatud = set()  # Kasutame hulka külastatud tippude jälgimiseks

    def lisa_kaar(self, algus, lopp):
        # Lisa suunatud kaar graafi
        self.kaared[algus].append(lopp)

    def laiuti_otsing(self, algus):
        # Järjekord tippude läbimiseks
        jarjekord = [algus]
        self.kulastatud.add(algus)

        while jarjekord:
            # Võtame järgmise tipu järjekorra algusest
            praegune = jarjekord.pop(0)
            print(praegune, end=" ")

            # Lisame kõik naabrid, mida pole veel külastatud
            for naaber in self.kaared[praegune]:
                if naaber not in self.kulastatud:
                    jarjekord.append(naaber)
                    self.kulastatud.add(naaber)

# Näidis kasutamine
g = Graaf()

g.lisa_kaar(0, 1)
g.lisa_kaar(0, 2)
g.lisa_kaar(1, 2)
g.lisa_kaar(2, 0)
g.lisa_kaar(2, 3)
g.lisa_kaar(3, 3)

g.laiuti_otsing(2)