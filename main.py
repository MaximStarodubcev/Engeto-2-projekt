# vytvarim blok promennych pro pozdrav

pozdrav_1 = 'Hi there'
oddelovac = '-' * 48
pozdrav_2 = '''I\'ve generated a random 4 digit number for you. 
Let\'s play a bulls and cows game.'''

# tisknu pozdrav
print(f'{pozdrav_1}\n{oddelovac}\n{pozdrav_2}\n{oddelovac}\nEnter a number: ')


def ctyri_cisla():
    """funkce si vyzaduje 4 místné číslo (číslice musí být unikátní a nesmí začínat 0)"""
    while True:
        zadej_cislo = input(f'{oddelovac}\n>>> ')

        if zadej_cislo.startswith('0'):  # nesmi zacinat nulou
            print('nesmi zacinat nulou')

        elif not zadej_cislo.isdigit():  # nejsou ciselne hodnoty
            print('povolene jsou pouze ciselne znaky (cela cisla bez znamenek a mezer)')

        elif len(set(zadej_cislo)) != len(zadej_cislo):  # podminka pro neopakovatelsnst cifer v cisle
            print('cisla se opakuji')

        elif len(zadej_cislo) < 4:  # vstup kratsi ney 4 cisla
            print('prilis kratke')

        elif len(zadej_cislo) > 4:  # vstup delsi nez 4 cisla
            print('prilis dlouhe')

        elif len(zadej_cislo) == 4:  # delka musi byt presne 4 cisla
            return zadej_cislo


# pokazde prevede cislo na seznam
def moje_na_finalni_seznam():
    return [int(i) for i in str(ctyri_cisla())]


# vygeneruji si 1 nahodne cislo
while True:

    import random

    cisloprogram1 = random.randrange(1000, 9999)  # zacnu generovat nahodna cisla v uvedenem rozmezi
    if len(set(str(cisloprogram1))) == 4:  # mnozona ma pouye unikatni prvky, proto by mela mit pouze 4 prvky
        cisloprogram = [int(i) for i in str(cisloprogram1)]  # vysldne cislo prevedu na seznam, kvuli prochazeni
    break  # jakmile mam vygenerovane cislo, while smycku ukoncim


def bull_cow():
    finalni_seznam = [0, 0]  # seznam pro zapisovani vysledku
    nahodne_cislo = cisloprogram  # nova promena pro jiz vytvoreny seznam
    muj_vyber = moje_na_finalni_seznam()  # ulozim si do promene finalni_seznam z predchozi funkce
    for i in range(4):  # potrebuji prochazet dle indexu v seznamu z mych cisel a random cisel
        if muj_vyber[i] == nahodne_cislo[i]:  # podminka pro stejne cislo na stejnem miste v obou seznamech
            finalni_seznam[0] += 1  # prictu 1 k cislu na prvnim indexu v seznamu 'finalni_seznam'
        elif muj_vyber[i] in nahodne_cislo:  # podminka pro stejne cislo v obou seznamech ale na ruznem miste
            finalni_seznam[1] += 1  # opet prictu k 2 indexu v seznamu 'finalni_seznam'
    return finalni_seznam


pocet_pokusu = 1

# podminka pro tisk vysledku pokusu
while True:
    finalni_seznam = bull_cow()
    bull = 'bull'
    cow = 'cow'
    if finalni_seznam[0] == 4:
        print(f'Correct, you\'ve guessed the right number in {pocet_pokusu} attemps!')
        if pocet_pokusu < 4:
            print('That\'s amazing, average, not so good, ...')
        break
    elif finalni_seznam[0] > 1:
        bull += 's'

    elif finalni_seznam[1] > 1:
        cow += 's'

    print(f'you hit: {finalni_seznam[0]} {bull} and {finalni_seznam[1]} {cow}')
    pocet_pokusu += 1