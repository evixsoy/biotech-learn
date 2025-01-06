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
for i in range(1,fileitemsdnalen-2):
    trojice = fileitemsdna[i] +fileitemsdna[i+1] +fileitemsdna[i+2]     
    if trojice == "ATG" or startval ==1 :
        print("found")
        startval =1
        opak = 1
        if counter < 3:
            counter +=1
        elif counter ==3 :
            print(trojice)
            found+=trojice
            opak = 0
            counter = 1
            again =1
            if trojice == "TAA" or trojice == "TAG" or trojice == "TGA" or trojice == "ATG":
                startval = 0
                print("break")
                testlist.append(found)
                counter = 0
                found = ""
                test =0
            if i == fileitemsdnalen-3:
                print("KONEC NENALEZEN")
                
print(testlist)
            

        
