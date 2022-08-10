f=open("0910.txt")
s=f.readline()
h=0
m=0
res=0
for i in range(len(s)):
    if s[i:i+5]=="heavy":
        h+=1
    if s[i:i+5]=="metal" and h>0:
        m+=1
        res+=h
print(res)