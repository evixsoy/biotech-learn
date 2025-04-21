import time
start_time = time.time() 

with open(f"datasets/rosalind_lcsm (1).txt", "r") as fileread:
    rawdata = fileread.read()

listvalues = []
string = ""
for i in rawdata:
    if i != "\n":
        if i == ">":
            if len(string) != 1:
                #kdyby to cislo za rosalind(v datasetu ) bylo jinaci tak upravit
                listvalues.append(string[13:])
                string = ""
        else:
            string += i
listvalues.append(string[13:])
listvalues.pop(0)

#1.
#vytvoreni vsech kombinaci pro prvni prvek v listu
def createfirst():
    for k in range(2, len(listvalues[0])+1): 
        for g in range(len(listvalues[0])): 
            substring = listvalues[0][g:g+k]  # vezme úsek
            maintemp.add(substring)

#2.
def compare(maintemp):
    for i in range(1, len(listvalues)):
        maintemplist_2 = set()
        for k in range(2, len(listvalues[i])+1):
            for g in range(len(listvalues[i])):
                substring = listvalues[i][g:g+k]
                maintemplist_2.add(substring)
        maintemp = maintemplist_2.intersection(maintemp)
    return maintemp

maintemp = set()
createfirst()

vysledek = compare(maintemp)
vysledek = list(vysledek)
vysledek.sort(key=len, reverse=True)
print(vysledek[0])

end_time = time.time() # mereni casu trvani programu
execution_time = end_time - start_time
print(f"Program běžel {execution_time:.5f} sekund.")

#1.vytahne prvni skupinu a udela z vsech znaku vsechny kombinace (dvojice,trojice,...) a da je do setu
#2. vezme druhou skupinu, udela vsechny dvojice,trojice,... a porovna s setem prvni skupiny (udela intersection -> v setu bude jen to co ma prvni skupina a druha skupina stejne), pote se porovnava prvni skupina s 3. skupinu atd.
#3. vysledny list se seradi podle delky (nejdelsi na zacatku) a prvni prvek v listu se vypise
