#The below python code calculates and present the square roots of the numbers in this list data type; [4, 16, 25, 36, 49, 81, 121, 225, 269] also by using a list data type
#The below line creates a list data type for the numbers and setting a variable for it
numbers = [4, 16, 25, 36, 49, 81, 121, 225, 269]
square_roots = []
for num in numbers:
    # This below line calculates the square root and append it to the square roots list
    square_roots.append(int(pow(num, 0.5)))
print("The square roots of {} are {}".format(numbers, square_roots))


# The below python code calculates/finds the root of  quadratic equation and determines whether it is a complex root or not
print("------Quadratic Equation Calculator----")
print("Format of the equation: ax{} + bx + c".format(chr(0x00B2)))
try:
    # The 3 line of codes below accepts the equation parameters from the user
    a = float(input("Enter your 'a' value from the equation: "))
    b = float(input("Enter your 'b' value from the equation: "))
    c = float(input("Enter your 'c' value from the equation: "))
except ValueError:
    print("Invalid input, try again!")
    exit()
if pow(b,2) > (4*a*c):
    # The 2 lines of codes calculates the two roots of the equation
    root_1 = ((-1*b) + pow((pow(b,2)-(4*a*c)), 0.5))/(2*a)
    root_2 = ((-1*b) - pow((pow(b,2)-(4*a*c)), 0.5))/(2*a)
    # The 2 lines of codes rounds up the two roots of the equation to 2 decimal places
    root_1 = round(root_1, 2)
    root_2 = round(root_2, 2)
    print("The roots of the quadratic equation are {} and {}".format(root_1, root_2))
else:
    root_1 = "({} + {}i)/{}".format((-1*b), round(pow(-1*(pow(b,2) - (4 * a* c)), 0.5),2), 2 * a)
    root_2 = "({} - {}i)/{}".format((-1 * b), round(pow(-1 * (pow(b, 2) - (4 * a * c)), 0.5),2), 2 * a)
    print("The quadratic equation has complex roots which are {} and {}".format(root_1, root_2))