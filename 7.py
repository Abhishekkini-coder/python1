f1 = open("in2.txt","r")
line1 = f1.readline()
arr1 = line1.split(",")
start = int(arr1[0])
stop = int(arr1[1])
for j in range(start,stop+1,1): 
    for i in range(1,11,1):
        print(j,"*",i,"=",j*i)
    print()

