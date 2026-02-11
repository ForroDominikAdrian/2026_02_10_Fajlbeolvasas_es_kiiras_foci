"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)

#Név; Csapat; Gólszám; Mérkőzések száma
A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""
labdarugok = []
with open("beolvasando_adatok/labdarugok.txt", "r", encoding="UTF8") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        sor = sor.rstrip("\n")
        labdarugok.append(list(sor.split(";")))
    for i in range(len(labdarugok)):
        labdarugok[i][2] = int(labdarugok[i][2])
        labdarugok[i][3] = int(labdarugok[i][3])

def legkevesebb_gol(labdarugok):
    golok_szama = 100000000000 
    jatekos = ""
    for i in range(len(labdarugok)):
        if golok_szama > labdarugok[i][2]:
            golok_szama = labdarugok[i][2]
            jatekos = labdarugok[i][0]
    return jatekos

def legtobb_gol(labdarugok):
    golok_szama = 0
    jatekos = ""
    for i in range(len(labdarugok)):
        if golok_szama < labdarugok[i][2]:
            golok_szama = labdarugok[i][2]
            jatekos = labdarugok[i][0]
    return jatekos

def legtobb_merkozes(labdarugok):
    merkozes_szam = 0
    jatekos = ""
    for i in range(len(labdarugok)):
        if merkozes_szam < labdarugok[i][3]:
            merkozes_szam = labdarugok[i][3]
            jatekos = labdarugok[i][0]
    return jatekos

def atlagos_golszam(labdarugok):
    golok_szama = 0
    for i in range(len(labdarugok)):
        golok_szama += labdarugok[i][2]
    return golok_szama / len(labdarugok)

def legtobb_csapat(labdarugok):
    thisdict = {}
    
    for i in range(len(labdarugok)):
        csapat = labdarugok[i][1]
        gol = labdarugok[i][3]
        
        if csapat in thisdict:
            thisdict[csapat] += gol
        else:
            thisdict[csapat] = gol
            
    return max(thisdict, key=thisdict.get)

print(f"A beolvasott fájlban összesen {len(labdarugok)} játékos szerepel.")
print(f"A legkevesebb gólt szerző játékos: {legkevesebb_gol(labdarugok)}")
print(f"A legtöbb gólt szerző játékos: {legtobb_gol(labdarugok)}")
print(f"A legtöbb mérkőzést játszó játékos: {legtobb_merkozes(labdarugok)}")
print(f"Az átlagos gólszám: {atlagos_golszam(labdarugok)}")
print(f"***A legtöbb gólt szerző csapat: {legtobb_csapat(labdarugok)}")