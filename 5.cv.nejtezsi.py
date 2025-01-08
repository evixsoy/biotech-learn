#mozna to neni dodelany nevim, limituji me genetic code a chatgpt ktery v tom dela taky chyby

filepath = "human dna original.fa"

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
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# rnaitems = "AUGCGUACGUUUGA"
# rnaitems = "AUGGGUUUAA"
# rnaitems = "AUGCUGCGCAGCUUGGCCUUGCCGAUGCCCCCAGCUUGGCGGAUGGACUCUAG"
# rnaitems = "AUGUCAGAGCAACGGCCCAAGUCUGGGUCUGGGGGGGAAGGUGUCAUGGAGCCCCCUACGAUUCCCAGUCGUCCUCGUCCUCCUCUGCCUGUGGCUGCUGCGGUGGCGGCAGAGGAGGGAUGGAGUCUAA"
rnaitemslen = len(rnaitems)
fileitemsdnalen = len(fileitemsdna)

found = ""
startval =0
sekvencelist = []
koncicikodony = []
output = []
counter = 0


for i in range(0,rnaitemslen-2):
    trojice = rnaitems[i] +rnaitems[i+1] +rnaitems[i+2]
    if trojice == "AUG" or startval ==1 :
        startval = 1
        found += rnaitems[i+3]
        if counter <3:
            counter +=1
        else:
            for g in range(1,(len(found))-2):
                trojicecheck = found[g] +found[g+1] +found[g+2]
                if trojicecheck == "UAA" or trojicecheck == "UAG" or trojicecheck == "UGA":
                    found = found[:-3]
                    sekvencelist.append(found)
                    found = ""
                    startval = 0

check = 0
for i in sekvencelist:
    translation = "M"
    if len(i) > 10:
        for g in range(0, len(i)-2, 3):
            trojice = i[g] + i[g+1] + i[g+2]
            check = 0
            for j in genetic_code:
                searchval = f"{j}"
                if searchval == trojice:
                    print("found", trojice)
                    check = 1
                    translation += genetic_code.get(j)
                    break  
            if check == 0:  
                print("not found", trojice)
                translation += "?"  
    else:
        for g in range(0, len(i), 3):
            trojice = i[g] + i[g+1] + i[g+2]
            check = 0
            for j in genetic_code:
                searchval = f"{j}"
                if searchval == trojice:
                    check = 1
                    translation += genetic_code.get(j)
                    break  
            if check == 0:  
                translation += "?" 
    output.append(translation + "_")                   
for i in range(len(output)):
    print(f"DNA Sekvence: {sekvencelist[i]}, \n Překlad protein: {output[i]}\n")

