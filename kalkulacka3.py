def isnumber(slovo):
    for pismeno in slovo:
        if not pismeno.isdigit():
            return False

    return True

# Nacti uzivatelsky text do promenne vstup
vstup = input("Napis rovnici")

# Rozsekej uzivatelsky vstup na jednotliva slova a uloz do promenne rovnice
rovnice = vstup.split()

# Pomocne pole pro udrzovani cisel
pole = []

for word in rovnice:
    if isnumber(word):
        cislo = int(word)
        pole.append(cislo)
    else:
        if word == "+":
            cislo1 = pole.pop()
            cislo2 = pole.pop()
            soucet = cislo1 + cislo2
            pole.append(soucet)
        elif word == "-":
            cislo1 = pole.pop()
            cislo2 = pole.pop()
            rozdil = cislo2 - cislo1
            pole.append(rozdil)
        elif word == "*":
            cislo1 = pole.pop()
            cislo2 = pole.pop()
            soucin = cislo1 * cislo2
            pole.append(soucin)
        elif word == "/":
            cislo1 = pole.pop()
            cislo2 = pole.pop()
            podil = cislo2 // cislo1
            pole.append(podil)
        else:
            print("Nerozumim " + word)

print("Vysledek" + str(pole[0]))





