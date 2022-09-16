#Write a python script to print first N even natural numbers in reverse order
n=int(input("enter number of times you want to print even natural number in reverse: "))
i=n*2
while i>0:
    print(i,end=' ')
    i-=2
