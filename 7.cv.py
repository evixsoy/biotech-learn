from random import randint

oddslist_a = []
oddslist_g= []
oddslist_t = []
oddslist_c = []
tempstring = ""
found = 0
generatedDNA = ""

delkaseq = 25
podil = {
    "A" : 50,
    "G" : 30,
    "T" : 1,
    "C" : 19
}

#check jestli podil = 100
podilcheck = podil.get("A") + podil.get("G") + podil.get("T") + podil.get("C")
if podilcheck != 100:
    print("podíl musí dávat dohromady 100!")
else:
    #vytvoreni odds
    for i in range(1,podil.get("A")+1):
        oddslist_a.append(i)

    for i in range(podil.get("A")+1,(podil.get("G") + podil.get("A"))+1):
        oddslist_g.append(i)

    for i in range((podil.get("G") + podil.get("A"))+1,(podil.get("G") + podil.get("A") + podil.get("T"))+1):
        oddslist_t.append(i)

    for i in range((podil.get("G") + podil.get("A") + podil.get("T"))+1, (podil.get("G") + podil.get("A") + podil.get("T") + podil.get("C") )+1):
        oddslist_c.append(i)

    #generovani cisla a pote vyhledani a dosazeni do outputu podle generovanho cisla
    for i in range(delkaseq):
        found =0
        genval = randint(0,99)
        for i in oddslist_a:
            if i == genval:
               generatedDNA += "A"
               found =1
               break
        if found ==0:
            for i in oddslist_t:
                if i == genval:
                    generatedDNA += "T"
                    found =1
                    break
        if found ==0:
            for i in oddslist_g:
                if i == genval:
                    generatedDNA += "G"
                    found =1
                    break
        if found ==0:
            for i in oddslist_c:
                if i == genval:
                    generatedDNA += "C"
                    found =1
                    break       
    print(f"Generované dna: {generatedDNA} | délka: {delkaseq}")