dna_seq = "AGGTTGATGGAAGATCTTGTGCTTGCCAGTTCAATACCATGAGGGCGGCGAATCCGGTGTAACGAGACCCTAAAGTCCTTGGCAACCTGAGGGATTGAGGTAGAAAGCTCTATGGTTGCAGACTTTAGCTGTACGCCTCAAAAAGCGTCTAACGGAGATCGGAGATCCCCCACTAGAAAACGCCCCGACCCCAAAATACATTCTCTGATCGGCGGCAGTATCCGTCAGGTTCTACTATCTGAGAGGGAGCACATGTCAGAGGATTAACCGCTGTCATTGTAAACCAGTGAAGTAGGGTCGACCAGGTTCCGGTCGAACTACAGGTGATGTGGTGCCCTTTGCGCGACATAATAGCGATATAGTGGTACATGGGTCTACCCCCAGTCAACACTGCGTAACAACTGGTAAATGAGTGTCAGGATCTGCCATGTCTATGGCGTCGTCACACTAGCGGAATTGGGCAAACCTTGACTTGGTGCTGTGGATCGTGTGCAGGTATCAATCCTCGTCCTTGACCTATCCTCGTTAGGGTCTGCTTGCAAGAGATGTCCGAGTGACAGGTGGTCGTGGTTATTGAGACCTGACTTTCACCGTCGCCATCTAGCTTACTCGCACCGAGCGTCACTAATACCTCGTATACTGAGTTGGAGTAGGCATCGAGGTGGTCAGAAGCGCCGGCCGCCTCCGGGCAGCATGAATCGGCTATGTTGTTGGTTACTTAACCCGTCACACGGGAAAAGCTTTGAACATCATCGTTACAATAATCGGTGAGGGAGCGCAAGAAGAAAAGTTGCCACCCACGACAGCTAAGTTATCTGTACCTCAGTATGACTCGGATTCG"

reverse_complement = ""
#prekonvertuje seq
for i in dna_seq:
    if i == "A":
        reverse_complement += "T"
    elif i =="T":
        reverse_complement += "A"
    elif i == "G":
        reverse_complement += "C"
    elif i == "C":
        reverse_complement += "G"
        
#print pozpatku aby vznikl reverse complement
print(reverse_complement[::-1])
