# 1. Počítání nukleotidů v DNA sekvenci
# Popis:
# Vytvoř program, který:

# Načte DNA sekvenci ze souboru nebo zadání uživatelem.
# Spočítá, kolik je jednotlivých nukleotidů (A, T, G, C).
# Určí podíl jednotlivých nukleotidů.

sequence = "ATGCTTAGC"
count_a = 0
count_t = 0
count_g = 0
count_c = 0

for i in sequence:
    if i == "A":
        count_a +=1
    if i == "T":
        count_t +=1
    if i == "G":
        count_g +=1
    if i == "C":
        count_c +=1
print(f"Pocet A :{count_a}\nPocet T :{count_t}\nPocet G :{count_g}\nPocet C :{count_c}\n ")