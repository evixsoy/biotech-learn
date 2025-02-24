with open(f"datasets/rosalind_gc.txt", "r") as fileread:
    test = fileread.read()

#prevedeni fasta stringu do listu
listvalues = []
string = ""
for i in test:
    if i != "\n":
        if i == ">":
            if len(string) != 1:
                listvalues.append(string)
                string = ""
        else:
            string += i
listvalues.append(string)
listvalues.pop(0)

#vypocitani gc 
gc_content_list = []
for i in listvalues:
    count = 0
    content = i[13:]
    for g in content:
        if g == "G" or g == "C":
            count +=1 
    gc_content = count/len(content)
    gc_content_list.append(gc_content)

#nalezeni nejvetsiho cisla
count = 0
tempnum = 0 # nejvcislo
pozice_nejvcisla = 0
for i in gc_content_list:
    count += 1
    if i >= tempnum:
        tempnum=i
        pozice_nejvcisla = count

#propojeni fasta nazvu a nejv cisla
nejvetsi_cislo = f"{tempnum*100:.6f}"
nazev_nejvcisla = listvalues[pozice_nejvcisla-1]

print(f"{nazev_nejvcisla[:13]}\n{nejvetsi_cislo}")




