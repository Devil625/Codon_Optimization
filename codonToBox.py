f2 = open("C:/Users/55499/Desktop/NCRFpp/ques/MmpI3(b).txt",'w') #output
f3 = open("C:/Users/55499/Desktop/NCRFpp/ques/MmpI3.txt",'r') #input

line = ''
i = 0
count = 0
err=0
for line in f3:
    line = line.strip('\n')
    while i <len(line):
        s=line[i]+line[i+1]+line[i+2]
        if s == 'TTT':
            o = 'F'
            w='a'
        elif s == 'TTC':
            o = 'F'
            w = 'b'
        elif s == 'TTA':
            o = 'L'
            w = 'c'
        elif s == 'TTG':
            o = 'L'
            w = 'd'
        elif s == 'TCT':
            o = 'S'
            w = 'b'
        elif s == 'TCC':
            o = 'S'
            w = 'f'
        elif s == 'TCA':
            o = 'S'
            w = 'h'
        elif s == 'TCG':
            o = 'S'
            w = 'g'
        elif s == 'TAT':
            o = 'Y'
            w = 'c'
        elif s == 'TAC':
            o = 'Y'
            w = 'h'
        elif s == 'TAA':
            o = 'X'
            w = 'w'
        elif s == 'TAG':
            o = 'X'
            w = 'w'
        elif s == 'TGT':
            o = 'C'
            w = 'd'
        elif s == 'TGC':
            o = 'C'
            w = 'g'
        elif s == 'TGA':
            o = 'X'
            w = 'w'
        elif s == 'TGG':
            o = 'W'
            w = 'k'
        elif s == 'CTT':
            o = 'L'
            w = 'b'
        elif s == 'CTC':
            o = 'L'
            w = 'f'
        elif s == 'CTA':
            o = 'L'
            w = 'h'
        elif s == 'CTG':
            o = 'L'
            w = 'g'
        elif s == 'CCT':
            o = 'P'
            w = 'f'
        elif s == 'CCC':
            o = 'P'
            w = 'l'
        elif s == 'CCA':
            o = 'P'
            w = 'm'
        elif s == 'CCG':
            o = 'P'
            w = 'n'
        elif s == 'CAT':
            o = 'H'
            w = 'h'
        elif s == 'CAC':
            o = 'H'
            w = 'm'
        elif s == 'CAA':
            o = 'Q'
            w = 'o'
        elif s == 'CAG':
            o = 'Q'
            w = 'r'
        elif s == 'CGT':
            o = 'R'
            w = 'g'
        elif s == 'CGC':
            o = 'R'
            w = 'n'
        elif s == 'CGA':
            o = 'R'
            w = 'r'
        elif s == 'CGG':
            o = 'R'
            w = 's'
        elif s == 'ATT':
            o = 'I'
            w = 'c'
        elif s == 'ATC':
            o = 'I'
            w = 'h'
        elif s == 'ATA':
            o = 'I'
            w = 'i'
        elif s == 'ATG':
            o = 'M'
            w = 'j'
        elif s == 'ACT':
            o = 'T'
            w = 'h'
        elif s == 'ACC':
            o = 'T'
            w = 'm'
        elif s == 'ACA':
            o = 'T'
            w = 'o'
        elif s == 'ACG':
            o = 'T'
            w = 'r'
        elif s == 'AAT':
            o = 'N'
            w = 'i'
        elif s == 'AAC':
            o = 'N'
            w = 'o'
        elif s == 'AAG':
            o = 'K'
            w = 'u'
        elif s == 'AAA':
            o = 'K'
            w = 't'
        elif s == 'AGT':
            o = 'S'
            w = 'j'
        elif s == 'AGC':
            o = 'S'
            w = 'r'
        elif s == 'AGA':
            o = 'R'
            w = 'u'
        elif s == 'AGG':
            o = 'R'
            w = 'q'
        elif s == 'GTT':
            o = 'V'
            w = 'd'
        elif s == 'GTC':
            o = 'V'
            w = 'g'
        elif s == 'GTA':
            o = 'V'
            w = 'j'
        elif s == 'GTG':
            o = 'V'
            w = 'k'
        elif s == 'GCT':
            o = 'A'
            w = 'g'
        elif s == 'GCC':
            o = 'A'
            w = 'n'
        elif s == 'GCA':
            o = 'A'
            w = 'r'
        elif s == 'GCG':
            o = 'A'
            w = 's'
        elif s == 'GAT':
            o = 'D'
            w = 'j'
        elif s == 'GAC':
            o = 'D'
            w = 'r'
        elif s == 'GAA':
            o = 'E'
            w = 'u'
        elif s == 'GAG':
            o = 'E'
            w = 'q'
        elif s == 'GGT':
            o = 'G'
            w = 'k'
        elif s == 'GGC':
            o = 'G'
            w = 's'
        elif s == 'GGA':
            o = 'G'
            w = 'q'
        elif s == 'GGG':
            o = 'G'
            w = 'p'
        else:
            err = err+1
        s2=o+" "+w
        f2.writelines(s2+"\n")
        i=i+3
        if o=='X':
            f2.write('\n')
            anino=''
    s1 = ''
    s2=''
    line = ''
    flag = 0
    i=0
