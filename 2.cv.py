# 2. Reverzní komplement DNA
# Popis:
# Vytvoř nástroj, který:

# Načte DNA sekvenci.
# Vrátí její reverzní komplement (vymění A ↔ T a G ↔ C, a zároveň otočí sekvenci).

sequence = "AAGCTTGACCTG"
changedseq  = ""
reversechseq  = ""

for i in sequence:
    if i == "A":
        i = "T"
    elif i == "T": 
        i = "A"
    elif i == "G":
        i = "C"
    elif i == "C": 
        i = "G"
    changedseq = changedseq + i

print(changedseq)
print(changedseq[::-1])

