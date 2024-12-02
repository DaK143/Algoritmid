#Kood pole minu kirjutatud ja on võetud analüüsiks internetist !

class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def primary_hash(self, key):
        # Esmane räsifunktsioon
        return key % self.size

    def secondary_hash(self, key):
        # Teine räsifunktsioon (valitud nii, et ei jagaks tabeli suurust)
        return 1 + (key % (self.size - 1))

    def insert(self, key, value):
        index = self.primary_hash(key)
        step = self.secondary_hash(key)

        for i in range(self.size):
            if self.table[index] is None or self.table[index][0] == key:
                # Kas salvestame tühja kohta või uuendame olemasolevat
                self.table[index] = (key, value)
                return
            index = (index + step) % self.size  # Järgmine indeks

        raise Exception("Tabel on täis, sisestamine ebaõnnestus.")

    def search(self, key):
        index = self.primary_hash(key)
        step = self.secondary_hash(key)

        for i in range(self.size):
            if self.table[index] is None:
                return None  # Võtit ei leitud
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step) % self.size  # Järgmine indeks

        return None  # Võtit ei leitud

    def display(self):
        for i, item in enumerate(self.table):
            print(f"Slot {i}: {item}")

# Näide
ht = DoubleHashingHashTable(7)  # Väike suurus näidishajutamiseks
ht.insert(10, "A")
ht.insert(20, "B")
ht.insert(15, "C")
ht.insert(30, "D")
ht.display()

print("Otsing 20:", ht.search(20))  # Output: B
print("Otsing 25:", ht.search(25))  # Output: None