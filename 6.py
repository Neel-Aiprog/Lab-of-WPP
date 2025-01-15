num1=int(input("pls enter the number you want to reverse\t"))
sum=0
sumd=0
num2=num1
while(num2!=0):
    q=int(num2%10)
    sumd+=1
    num2=int(num2/10)
while(num1!=0):
    q=int(num1%10)
    sumd-=1
    sum=sum+q*(10**sumd)
    num1=int(num1/10)
print(sum)