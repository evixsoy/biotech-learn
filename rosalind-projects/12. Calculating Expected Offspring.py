with open("datasets/rosalind_iev (1).txt", "r") as fileread:
    contentsraw = fileread.read()

contents =[]
temp = ""
#filtr datasetu
for i in contentsraw:
    temp += i
    if i == " ":
        contents.append(int(temp))
        temp = ""
contents.append(int(temp))

pairs = 2
probability = [1,1,1,0.75,0.5,0]

#vypocet pravdepodobnosti E= 2×i=1∑6​(pi​×Pr(dom)) => E=2×(p1​×1.0+p2​×1.0+p3​×1.0+p4​×0.75+p5​×0.5+p6​×0.0) p1-6 = prvek, probability
count = 0
for i in range(len(probability)):
    count = (contents[i]*probability[i]) + count
print((count*pairs))



