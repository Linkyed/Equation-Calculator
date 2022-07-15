from general_functions import x_to_left, show_full_equation, equation_split, equation_treatment, show_part_equation, get_X, case_level
from calculation_functions import solve_part_equation, solve_full_equation
from time import sleep

equation = "13-x=-13"
#equation = 'x+33-22=1+2'
# Plus = +
# Minus = -
# Multiply = *
# Division = /
# Exponetation = ^   
# Square Root = sq


#Geting the position of X (If it is before or after the '=') and the X variable
x_position, x = get_X(equation)
#Use a copy of the equation without x to check the order of the math counts to do
equation_aux = equation.replace(x, '').split('=')
has_parenthesis_Right, has_exponentiation_Right, has_Squareroot_Right, has_Multiply_Right, has_Division_Right = case_level(equation_aux[1])
has_parenthesis_Left, has_exponentiation_Left, has_Squareroot_Left, has_Multiply_Left, has_Division_Left = case_level(equation_aux[0])

#Pass the x to the left side of equation
x, equation = x_to_left(equation, x, x_position)


#Spliting the equation in left part and right part
equation_Left, equation_Right = equation_split(equation, x)
if equation_Right == '':
    equation_Right = '0'


print("Solving this equation: \n{}\n".format(equation))

#This just solve simple equation onlyy with + and - and only one X
#Start solving the Left part where the X stay
print("Left Part:")
solution_Left = solve_part_equation(has_parenthesis_Left, has_exponentiation_Left, has_Squareroot_Left, has_Multiply_Left, has_Division_Left, equation_Left, x)
print("\nThen now the equation looks like this: ")
show_full_equation(solution_Left, equation_Right, x, 'l')
sleep(1.5)

#Start to solve the right part of the equation
print("\nRight Part:")
solution_Right = solve_part_equation(has_parenthesis_Right, has_exponentiation_Right, has_Squareroot_Right, has_Multiply_Right, has_Division_Right, equation_Right)
print("\nThen now the equation looks like this: ")
almost_final_equation = show_full_equation(solution_Left, solution_Right, x, 'l')
sleep(1.5)

#Checking if alfter all of this, we still have to do math counts
aux = almost_final_equation.split('=')
if aux[0].replace(x, '') == '':
    print("\nAnd then this is the solution for the equation")
#If we have to do the left math count then this start
else:
    print("\nNow solving this equation: \n{}".format(almost_final_equation))
    x_position, x = get_X(almost_final_equation)
    almost_final_equation_L, almost_final_equation_R = equation_split(almost_final_equation, x)
    final_result = solve_full_equation(almost_final_equation_L, almost_final_equation_R, x)
    show_full_equation(' ', final_result, x, 'l')
    
    #If in end the X is negative, then show what to do and give the awnser with positive X
    if x.find('-') != -1:
        sleep(1.5)
        print("\nNow to finish the work, just multiply both sides to get a positive X:")
        show_full_equation(' ', final_result, x, 'l')
        print("({})*-1".format(x))
        print("({})*-1".format(final_result))
        x = x.replace('-', '')
        final_result = final_result*-1
        sleep(1.5)
        print("\nThen the value of x to solve the solution is: ")
        show_full_equation(' ', final_result, x, 'l')
