import mathematics

x=mathematics.multiply(6,4)
print(x)

y=mathematics.divide(12,4)
print(y)
import operators
import others
import trig
x=others.cube(9)
# get numbers
num1=eval(input("enter number 1:"))
num2=eval(input("enter number2:"))
operator=input("enter operator:")
if operator =="+":
   x= operators.add(num1,num2)
   print(x)
elif operator=="-":
    x=operators.subtract(num1,num2)
    print(x)
elif operator=="*"or"x"or"X":
    x=operators.multiply(num1,num2)
if operator=="cube":
    num=eval(input("enter number:"))
    x=others.cube(num)
    print(x)

elif operator=="sin":
    angle=eval(input("enter angle in degrees:"))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle)
elif operator=="tan":
    angle=eval(input("enter angle in degrees:"))
    print(trig.get_tan(angle))

    
    
