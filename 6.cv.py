# 6. Výpočet GC obsahu
# Popis:
# GC obsah (podíl G a C v DNA) je důležitým ukazatelem. Napiš program, který:
# Spočítá procentuální podíl G a C v DNA sekvenci.
# Umožní porovnat GC obsah mezi dvěma sekvencemi.
# Klíčové dovednosti:
# Matematické výpočty.
# Porovnávání dat.

filepath = "human dna original.fa"
delkaseq = 25

with open(filepath, 'r') as openfile:
    fileitems = openfile.read()
#pro jednotlive delkaseq

#rozdeleni na sekvcence
sekvencelist = []
sekvencetemp = ""
counter = 0
ovrcounter = 0
for i in fileitems:
    ovrcounter += 1
    if i != "\n":
        sekvencetemp += i
        counter += 1
        if counter == 25:
            sekvencelist.append(sekvencetemp)
            sekvencetemp = ""
            counter = 0
        elif ovrcounter == len(fileitems):
            sekvencelist.append(sekvencetemp)
print(sekvencelist)

#zjisteni
pocet = 0
for i in range(len(sekvencelist)):
    pocet += 1
    sekvence = sekvencelist[i]
    count_g = 0
    count_c = 0
    for i in sekvence:
        if i == "G":
            count_g +=1
        elif i =="C":
            count_c +=1
            
    print(f"{pocet}. Sekvence| GC obsah : {((count_g + count_c)/delkaseq)*100:.1f}%")
    

