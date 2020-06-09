bez=0

print("Hau produktuen BEZa kalkulatzen lagunduko dizun programa bat da.\nLehenik hautatu zure produktua zein lehentasun-mailakoa den:\n")
print("1) Orokorra\n2) Murriztua\n3) Oso murriztua\n")

mota=input("Hautatu horietako bat: ").lower()

while mota!="1" and mota!="2" and mota!="3" and mota!="orokorra" and mota!="murriztua" and mota!="oso murriztua":
    print("Ez dezu aukera baliogarririk idatzi. Ziurtatu ondo idatzi dezula.")
    mota=input("Saiatu berriro: ")

if mota=="1" or mota=="orokorra":
    bez=0.21
    ehun=21
elif mota=="2" or mota=="murriztua":
    bez=0.18
    ehun=18
elif mota=="3" or mota=="oso murriztua":
    bez=0.04
    ehun=4


prezioa=float(input(f"\nSartu BEZa (%{ehun}) aplikatu nahi diozun produktuaren prezioa: "))
gehigarria=prezioa*bez

print(f"    BEZa gehituta duen prezioa: {prezioa+gehigarria}")