# Määrame maksimaalse võimaliku väärtuse vahemiku
MAX = 1000

# Luuakse kaks massiivi: üks positiivsete ja teine negatiivsete arvude jaoks
positive_map = [False] * (MAX + 1)
negative_map = [False] * (MAX + 1)

# Funktsioon väärtuse lisamiseks
def insert(arr, x):
    if x >= 0:
        positive_map[x] = True
    else:
        negative_map[-x] = True

# Funktsioon väärtuse otsimiseks
def search(arr, x):
    if x >= 0:
        return positive_map[x]
    else:
        return negative_map[-x]

# Näide
values = [3, -7, 15, 0, -3, 8]

# Andmete lisamine
for v in values:
    insert(positive_map if v >= 0 else negative_map, v)

# Otsing
test_values = [3, -7, 2, -5, 0]
print("Otsingu tulemused:")
for v in test_values:
    print(f"{v}: {'Leitud' if search(positive_map if v >= 0 else negative_map, v) else 'Ei leitud'}")