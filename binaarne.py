def otsing(massiiv, vaikseim, suurim, target):# Definitsioon
    if suurim >= vaikseim:# võrdlus
        keskmine =(vaikseim + suurim) // 2# Arvutatakse keskmine, saame keskkoha
        if massiiv[keskmine] == target:# Kui sisestatud arv on massiivi keskel, tagastatakse selle sama arvu indeks(nr)
            return keskmine
        elif massiiv[keskmine] < target:#Kui keskmine on väiksem kui target, siis otsime massiivi paremalt poolt
            return otsing(massiiv, keskmine + 1, suurim, target) 
        else:
            return otsing(massiiv, vaikseim, keskmine -1, target)# Kui keskmine on suurem kui target, otsime massiivi vasakult poolt
    else:
        return -1# Kui väärtust pole massiivis, tagastatakse -1

massiiv = [1, 3, 5, 7, 9, 11, 13, 15,]#Mmassiiv, väiksemast suuremani
target = 15# Väärtus, mida massiivist otsime

nr = otsing(massiiv, 0, len(massiiv)-1, target)
if nr == -1:# Kui indeks(nr) on -1  siis teatatakse, et arvu massiivis pole
    print("Otsitud väärtust massiivis pole.")
else:
    print("Otsitud väärtuse indeks on", str(nr))# Kui otsingu tulemus ei ole -1, siis järelikult on arv massiivis ning sellisel juhul prinditakse tema indeks 