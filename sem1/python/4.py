a=int(input("enter a integer:"))
if(a<10):
    n1=int("%s" %(a))
    n2=int("%s%s" %(a,a))
    n3=int("%s%s%s" %(a,a,a))
print("sum:",n1+n2+n3)
