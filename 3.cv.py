# Projekt 3: Hledání podsekvencí v DNA
# Cíl projektu: Vytvořit program, který:

# Načte DNA sekvenci od uživatele nebo ze souboru.
# Hledá, kolikrát se v sekvenci vyskytuje určitá podsekvence (například ATG).
# Zobrazí všechny pozice, na kterých se podsekvence nachází (volitelně).

inputvalue = "ATGCGATGCGTACGATG"
searchvalue = "GCG"
inputvaluelist = []
searchvaluelist = []
found = 0
foundloc = ""

for i in inputvalue:
    if i =="A" or i=="T" or i =="G" or i=="C":
        inputvaluelist.append(i)
    else:
        print("Neplatne znaky")

for i in searchvalue:
    if i =="A" or i=="T" or i =="G" or i=="C":
        searchvaluelist.append(i)
    else:
        print("Neplatne znaky")

searchvaluelen = len(searchvalue)
templist = []

for i in range(0, len(inputvalue)-2):
    for g in range(0,searchvaluelen):
        templist.append(inputvalue[i+g])

    if templist == searchvaluelist:
        print("nalezeno")
        print(i)
        found +=1
        foundloc = foundloc + f"{i+1}|" 
    templist.clear()

print(f"pocet vyskytu:{found}")
print(f"nalezeno na :{foundloc}")