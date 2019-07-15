s11,s22=input().split()
C3=0
for i in range(0,len(s11)):
    for j in range(0,i+1):
        if s11[i]!=s22[j]:
            C3+=1
            break
if C3==1:
    print("yes")
else:
    print("no")
