print("     ADIN EGIAZTAKETA\n")

adina=int(input("Sartu zure adina: "))

while adina<0:
    print(f"{adina} zenbaki negatibo bat da eta ezin dezu adin negatiborik eduki.")
    adina=int(input("Sartu zure adina: "))
while adina>130:
    print(f"{adina} adin haundiegi bat da, ez det sinisten adin hoi dezunik.")
    adina=int(input("Sartu zure adina: "))

if adina>=18:
    print("18 urte baino gehiago dituzu, beraz pasa zaitezke.")
else:
    print("18 urte baino gutxiago dituzu, beraz ezin zea pasa.")