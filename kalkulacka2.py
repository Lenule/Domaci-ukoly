# Udelej kalkulacku, ktera se zepta na operaci kterou ma provest a pokud:
#  1. je operace exit, tak skonci program
#  2. pokud ne:
#               a. pokud je operace secti, tak se zepta na 2 cisla a vrati vysledek
#               b. pokud je operace odecti, tak se zepta na 2 cisla a vrati vysledek

# Dokud uzivatel nezadá operaci exit, kalkulacka se bude ptat opakovane na dalsi operaci
# 
# # vstupy, vystupy a podminky a while

vstup = input ("Zadejte cislo: ")

cislo = int (vstup) 

vstup = input ("Zadejte druhe cislo: ")

cislo2 = int (vstup)

vstup = input ("Co mam s cisly udelat?")

# ==
# !=
# >
# <
# >=
# <=

while vstup != "exit":
    if vstup == "secist":
        z = cislo + cislo2
        print ("Výsledek: " + str(z))

    elif vstup == "odecist":
        z = cislo - cislo2
        print ("Vysledek: " + str(z))

    else:
        print("nerozumim...")

    vstup = input ("Zadejte cislo: ")

    cislo = int (vstup) 

    vstup = input ("Zadejte druhe cislo: ")
    
    cislo2 = int (vstup)
    
    vstup = input ("Co mam s cisly udelat?")
    

print ("Program je skoncen")