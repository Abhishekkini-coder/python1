f1 = open("in1.txt","r")

start = int(f1.readline())
stop = int(f1.readline())
for j in range(start,stop+1,1): 
    for i in range(1,11,1):
        print(j,"*",i,"=",j*i)
    print()

