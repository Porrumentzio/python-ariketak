print("Sartu zenbakiak...")

a=int(input("Sartu lehenengoa: "))
b=int(input("sartu bigarrena: "))

def baino_haundiagoa(a, b):

    if a > b:
        return("Lehenengo zenbakia haundiagoa da.")
    elif a < b:
        return("Bigarren zenbakia haundiagoa da.")
    else:
        return("Zenbaki berdina sartu dezu.")

print(baino_haundiagoa(a, b))
