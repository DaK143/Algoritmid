# andmed
list = ["puu","tee",10]
#programmi saab kasutada niikaua, kuni listis on andemid
while list != None:
    print("Kas soovite lisada andmeid? jah või ei")
    lisa = input()
    if lisa == "jah":
        #lisame listi andmed viimasele kohale
        andmed = input("Sisesta siia andmed! ")
        print(len(list))
        uus = (len(list)-0)
        list.insert(uus,andmed)
        print(list)
    if lisa == "ei":
        print("Kas soovite andmeid eemaldada? jah või ei ")
        andmed2 = input()
        if andmed2 == "jah":
            #eemaldame viimase elemendi listist
            list = list[:-1]
            print(list)
        if andmed2 == "ei":
            print("Head päeva jätku!")
