import string
import sys
size=int(input("Enter the pattern length(<=26):"))
pattern=[]
if(size==1):
    print("a")
    sys.exit()
else:
    if(size<=26):
        str_list=list(string.ascii_lowercase)
        pattern.append(str_list[size-1].center(4*size-3,"-"))
        for i in range(size-3,-2,-1):
            k=str_list[size-1:i:-1]
            if(i==-1):
                k=str_list[size-1::-1]
            for j in range(1,2*(size-1-i)-1,2):
                k.insert(j,"-")
            k.extend(k[2*(size-i-1)-3::-1])
            k=''.join(k)
            pattern.append(k.center(4*size-3,"-"))
        pattern.extend(pattern[len(pattern)-2::-1])
        for m in range(len(pattern)):
            print(pattern[m])
    else:
        print("input error")
