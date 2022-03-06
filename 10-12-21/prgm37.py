def perfectsquare(l, r):
    for i in range(l, r+1):
        if(i**(.5)==int(i**(.5))) and (i%2==0):
            print(i, end="\n")
l = int(input("enter the 4 digit lower limit:"))
r = int(input("enter the 4 digit upper limit:"))
perfectsquare(l, r)