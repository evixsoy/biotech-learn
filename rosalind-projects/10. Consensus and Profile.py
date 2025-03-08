with open(f"datasets/rosalind_cons.txt", "r") as fileread:
    test = fileread.read()

#1. prevedeni fasta stringu do listu
listvalues = []
string = ""
for i in test:
    if i != "\n":
        if i == ">":
            if len(string) != 1:
                listvalues.append(string[13:])
                string = ""
        else:
            string += i
listvalues.append(string[13:])
listvalues.pop(0)


#2.  vytvoreni matrixu
matrix = []
templist = []
for i in listvalues:
    for g in i:
        templist.append(g)
    matrix.append(templist)
    templist = []

#3. udela matrix znaku pod sebou, melo by se to jmenovat line protoze to je sloupec xdd
row = []
rowmatrix = []
for i in range(len(matrix[0])):
    for g in range(len(matrix)):
        row.append(matrix[g][i])
    rowmatrix.append(row)
    row =[]

#4. secte rowmatrix, udela list ve kterych jsou indexy nejvetsich cisel 
count_a,count_t,count_g,count_c = 0,0,0,0
nejvindexlist = []
profilenums = []
for i in range(len(rowmatrix)):
    countlist = []
    for g in rowmatrix[i]:
        if g == "A":
            count_a += 1
        elif g == "T":
            count_t += 1
        elif g == "G":
            count_g += 1
        elif g == "C":
            count_c += 1
    countlist.append(count_a)
    countlist.append(count_t)
    countlist.append(count_g)
    countlist.append(count_c)
    count_a,count_t,count_g,count_c = 0,0,0,0

    nejvcislo = 0
    nejvindex = 0
    for k in countlist:
        if k > nejvcislo:
            nejvcislo = k
            nejvindex = countlist.index(k)
    nejvindexlist.append(nejvindex)

    profilenums.append(countlist)

#5. predelani indexu na pismena
consensus =""
for g in nejvindexlist:
    if g == 0:
        consensus += "A"
    elif g == 1:
        consensus += "T"
    elif g == 2:
        consensus += "G"
    elif g == 3:
        consensus += "C"


#6. Profile format printu /// neni potreba
tempstr = ""
symbols =["A","T","G","C"]
count = 0
print(consensus)
for i in range(len(profilenums[0])):
    for g in range(len(profilenums)):
        tempstr += str(profilenums[g][i]) + " "
    print(f"{symbols[count]}: {tempstr}")
    count +=1
    tempstr =""

#1.program vyfiltruje dataset
#2.udela z neho matrix dna stringu(https://rosalind.info/problems/cons/)
#3.udela matrix sloupcu znaku
#4. secte vsechny znaky, najde nejvetsi cislo -> ulozi si jeho index na vytvoreni consensus
#5. indexy predela na znaky -> consensus
#6. print aby mi to prijal rosalind (poradi a,t,g,c mam stejne naopak nez na rosalind (nepodstatny))

#program vezme dna stringu z souboru, udela z nich "tabulku dna stringu", z sloupcu udela Profile (tabulka s cisly, v sloupcich je zastouopeni danych a,t,g,c)
#z nejvetsich cisel v kazdem sloupcu priradi pismeno a tim vznika consensus

#consensus -> kdyz je tabulka dna tak v podstate se vytvori jedno dna ktere je jakoby spojeni ty tabulky

#idk uz to neumim vysvetlit (https://rosalind.info/problems/cons/)