# https://www.figma.com/design/bZ9W6PMRNvBUlfmJQith0f/Untitled?node-id=0-1&p=f&t=AfZaePpDieXo9gHb-0

nazvy = ['k','m','n']
cisla = []
typy_organismu = ["AA", "Aa", "aa"]

print(f"Zadej počet k:")
cisla.append(int(input(">")))
print(f"Zadej počet m:")
cisla.append(int(input(">")))
print(f"Zadej počet n:")
cisla.append(int(input(">")))

percentage_list = []
for i in nazvy:
    #1. hledani citatelu + vypocitani probability
    prvek1_index = nazvy.index(f"{i}")
    prvek1_citatel = cisla[prvek1_index]
    prvek1_probability = prvek1_citatel/sum(cisla)
    for g in nazvy:
        if g==i:
            prvek2_check = 0
            prvek2_citatel = prvek1_citatel - 1
        else:
            prvek2_check = 1
            prvek2_index = nazvy.index(f"{g}")
            prvek2_citatel = cisla[prvek2_index]
        prvek2_probability = prvek2_citatel/(sum(cisla)-1)

        #2. sestaveni tabulky na krizeni typu organismu
        prvek1_typorg = typy_organismu[prvek1_index]
        if prvek2_check == 0:
            row_1 = [prvek1_typorg[0],prvek1_typorg[1] ]
            row_2 = row_1
        else:
            prvek2_typorg = typy_organismu[prvek2_index]
            row_1 = [prvek1_typorg[0],prvek1_typorg[1] ]
            row_2 = [prvek2_typorg[0],prvek2_typorg[1] ]
        
        #3. slozeni vysledku krizeni typu organismu
        tabulka =[]
        for k in row_1:
            for l in row_2:
                tabulka.append(k+l)
        
        #quick fix aA
        for u in tabulka:
            if u == "aA":
                indexfix = tabulka.index(u)
                tabulka[indexfix] = "Aa"

        #4. scitani procent tabulky, secteni procent krizeni a odds citatelu
        tabulka_odds = []
        count = 0
        for f in typy_organismu:
            for p in tabulka:
                if f == p :
                    count += 25
            tabulka_odds.append(count)
            count = 0
            if len(tabulka_odds) ==1:
                percentage = (tabulka_odds[0])/100
            if len(tabulka_odds) > 1:
                percentage = (tabulka_odds[0] + tabulka_odds[1])/100
        tabulka_odds = []
        print(f"{i}:{g} -> {percentage* (prvek1_probability * prvek2_probability)}")
        percentage_list.append(percentage* (prvek1_probability * prvek2_probability))

print(percentage_list)
print(sum(percentage_list))


#1. program vypocita podle cisel k,m,n (a jejich inputu) pravdepodobnost padnuti(napriklad pravdepodobnost toho ze padne k,m apod.) ->  viz figure 2 https://rosalind.info/problems/iprb/
#2. podle toho co to je za znaky k,m,n se priradi AA, Aa, aa a vytvori se tabulka ktera se pouziva na krizeni -> viz prostredni obrazek v figma linku nahore
#3. podle tabulky se do listu zaradi vysledky krizeni urcitych allelu(AA,Aa,aa)
    #quickfix -> nekdy pri krizeni muze dojit ze misto Aa je aA -> loop pouze preradi z aA na Aa
#4. vezme vysledky pravdepodobnosti z 1. a vypocita procenta podle polozek z listu vysledku krizeni -> tyto vysledky vynasobi
#5. secteni vysledku 4. u vsech kombinaci da finalni vysledek

        



