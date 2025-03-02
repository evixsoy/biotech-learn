#idk jestli to funguje na 100%, blbe se overuje

filepath = "human dna original.fa"

with open(filepath, 'r') as openfile:
    fileitemsdna = openfile.read()

fileitemsdna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
#filtr mezer z souboru oddela mezery \n
def filtrmezer(soubor):
    string = ""
    for i in soubor:
            if i  == "\n" :
                pass
            else:
                string+=i
    return string

#predela dna soubor do rna("predela T -> U")
def translateToRNA(soubor):
    translation = ""
    for i in soubor:
        if i == "T":
            i = "U"
        translation+= i
    return translation

#filtr prochazi jednotlive znaky a hleda zacatecni kodon "ATG" -> jede dalsi loop dokud nenajde koncici kodon "UAG/UAA/UGA" a mezitim vse dava do listu raw
def filtr(soubor,):
    raw = []
    konec = 0
    for i in range(len(soubor)-2):
        string ="AUG"
        konec = 0
        prvniznak = soubor[i]
        druhyznak = soubor[i+1]
        tretiznak = soubor[i+2]
        if prvniznak + druhyznak + tretiznak =="AUG":
            # print(f"found:{prvniznak + druhyznak + tretiznak}| pozice: {i+3}")
            while konec != 1:
                for g in range(i+3,len(soubor)-3):
                    pendingznak1 = soubor[g]
                    pendingznak2 = soubor[g+1]
                    pendingznak3 = soubor[g+2]
                    check = pendingznak1 + pendingznak2 + pendingznak3
                    if check == "UAG":
                        break
                    elif check == "UAA":
                        break
                    elif check == "UGA":
                        break
                    else:
                        string += check
                string += check
                raw.append(string)
                konec =1
    return raw

#vezme list raw a projizdi trojice a porovnava je s seznamem kodonu a proteinu(?) a dosazuje do protein finalniho stringu
def search(seznam):
    genetic_code = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
    'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
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
    found =0
    completion = [""]
    for g in seznam:
        vazba = ""
        for i in range(0,len(g) -2,3):
            searchznak1= g[i]
            searchznak2= g[i+1]
            searchznak3= g[i+2]
            for k in genetic_code:
                if k == searchznak1 + searchznak2 + searchznak3:
                    found =1
                    vazba +=genetic_code[k]
            if found == 0:
                vazba += "?"
        completion.append(vazba)
    return completion

#chod programu aby vse posilalo spravna data a slo spravne postupne
filtrmezer = filtrmezer(fileitemsdna)
RNAitems = translateToRNA(filtrmezer)
filtr = filtr(RNAitems)
print(filtr)
vysledek = search(filtr)

#simple print
count= 0
for i in vysledek:
    # print(f"{count}. vazba | {vysledek[count]} ")
    print(vysledek[count])
    count += 1


#TODO export do csv (pandas ) nebo neco
#TODO nejaka dalsi vizualizace(kolik procent je zastoupeno: A,U,G,C, )
