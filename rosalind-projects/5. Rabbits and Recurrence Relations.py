#https://www.figma.com/design/bZ9W6PMRNvBUlfmJQith0f/Untitled?node-id=0-1&p=f&t=AfZaePpDieXo9gHb-0

print(f"Zadej počet měsíců:")
month_input = int(input(">"))
print(f"Zadej počet rozm. párů:")
rozmpary_input = int(input(">"))

def vypocet(month,rozmpary):
    #prvni mesic je pouze jeden mladej kralik
    d,m =0,1
    for i in range(month -1):
        # mlady kralici jsou dospeli krat koeficient rozmnozovani, dospeli jsou dospeli kralici plus mladi kralici z minulyho mesice (vyrostli)
        m,d = d*rozmpary , d +m
    return m+d

print(vypocet(month_input, rozmpary_input))