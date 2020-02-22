mc=[]
def longest_words(dokimi):
    with open(dokimi, 'r') as infile:
        words = infile.read().split()
    global mc
    p = 0
    mx=[]
    mxl=[]
    mcl=[]
    while(p<5):
        s=-1
        ml=len(max(words, key=len))
        for x in words:
            s+=1
            if(len(x) == ml):
                p+=1
                mx.append(words.pop(s))
                mxl.append(len(x))
    for i in range(5):
        mc.append(mx[i])
        mcl.append(len(x))
    print(mc)
    return[]
    

print(longest_words('dokimi.txt'))
for i in range(5):
    if mc[i] == 'x':
        exit();
    else:
        newstr = mc[i];
        vowels = ('a', 'e', 'i', 'o', 'u', 'α', 'ε', 'η', 'ι', 'ο', 'υ', 'ω');
        for x in mc[i].lower():
            if x in vowels:
                newstr = newstr.replace(x,"");
        print(newstr[::-1]);








































