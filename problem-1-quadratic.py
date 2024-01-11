import math

#inputs
a = int(input("what is a?"))
b = int(input("what is b?"))
c = int(input("what is c?"))


#check roots then sort
imaginary = b**2-(4*a*c)


if imaginary > 0:
    root_1 = (-b + math.sqrt(imaginary))/ (2*a)
    root_2 = (-b - math.sqrt(imaginary))/ (2*a)

    print('the roots are ', root_1 , "and" , root_2)
elif imaginary == 0:
    root_1 = ((-b)/(2*a))

    print('the only root is', root_1)
else:
    print("the roots are imaginary")