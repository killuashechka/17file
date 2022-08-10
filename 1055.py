k=0
for i in range(0,10000):
    ch=i
    for j in range(50):
        ch=ch+int(str(ch)[::-1])
        if ch==int(str(ch)[::-1]):
            k+=1
            break
print(10000-k)
