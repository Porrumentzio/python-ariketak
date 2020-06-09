print("Sartu zenbakiak...")

a=int(input("Sartu lehenengo zenbakia: "))
b=int(input("Sartu bigarren zenbakia: "))

def baino_txikiagoa(a, b):

    if a > b:
        return("Bigarren zenbakia txikiagoa da.")
    elif a < b:
        return("Lehenengo zenbakia txikiagoa da.")
    elif a == b:
        return("Zenbaki berdina sartu dezu.")
    else:
        return("Ez dezu zenbaki bat sartu. Saiatu berriro.")

print(baino_txikiagoa(a, b))
