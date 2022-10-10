import re

def split(txt):
    if not txt:
        return txt
    l = len(txt)
    s = -1
    e = 0
    for i in range(l):
        if txt[i].isnumeric():
            if s == -1:
                s = i
            e = i
    return txt[s:e+1]



def split_number_in_text(txt):
    n = re.findall(r'\d+', txt)
    if len(n)> 0:
        f = txt.index(n[0])
        l = txt.index(n[len(n)-1]) if len(n)==1 else txt.index(n[len(n)-1], len(n[len(n)-1]))
        s = len(n[len(n)-1])
        mm = txt[f:l+s]
        return mm
    else: 
        return txt
# b = split_number_in_text(s1)
# print(b)

s1 = "aasvv"
print(split(s1))