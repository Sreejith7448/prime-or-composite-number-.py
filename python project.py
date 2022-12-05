
'''To find out the status (prime and composite) of each number available in the given range.'''

num1=int(input("Enter Range--->1: "))
num2=int(input("Enter Range--->2: "))
print("Then the status of each number in the range is:")
count1=0
count2=0
for num in range(num1,num2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is composite or not prime")
                count1+=1
                break
        else:
            print(num,"is prime")
            count2+=1
print(count2,"prime and",count1,"composite numbers in the range.")















