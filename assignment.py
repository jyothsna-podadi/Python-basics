#1. write a program that asks the user for their name and age, then prints a sentence 

# name=input()
# age=input()

# print("Hello "+ name+", you are " + age+" years old!")


#2. Take two numbers as input from the user and print their sum, difference, product, and quotient.

# num1=int(input())
# num2=int(input())

# sum=num1+num2
# difference=num1-num2
# product=num1*num2
# quotient=num1/num2

# print(sum,difference,product,quotient)


#3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# num1=int(input())
# num2=int(input())
# num3=float(input())

# sum=float(num1)+float(num2)+num3
# average=sum/3

# print(average)


#4. The user enters a string containing a number (e.g. "45"). convert it to:
#   i. an integer
#   ii. a float
#   iii. a string
#print all three values with their types.


# num=input()

# #integer 
# num=int(num)
# print(num,type(num))

# #float
# num=float(num)
# print(num,type(num))

# #string
# num=str(num)
# print(num,type(num))


#5. Evaluate and print the result of the following expression:
#       x=10+3*2**2

# x=10+3*2**2 #(it follows the 'PEMDAS' rule, exponential--->multiplication--->addition--->assign)
# print(x)


#6. Write a program to swap values of two numbers entered by the user.

# num1=int(input())
# num2=int(input())

# num1,num2=num2,num1 #swapping numbers
# print(num1,num2)


#7. ask the user for a temperatue in celcius (string input). convert it to float, then calculate and print temperature in fahrenheit.
# conversion formula: FahrenheitTemp=(celciusTemp*(9/5))+32

# celciusTemp=input()

# celciusTemp=float(celciusTemp)

# FahrenheitTemp=(celciusTemp*(9/5))+32
# print(FahrenheitTemp)


#8. Take the radius (r) as user input and print the area.

# r=int(input())
# pie=3.14

# area=pie*r**2
# print(area)


#9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest

# P=input()
# R=input()
# T=input()

# simple_interest=(float(P)*float(R)*float(T))/100

# print(simple_interest)


#10. Take a decimal number as a input (like 45.78) and output is:
#       integer part-45
#       fractional part= .78

num=float(input())

integer=num//1
print(int(integer))

fraction=(num%1)*100
print(int(fraction))