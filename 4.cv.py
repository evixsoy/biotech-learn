# Projekt 4: Statistika DNA sekvence
# Cíl projektu: Analyzovat DNA sekvenci a vytvořit statistiku obsahující:

# Počty jednotlivých nukleotidů (A, T, G, C).
# GC obsah (poměr nukleotidů G a C k celkové délce sekvence).
# Délku sekvence.
# (Volitelné) Distribuci velikosti genů (pokud FASTA obsahuje více sekvencí).

filepath = "human dna original.fa"
delkaseq = 25

with open(filepath, 'r') as openfile:
    fileitems = openfile.read()
#pro jednotlive delkaseq

listitems = []
for i in fileitems:
    if i =="\n":
        pass
    else:
        listitems.append(i)

dictseq= {}
pocet = len(fileitems)//delkaseq
print(pocet)
for g in range(pocet):
    templist =[]
    for i in range(delkaseq):
        index = g * delkaseq + i 
        if index >= len(listitems):  
            break
        templist.append(listitems[index])
        if i == delkaseq-1:
            dictseq[g] = templist
    if g >= pocet-1:
        break
    else:
        count_a = 0
        count_t = 0
        count_g = 0
        count_c = 0
        if index >= len(listitems): 
            break
        for i in dictseq[g]:
             if i == "A":
                count_a +=1
             elif i == "T":
                 count_t +=1
             elif i == "G":
                 count_g +=1
             elif i == "C":
                count_c +=1
        print(f"{g+1}. Sekvence | Pocet A :{count_a} | Pocet T :{count_t} | Pocet G :{count_g} | Pocet C :{count_c}| GC obsah: {((count_g + count_c)/delkaseq)*100:.1f}%")

# pro celou sekvenci
count_a = 0
count_t = 0
count_g = 0
count_c = 0

for i in fileitems:
    if i == "A":
        count_a +=1
    elif i == "T":
        count_t +=1
    elif i == "G":
        count_g +=1
    elif i == "C":
        count_c +=1
print(f"Pocet A :{count_a}\nPocet T :{count_t}\nPocet G :{count_g}\nPocet C :{count_c}")
print(f"delka: {len(fileitems)}")
print(f"GC obsah: {((count_g + count_c)/len(fileitems))*100:.1f}%")