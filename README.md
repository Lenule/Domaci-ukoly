# Domaci úkoly

## Zadání
### Kalkulačka
1. Udělej soubor `mocnina.py`, který bude stejně jako `text.py` obsahovat program na mocnění. Rozdíl bude v tom, že mocnění bude zadefinováno funkcí a ne přímo řádkem co dělá `číslo ** číslo2`. (chtěl bych, aby namísto toho bylo použito `mocnina = power(cislo1, cislo2)` a program obsahoval definici funkce `power`)
2. Až budeš mít program `mocnina.py`, udělej program `mocnina-short.py`, který opět dělá to samé, ale celý program je jen na jednom řádku. To není možné, pokud chceš dělat víc výstupů a proto zkrať program jen na následující:
```python
vstup = input("Zadejte cislo, prosim:")
cislo = int(vstup)  #proc musi byt v zavore vstup, kdyz to funguje i bez nej?
vstup = input("Na kolikatou si prejete mocnit?")
cislo2 = int(vstup)
mocnina = cislo ** cislo2
vystup = str(mocnina)

print ("Vysledek:" + vystup)
```

### Semafor
1. Semafor s reálným časováním
