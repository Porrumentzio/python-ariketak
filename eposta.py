badu_abil=False
badu_punt=False

helbidea=input("Sartu zure e-posta helbidea: ")

# for i in helbidea:
#     if(i=="@"):
#         badu_abil=True
#     if(i=="."):
#         badu_punt=True

if "." in helbidea:
    badu_abil=True
if "@" in helbidea:
    badu_punt=True

if badu_abil and badu_punt:
    print("Ados, aurrera egin dezakezu.")
else:
    print("Hori ez da e-posta helbide bat.")

