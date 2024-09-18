luku = int(input("Anna luku:"))

if luku == 1984:
    print("Orwell")

###

luku = int(input("Anna luku:"))
if luku < 0:
    tulos = (f"{luku*-1}")
    print(f"{tulos}")

if luku >= 0:
    print(f"{luku}")

###

hinta = 5,90
nimi = input("Mikä on nimesi:")

if nimi != Jerry:
    määrä = int(input("Kuinka monta annosta keittoa:"))
    yhthinta = määrä*hinta
    print(f"Kokonaishinta on {yhthinta}")
    print("Seuraava asiakas")

if nimi == Jerry:
print("Seuraava asiakas")

### Palkka

palkka = float(input("Tuntipalkka:"))
tunnit = float(input("Työtunnit:"))
vkopv = input("Viikonpäivä:")
if vkopv != "sunnuntai":
    print(f"Palkka {palkka*tunnit} euroa")
if vkopv == "sunnuntai":
    print(f"Palkka {palkka*tunnit*2} euroa")

### Korkoa kortille

pisteet = int(input("Kuinka paljon pisteitä?"))
if pisteet < 100:
    tulo10 = pisteet * 1.1
    print("Sait 10 % bonusta")
    print(f"Pisteitä on nyt {tulo10}")

if pisteet >= 100:
    tulo15 = pisteet * 1.15
    print("Sait 15% bonusta")
    print(f"Pisteitä on nyt {tulo15}")


### Huomisen vaatteet ???????????????????????

print("Kerro huominen sääennuste:")
lampo = int(input("Lämpötila:"))
sade = input("Sataako (kyllä/ei):")
sataa = sade == "kyllä"
if lampo >= 21:
    print("Pue housut ja t-paita")

if lampo <= 20:
    print("Ota myös pitkähihainen paita")

if lampo <= 10:
    print("Pue päälle takki")

if lampo < 5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if sataa:
    print("Muista myös sateenvarjo!")

### Toisen asteen yhtälö
























