#Assignment - 4 Full Stack Web Development using Python MySirG User Input Problems
#1. Write a python script to take your name as input from the user and then print it.
a=input("your name")
print(a)
#2. Write a python script to take input from the user. Input must be a number.
a=int(input("input a number"))
print("The num is-",a)
#3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
a=int(input("input first number:"))
b=int(input("input second number:"))
print("Sum=",a+b)
#4. Write a python script which takes the radius from the user and display area of a circle.
a=float(input("input radius:"))
pi=3.141
area=pi*a**2
print("area of the circle is=",area)
#5. Write a python script to calculate the square of a number. Number is entered by the user.
a=int(input("enter a number"))
print("Square=",a**2)
#6. Write a python script to calculate the area of Triangle. Number is entered by the user.
a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter third side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle is", area)
#7. Write a python script to calculate average of three numbers, entered by the user
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
average=(a+b+c)/3
print("Average=",average)
#8. Write a python script to calculate simple interest
p=300
r=2
t=5
simple_interest=(p*r*t)/100
print("The Simple interest is=  ",simple_interest)
#9. Write a python script to calculate the volume of a cuboid.
lenth=float(input("Enter the lenth of cuboid:"))
width=float(input("Enter the width of cuboid:"))
height=float(input("Enter the height of cuboid:"))
volume=lenth*height*width
print("volume of the cuboid is=",volume)
#10. Write a python script to calculate area of a rectangl
lenth=float(input("Enter the lenth of rectangle:"))
breadth=float(input("Enter the breadth of rectangle:"))
area=lenth*breadth
print("Area of the rectangle is=", area)
