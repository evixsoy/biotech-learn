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
fileitemsdnalen = len(fileitemsdna)

found = ""
hledani = 0
startval =0
check = 0
testlist = []
test = 0
counter = 0
again = 0
trojicecheck=""
for i in range(1,fileitemsdnalen-3):
    trojice = fileitemsdna[i] +fileitemsdna[i+1] +fileitemsdna[i+2]     
    if trojice == "ATG" or startval ==1 :
        print("found")
        startval =1
        found+=fileitemsdna[i+3]
        print(found)
        if len(found) >3:
            found =""
            for g in range((fileitemsdnalen-3)-i):
                found+=fileitemsdna[i+g]
                if len(found) >3:
                    trojicecheck = found[g-2] +found[g-1] +found[g] 
                if trojicecheck == "TAA" or trojicecheck == "TAG" or trojicecheck == "TGA":
                    print("break")
                    testlist.append(found)
                    found=""
                    startval=0
                    break  


                
print(testlist)
            

        
