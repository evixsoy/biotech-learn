#raw = s mezerama 

filepath = "human dna original.fa"

with open(filepath, 'r') as openfile:
    fileitemsdna = openfile.read()

def translateToRNA(soubor):
    translation = ""
    for i in soubor:
        if i == "T":
            i = "U"
        translation+= i
    return translation

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
                for g in range(i+3,len(soubor)-3,3):
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
    return filtrmezer(raw,soubor)

def filtrmezer(raw,soubor):
    filtr = []
    for i in raw:
        string = ""
        for g in range(len(i)):
            znak = i[g]
            if znak  == "\n" :
                pass
            else:
                string+=znak
        filtr.append(string)
    filtr[len(filtr)-1] += soubor[len(soubor)-1]
    return filtr

def search(seznam):
    genetic_code = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '|Stop', 'UAG': '|Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': '|Stop', 'UGG': 'W',
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
        vazba = "Start->"
        for i in range(0,len(g) -2,3):
            searchznak1= g[i]
            searchznak2= g[i+1]
            searchznak3= g[i+2]
            for k in genetic_code:
                if k == searchznak1 + searchznak2 + searchznak3:
                    # print(f"Found {k}, {genetic_code[k]}")
                    found =1
                    vazba +=genetic_code[k]
            if found == 0:
                # print(f"NOT FOUND {k}")
                vazba += genetic_code[k]
        completion.append(vazba)
    return completion

RNAitems = translateToRNA(fileitemsdna)
filtr = filtr(RNAitems)
print(filtr)
print(search(filtr))

# search(seznam)

#TODO projizdet seznam po trech znacich a hledat aminokys., kdyz nenajde v listu hodi err
#TODO export do csv nebo neco,
#TODO nejaka dalsi vizualizace
#pozn kdyz je v ATG dalsi ATG nez se ukonci search pro koncici aminokys. dalsi item je ten atg v predchozim atg:
    #[atgCTAGGCatgCCGGTTtga, atgCCGGTTtga] -> asi to tak nema byt
#TODO nekdy to nenajde koncici kodon
