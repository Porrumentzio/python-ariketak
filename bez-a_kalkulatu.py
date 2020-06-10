# Zehaztapenak
bez=0
motak_zer = ["1", "orokorra", "2", "murrriztua", "3", "oso murriztua"]
    #Eragiketak
gehitu_eragi_zer = ["1", "prezioari beza gehitu", "gehitu"]
atera_eragi_zer = ["2", "preziotik beza atera", "atera"]

# Hasiera eta motak
print("\nHau produktuen BEZa kalkulatzen lagunduko dizun programa bat da.\nLehenik hautatu zure produktua zein lehentasun-mailakoa den:\n")
print("1) Orokorra\n2) Murriztua\n3) Oso murriztua\n")

mota=input("Hautatu horietako bat: ").lower().strip()

while mota not in motak_zer:
    print("Ez dezu aukera baliogarririk idatzi. Ziurtatu ondo idatzi dezula.")
    mota=input("Saiatu berriro: ").lower().strip()

if mota=="1" or mota=="orokorra":
    bez=0.21
    ehun=21
elif mota=="2" or mota=="murriztua":
    bez=0.18
    ehun=18
elif mota=="3" or mota=="oso murriztua":
    bez=0.04
    ehun=4


# Eragiketa aukeratu
print("\nZein eragiketa mota egin nahi duzu?\n")
print("1) Prezioari BEZa gehitu\n2) Preziotik BEZa atera\n")
eragiketa=input("Hautatu horietako bat: ").lower().strip()

while eragiketa not in gehitu_eragi_zer and eragiketa not in atera_eragi_zer:
    print("Ez dezu aukera baliogarririk idatzi. Ziurtatu ondo idatzi dezula.")
    eragiketa=input("Saiatu berriro: ").lower().strip()


if eragiketa in gehitu_eragi_zer:
    prezioa=float(input(f"\nSartu BEZa (%{ehun}) aplikatu nahi diozun produktuaren prezioa: "))
    zerga=prezioa*bez

    print(f"    BEZa gehituta duen prezioa: {prezioa+zerga}€")

elif eragiketa in atera_eragi_zer:
    prezioa=float(input(f"\nSartu BEZa (%{ehun}) atera nahi diozun produktuaren prezioa: "))
    zerga=prezioa*bez

    print(f"    Prezio originaletik BEZa hau da: {zerga}€")