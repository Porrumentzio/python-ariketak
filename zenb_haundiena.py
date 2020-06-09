print("Funtzio honek sartutako lau zenbakien arteetan handiena zein den esango dizu.")

a=int(input("Sartu lehenengo zenbakia: "))
b=int(input("Sartu bigarren zenbakia: "))
c=int(input("Sartu hirugarren zenbakia: "))
d=int(input("Sartu laugarren zenbakia: "))

def zenb_haundiena(a, b, c, d):
    
    if a > b and a > c and a > d:
        return f"Lehenengo zenbakia da haundiena: {a}"
    elif b > a and b > c and b > d:
        return f"Bigarren zenbakia da haundiena: {b}"
    elif c > a and c > b and c > d:
        return f"Hirugarren zenbakia da haundiena: {c}"
    elif d > a and d > b and d > c:
        return f"Laugarren zenbakia da haundiena: {d}"
    else:        
        return("Ez dago zenbaki altuen bakarra, batzuk balio altuen berdina dute.")

print(zenb_haundiena(a, b, c, d))