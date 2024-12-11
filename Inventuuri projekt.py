inventuur = {
    101: "Külmkapid",
    102: "Pesumasinad",
    103: "Kuivatuskapid",
    104: "Tolmuimejad",
    105: "Õhupuhastid",
    106: "Mikrolaineahjud",
    107: "Segistid",
    108: "Blenderid",
    109: "Triikrauad",
    110: "Röstrid",
    111: "Veinikülmikud",
    112: "Kohvimasinad",
    113: "Ahjud",
    114: "Nõudepesumasinad",
    115: "Ventilaatorid",
    116: "Radiaatorid",
    117: "Kuumapuhur",
    118: "Konditsioneerid",
    119: "Külmikud",
    120: "Veekeetjad",
    121: "Pliidid",
    122: "Riisipliidid",
    123: "Smuutimikserid",
    124: "Grillid",
    125: "Toiduvalmistuspotid"
}

kogus = [
    105, 120, 106, 113, 102, 121, 123, 122, 103, 108,
    104, 110, 124, 114, 116, 115, 117, 109, 118, 119,
    111, 112, 117, 107, 101, 105, 108, 110, 112, 115,
    120, 125, 101, 103, 107, 109, 119, 122, 123, 104,
    117, 114, 121, 110, 116, 106, 108, 111, 109, 115,
    120, 105, 113, 125, 122, 103, 107, 123, 119, 117,
    104, 118, 114, 101, 102, 108, 112, 110, 107, 116,
    121, 105, 113, 122, 120, 124, 125, 119, 103, 111,
    103, 105, 107, 111, 108, 115, 124, 122, 117, 114,
    107, 122, 112, 101, 108, 125, 117, 114, 105, 120
]

# Funktsioon, mis otsib toodet ID alusel
def search_item(item_id):
    return inventuur.get(item_id, "Toodet antud ID-ga ei leitud")

# Lihtne sorteerimisalgoritm (bubble sort)
def sort_inventory(items):
    sorted_items = items[:]
    for i in range(len(sorted_items)):
        for j in range(len(sorted_items) - i - 1):
            if sorted_items[j] > sorted_items[j + 1]:
                sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]
    return sorted_items

# Funktsioon, mis loendab kindla ID-ga tooteid
def count_item(stock, item_id):
    return stock.count(item_id)

# Põhimenüü tsükkel
while True:
    print("\n\nValikud:")
    print("1. Leia toode ID alusel.")
    print("2. Vaata toodete loendit.")
    print("3. Sorteeri laoseis.")
    print("4. Lisa toode laoseisu.")
    print("5. Eemalda toode laoseisust.")
    print("6. Välju programmist.")

    user_choice = input("Sisesta valiku number: ")

    if user_choice == "1":
        try:
            item_id = int(input("Sisesta otsitava toote ID: "))
            print(f"Toode: {search_item(item_id)}")
            print(f"Laos saadaval: {count_item(kogus, item_id)} tk.")
        except ValueError:
            print("Sisestage korrektne ID number.")

    elif user_choice == "2":
        print("Laoseisu tooted:")
        for key, value in inventuur.items():
            print(f"ID {key}: {value}")

    elif user_choice == "3":
        kogus = sort_inventory(kogus)
        print(f"Sorteeritud laoseis: {kogus}")

    elif user_choice == "4":
        try:
            item_id = int(input("Sisesta toote ID, mida soovid lisada: "))
            if item_id in inventuur:
                quantity = int(input("Sisesta kogus: "))
                kogus.extend([item_id] * quantity)
                print(f"Lisati {quantity} tk toodet: {inventuur[item_id]}.")
            else:
                print("Sellist toodet ei leitud.")
        except ValueError:
            print("Sisestage kehtiv ID ja kogus.")

    elif user_choice == "5":
        try:
            item_id = int(input("Sisesta toote ID, mida soovid eemaldada: "))
            if item_id in inventuur:
                quantity = int(input("Sisesta kogus: "))
                for _ in range(quantity):
                    if item_id in kogus:
                        kogus.remove(item_id)
                    else:
                        print("Laos pole piisavalt toodet.")
                        break
                print(f"Eemaldati {quantity} tk toodet: {inventuur[item_id]}.")
            else:
                print("Sellist toodet ei leitud.")
        except ValueError:
            print("Sisestage kehtiv ID ja kogus.")

    elif user_choice == "6":
        print("Programm lõpetatakse. Nägemist!")
        break

    else:
        print("Vale valik! Proovi uuesti.")
