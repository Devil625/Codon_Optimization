f = open("C:/Users/55499/Desktop/NCRFpp/ques/res-MmpI3.txt",'r') #数据源
f2= open("C:/Users/55499/Desktop/NCRFpp/ques/MmpI3(b).txt",'w') #数据格式




line = ''
count = 1
count1=0
s = ''
c=0
err = []
for line in f:
    line=line.strip('\n')
    print(line)

    if(line == ''):
        f2.writelines(s + '\n')
        s = ''
        count = count + 1
        continue
    if(line[0] == '#'):
        continue

    else:
        count1 = count1+1
        if(line == 'F a'):
            s = s + 'TTT'
        elif(line == 'F b'):
            s = s + 'TTC'
        elif(line == 'L c'):
            s = s + 'TTA'
        elif(line == 'L d'):
            s = s + 'TTG'
        elif(line == 'S b'):
            s = s + 'TCT'
        elif(line == 'S f'):
            s = s + 'TCC'
        elif(line == 'S h'):
            s = s + 'TCA'
        elif(line == 'S g'):
            s = s + 'TCG'
        elif(line == 'Y c'):
            s = s + 'TAT'
        elif(line == 'Y h'):
            s = s + 'TAC'
        elif(line == 'X w'):
            s = s + 'TAA'
        elif(line == 'C d'):
            s = s + 'TGT' 
        elif(line == 'C g'):
            s = s + 'TGC'
        elif(line == 'W k'):
            s = s + 'TGG'     
        elif(line == 'L b'):
            s = s + 'CTT'
        elif(line == 'L f'):
            s = s + 'CTC'
        elif(line == 'L h'):
            s = s + 'CTA'
        elif(line == 'L g'):
            s = s + 'CTG'
        elif(line == 'P f'):
            s = s + 'CCT'
        elif(line == 'P l'):
            s = s + 'CCC'
        elif(line == 'P m'):
            s = s + 'CCA'
        elif(line == 'P n'):
            s = s + 'CCG'
        elif(line == 'H h'):
            s = s + 'CAT'
        elif(line == 'H m'):
            s = s + 'CAC'
        elif(line == 'Q o'):
            s = s + 'CAA'
        elif(line == 'Q r'):
            s = s + 'CAG'
        elif(line == 'R g'):
            s = s + 'CGT'
        elif(line == 'R n'):
            s = s + 'CGC'
        elif(line == 'R r'):
            s = s + 'CGA'
        elif(line == 'R s'):
            s = s + 'CGG'
        elif(line == 'I c'):
            s = s + 'ATT'
        elif(line == 'I h'):
            s = s + 'ATC'
        elif(line == 'I i'):
            s = s + 'ATA'
        elif(line == 'M j'):
            s = s + 'ATG'
        elif(line == 'T h'):
            s = s + 'ACT'
        elif(line == 'T m'):
            s = s + 'ACC'
        elif(line == 'T o'):
            s = s + 'ACA'
        elif(line == 'T r'):
            s = s + 'ACG'
        elif(line == 'N i'):
            s = s + 'AAT'
        elif(line == 'N o'):
            s = s + 'AAC'
        elif(line == 'K u'):
            s = s + 'AAG'
        elif(line == 'K t'):
            s = s + 'AAA'
        elif(line == 'S j'):
            s = s + 'AGT'
        elif(line == 'S r'):
            s = s + 'AGC'
        elif(line == 'R u'):
            s = s + 'AGA'
        elif(line == 'R q'):
            s = s + 'AGG'
        elif(line == 'V d'):
            s = s + 'GTT'
        elif(line == 'V g'):
            s = s + 'GTC'
        elif(line == 'V j'):
            s = s + 'GTA'
        elif(line == 'V k'):
            s = s + 'GTG'
        elif(line == 'A g'):
            s = s + 'GCT'
        elif(line == 'A n'):
            s = s + 'GCC'
        elif(line == 'A r'):
            s = s + 'GCA'
        elif(line == 'A s'):
            s = s + 'GCG'
        elif(line == 'D j'):
            s = s + 'GAT'
        elif(line == 'D r'):
            s = s + 'GAC'
        elif(line == 'E u'):
            s = s + 'GAA'
        elif(line == 'E q'):
            s = s + 'GAG'
        elif(line == 'G k'):
            s = s + 'GGT'
        elif(line == 'G s'):
            s = s + 'GGC'
        elif(line == 'G q'):
            s = s + 'GGA'
        elif(line == 'G p'):
            s = s + 'GGG'

        # 有错误的部分
        elif(line == 'N w'):
            s = s + 'AAC'
        elif(line == 'E w'):
            s = s + 'GAA'
        #
        else:
            print("不一致的："+ line+"\n")
            err.append(line)
            c = c + 1
        
    

print(err)        

print(c)  
print(count1)

print('ok')
