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

# inputvalue = "ATGCGATGCGTACGATG"
# searchvalue = "GCG"
# inputvaluelist = []
# searchvaluelist = []
# found = 0
# foundloc = ""

# for i in inputvalue:
#     if i =="A" or i=="T" or i =="G" or i=="C":
#         inputvaluelist.append(i)
#     else:
#         print("Neplatne znaky")

# for i in searchvalue:
#     if i =="A" or i=="T" or i =="G" or i=="C":
#         searchvaluelist.append(i)
#     else:
#         print("Neplatne znaky")

# searchvaluelen = len(searchvalue)
# templist = []

# for i in range(0, len(inputvalue)-2):
#     for g in range(0,searchvaluelen):
#         templist.append(inputvalue[i+g])

#     if templist == searchvaluelist:
#         print("nalezeno")
#         print(i)
#         found +=1
#         foundloc = foundloc + f"{i+1}|" 
#     templist.clear()

# print(f"pocet vyskytu:{found}")
# print(f"nalezeno na :{foundloc}")





# Projekt 4: Statistika DNA sekvence
# Cíl projektu: Analyzovat DNA sekvenci a vytvořit statistiku obsahující:

# Počty jednotlivých nukleotidů (A, T, G, C).
# GC obsah (poměr nukleotidů G a C k celkové délce sekvence).
# Délku sekvence.
# (Volitelné) Distribuci velikosti genů (pokud FASTA obsahuje více sekvencí).

# filepath = "human dna.fa"
# delkaseq = 25

# with open(filepath, 'r') as openfile:
#     fileitems = openfile.read()
# #pro jednotlive delkaseq

# listitems = []
# for i in fileitems:
#     if i =="\n":
#         pass
#     else:
#         listitems.append(i)

# dictseq= {}
# pocet = len(fileitems)//delkaseq
# print(pocet)
# for g in range(pocet):
#     templist =[]
#     for i in range(delkaseq):
#         index = g * delkaseq + i 
#         if index >= len(listitems):  
#             break
#         templist.append(listitems[index])
#         if i == delkaseq-1:
#             dictseq[g] = templist
#     if g >= pocet-1:
#         break
#     else:
#         count_a = 0
#         count_t = 0
#         count_g = 0
#         count_c = 0
#         if index >= len(listitems): 
#             break
#         for i in dictseq[g]:
#              if i == "A":
#                 count_a +=1
#              elif i == "T":
#                  count_t +=1
#              elif i == "G":
#                  count_g +=1
#              elif i == "C":
#                 count_c +=1
#         print(f"{g+1}. Sekvence | Pocet A :{count_a} | Pocet T :{count_t} | Pocet G :{count_g} | Pocet C :{count_c}| GC obsah: {((count_g + count_c)/delkaseq)*100:.1f}%")

#pro celou sekvenci
# count_a = 0
# count_t = 0
# count_g = 0
# count_c = 0

# for i in fileitems:
#     if i == "A":
#         count_a +=1
#     elif i == "T":
#         count_t +=1
#     elif i == "G":
#         count_g +=1
#     elif i == "C":
#         count_c +=1
# print(f"Pocet A :{count_a}\nPocet T :{count_t}\nPocet G :{count_g}\nPocet C :{count_c}")
# print(f"delka: {len(fileitems)}")
# print(f"GC obsah: {((count_g + count_c)/len(fileitems))*100:.1f}%")










# 5. Překlad DNA do proteinů
# Popis:
# Program by měl:
# Převést DNA sekvenci na RNA (A → U, T → A, G ↔ C).
# Přeložit RNA sekvenci do aminokyselin (pomocí genetického kódu).
# Vypisovat odpovídající proteiny.
# Klíčové dovednosti:
# Použití slovníků pro genetický kód.
# Zpracování dat v blocích (tripletech).


filepath = "human dna.fa"

with open(filepath, 'r') as openfile:
    fileitemsdna = openfile.read()

#preklad do rna
rnaitems = ""
for i in fileitemsdna:
    if i == "T":
        rnaitems += "U"  
    elif i != "\n":  
        rnaitems += i
#kodovani do proteinu

# Tabulka genetického kódu
genetic_code = {
    "ATA":"I", "ATC":"I", "ATT":"I",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y"
}
start = "AUG"
end = ["TAA", "TAG", "TGA"]
rnaitemslen = len(rnaitems)

found = ""
hledani = 0
pocitadlo =0
check = 0
for i in range(1,rnaitemslen-2):
    trojice = rnaitems[i] +rnaitems[i+1] +rnaitems[i+2]     
    if hledani <3:
        hledani +=1
    elif hledani ==3:
        if trojice == "UAA" or trojice =="UAG" or trojice == "UGA" or trojice == start:
            pass
        else:
            found+=trojice
    # print(rnaitems[i] +rnaitems[i+1] +rnaitems[i+2]
    if trojice == start and check ==1:
        hledani = 0
        check =0
    if trojice == start:
        print("found")
        found+=trojice
        hledani =1
        check = 1
    if trojice == "UAA" or trojice =="UAG" or trojice == "UGA":
        hledani = 0
        print(found)
        found =""
        check = 0


