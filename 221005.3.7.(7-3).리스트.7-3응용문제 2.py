#마지막 for문을 while문으로
aa=[]
for i in range(4):
    aa.append(0)

i=0
while(i<4):
    aa[i]=int(input(str(i+1)+"번째 숫자: "))
    i+=1
hap=0
hap=aa[0]+aa[1]+aa[2]+aa[3]

print("1~4입력받은 숫자의 합: %d"%hap)

