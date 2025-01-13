import matplotlib.pyplot as plt
import numpy as np

filepath = "human dna original.fa"
delkaseq = 150
testfilepath = "test.fa"

with open(filepath, 'r') as openfile:
    fileitems = openfile.read()
with open(testfilepath, "w") as writefile:
    writefile.write("")

count = 0
tempstr = ""
sekvencelist = []

#lowkey zbytecny ale chtel jsem to zkusit 
for i in fileitems: 
    if i != "\n":
        count += 1
        tempstr += i
        if count == delkaseq:
            tempstr += "|" 
            with open(testfilepath, "a") as writefile:
                writefile.write(tempstr)
            count = 0
            tempstr = ""
with open(testfilepath, "a") as writefile:
                writefile.write(tempstr)


with open(testfilepath, 'r') as newopenfile:
    newfileitems = newopenfile.read()

tempstr = ""
sekvencelist = []
counter = 1
for i in newfileitems:
    if i !=  "|":
       tempstr += i
    else:
        sekvencelist.append(f"{counter}. {tempstr}")
        counter +=1 
        tempstr = ""

#pocitani zastoupeni, gc
keepcount_a = 0
keepcount_t = 0
keepcount_g = 0
keepcount_c = 0
counter = 1
zastoupenilist = []
gcrozdillist = []
gcrozdilvalues = []
for i in sekvencelist:
    templist = []
    count_a = 0
    count_t = 0
    count_g = 0
    count_c = 0
    for g in i:
        if g == "A":
            count_a +=1
        if g == "T":
            count_t +=1
        if g == "G":
            count_g +=1
        if g == "C":
            count_c +=1     
    keepcount_a += count_a
    keepcount_t += count_t
    keepcount_g += count_g
    keepcount_c += count_c
    gcrozdilvalues.append(f"{((count_g + count_c)/delkaseq)*100:.1f}")
    counter += 1
    # zastoupenilist.append((f"{counter}. | Pocet A :{count_a} | Pocet T :{count_t} | Pocet G :{count_g} | Pocet C :{count_c}| "))
    # gcrozdillist.append((f"{counter}. | GC obsah: {((count_g + count_c)/delkaseq)*100:.1f}%"))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,8))

nukleotidy = [keepcount_a, keepcount_t, keepcount_g, keepcount_c]
labels = [f"Nukleotid A","Nukleotid T","Nukleotid G","Nukleotid C" ]
axes[0].pie(nukleotidy,labels = labels, autopct='%1.1f%%')
axes[0].set_title('Procentuální zastoupení nukleotidů.')

axes[1].plot(np.arange(counter-1),gcrozdilvalues, marker = "o")
plt.xlabel("pocet sekvenci")
plt.ylabel("procenta gc")
axes[1].set_title('Rozsah a průměr GC obsahu')

fig.tight_layout()
plt.grid()
plt.show()



          
