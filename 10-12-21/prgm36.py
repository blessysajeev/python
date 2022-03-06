a=['apple','orange','watermelon','watermelon']
def list(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if(len(i)>max1):
            max1=len(i)
            temp=i
    print("longest word is ",temp ,"length is",max1)
list(a)