
with open(f"datasets/rosalind_grph.txt", "r") as fileread:
    test = fileread.read()

#1. prevedeni fasta stringu(datasetu) do listu
listvalues = []
listnazvy = []
string = ""
for i in test:
    if i != "\n":
        if i == ">":
            if len(string) != 1:
                #kdyby to cislo za rosalind(v datasetu ) bylo jinaci tak upravit
                listvalues.append(string[13:])
                listnazvy.append(string[:13])
                string = ""
        else:
            string += i
listvalues.append(string[13:])
listnazvy.append(string[:13])
listvalues.pop(0)
listnazvy.pop(0)

#checkuje posledni tri znaky iprvku s prvnima trema gprvku -> nalezeni overlapu
konstanta = 3
listpozic = []
pozice = []
for i in range(len(listvalues)):
    for g in range(len(listvalues)): 
        if listvalues[i] != listvalues[g]:
            if str(listvalues[i][-konstanta:]) == str(listvalues[g][:konstanta]): #check posledni tri symboly a prvni tri
                
                # print(listvalues[i][-konstanta:],listvalues[g][:konstanta], "SUCCESS")
                pozice.append(listvalues.index(listvalues[i]))
                pozice.append(listvalues.index(listvalues[g]))
                listpozic.append(pozice)
                pozice = []      
print(listpozic)

#print funkce
for i in listpozic:
    index1,index2 = i
    print(f"{listnazvy[index1]} {listnazvy[index2]}")

