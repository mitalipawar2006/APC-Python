n=int(input("enter a no:"))
for i in range(1,n+1):
    sqr_root=i**1/2
    if sqr_root%1==0 and sqr_root%sqr_root==0:
        print("number is prime")
       