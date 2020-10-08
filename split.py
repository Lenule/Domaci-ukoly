parts = "Ahoj ja jsem kuba".split()
print(parts)

vstup = input ("Zadejte rovnici: ")

# 2 * 3
# +, -, *, /

rozdelit = vstup.split()
cislo1 = int(rozdelit[0])
cislo2 = int(rozdelit[2])
operace = rozdelit[1]

while vstup != "exit":
    if operace == "+":
        print (cislo1 + cislo2)

    elif operace == "-":
        print (cislo1 - cislo2)

    elif operace == "*":
        print (cislo1 * cislo2)

    elif operace == "/":
        print (cislo1 / cislo2)

    else:
        print ("Hovadina")

    vstup = input ("Zadejte rovnici: ")



print ("Koneeec")
# DOMACI UKOL: Udelej z toho cyklus do "exit"