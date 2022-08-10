import copy
N=int(input())
K=int(input())
left_K=str(K)[:N//2:]
right_K=str(K)[N//2::]
left_mas=[]
right_mas=[]
for i in range(N//2):
    left_mas.append(int(left_K[i]))
    right_mas.append(int(right_K[i]))
left_mas.sort()
right_mas.sort()
right_mas_2=copy.copy(right_mas)
k=0
L=0
for i in range(N//2):
    for j in range(N//2-1,-1,-1):
        if left_mas[i]>right_mas[j]:
            right_mas[j]=10
            k+=1
            break
for i in range(N//2-1,-1,-1):
    for j in range(N//2):
        if left_mas[i]<right_mas_2[j]:
            right_mas_2[j]=-1
            L+=1
            break
if k==N//2 or L==N//2:
    print("Число K волшебное")
else:
    print("Число K не волшебное")