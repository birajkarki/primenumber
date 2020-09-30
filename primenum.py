#Prints all prime number which is given by user
num1 =int(input("Enter your beginning number \n"))
num2 =int(input("Enter your ending number \n"))

print(f"Your prime numbers from {num1} to {num2} is:")
 # note that in for num in range(num1 appears but num2 doesnot so num2+1 while giving end number)
for num in range (num1,num2):
    for i in range(2, num):
        if num %i ==0:
            break
    else:
        print(num)    
 
