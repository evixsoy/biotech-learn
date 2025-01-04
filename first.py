# 1. Počítání nukleotidů v DNA sekvenci
# Popis:
# Vytvoř program, který:

# Načte DNA sekvenci ze souboru nebo zadání uživatelem.
# Spočítá, kolik je jednotlivých nukleotidů (A, T, G, C).
# Určí podíl jednotlivých nukleotidů.

# sequence = "ATGCTTAGC"
# count_a = 0
# count_t = 0
# count_g = 0
# count_c = 0

# for i in sequence:
#     if i == "A":
#         count_a +=1
#     if i == "T":
#         count_t +=1
#     if i == "G":
#         count_g +=1
#     if i == "C":
#         count_c +=1
# print(f"Pocet A :{count_a}\nPocet T :{count_t}\nPocet G :{count_g}\nPocet C :{count_c}\n ")



# 2. Reverzní komplement DNA
# Popis:
# Vytvoř nástroj, který:

# Načte DNA sekvenci.
# Vrátí její reverzní komplement (vymění A ↔ T a G ↔ C, a zároveň otočí sekvenci).

# sequence = "AAGCTTGACCTG"
# changedseq  = ""
# reversechseq  = ""

# for i in sequence:
#     if i == "A":
#         i = "T"
#     elif i == "T": 
#         i = "A"
#     elif i == "G":
#         i = "C"
#     elif i == "C": 
#         i = "G"
#     changedseq = changedseq + i

# print(changedseq)
# print(changedseq[::-1])





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
