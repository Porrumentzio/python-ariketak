# Hiztegi bat deklaratu ta aldagaiak jarri, erabiltzaileak sartu ditzan

hizt = {}

EI = input("Sartu zure erabiltzaile izena:\n")
hizt['Erabiltzaile_izena'] = EI

PH = input("Sartu zure pasahitza:\n")
hizt['Pasahitza'] = PH

# Aldagai hoiek gorde ta bukle batekin bere datuak sartzea, ondo sartu arte (input = hiztegian sartutako datua)

print("\n\nERREGISTRO LEIHOA\n")
input("Sartu zure erabiltzaile izena:\n")

if input == EI:
    print("Ondo, orain sartu pasahitza.")
else:
    print("Gaizki.")