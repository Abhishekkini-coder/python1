 start = int(input("Enter the start value"))
stop = int(input("Enter the stop value"))


for j in range(start,stop+1,1): 
    for i in range(1,11,1):
        print(j,"*",i,"=",j*i)
    print()

