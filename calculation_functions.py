from general_functions import show_full_equation, show_part_equation
from time import sleep
#Creating a object to save operator and numbers of a equation
class equation_values:
    def __init__(self, operator, number):
        self.operator = operator
        self.number = number

#Function to read a equation and get the numbers and operators
def get_values(equation):
    numbers_list = []
    operators_list = []
    object_list = []

    #Creat a second equation with only numbers and creat a list with these numbers
    aux_equation = equation.replace('+', ' ')
    aux_equation = aux_equation.replace('-', ' ')
    numbers_list = aux_equation.split(' ')
    #Clear a space if the equation starts with '-' or '+'
    if numbers_list[0] == '':
        numbers_list = numbers_list[1: len(numbers_list)]
    #Get the operador of each number
    for char in equation:
        if char.isnumeric() == False:
            operators_list.append(char)
    
    number_list_size = len(numbers_list)

    #Star to save the numbers and their operators in a list of objects
    if number_list_size > len(operators_list):
        for i in range(0, number_list_size):
            if i == 0:
                object_list.append(equation_values('+', numbers_list[i]))
            else:
                object_list.append(equation_values(operators_list[i-1], numbers_list[i]))
    else:
        for i in range(0, number_list_size):
            object_list.append(equation_values(operators_list[i], numbers_list[i]))
        
    return object_list, number_list_size
        


#Function that use the list of objectos with operators(only '+' and '-') and numbers to calculate the result
def basic_calculate(number_operators, size):
    sum = 0
    for i in range(0, size):
        sum += int(number_operators[i].operator + number_operators[i].number)
    return sum


#Function to solve the equation math based in the operations
def solve_part_equation(has_parenthesis, has_exponentiation, has_Squareroot, has_Multiply, has_Division, equation, x=''):
    #Start solving the equation based in the math order
    if has_parenthesis == True:
        a = 0
    elif has_exponentiation == True:
        a = 0
    elif has_Squareroot == True:
        a = 0
    elif has_Multiply == True:
        a = 0
    elif has_Division == True:
        a = 0
    else:
        if equation == '':
            print("In this part you dont need to do any math counts")
            return ''
        
        values, size = get_values(equation)
        if len(values) > 1:
            print("Start solving the math counts:")
            
            show_part_equation(equation, x)
            sleep(1.5)
            final_result = basic_calculate(values, size)
            show_part_equation(final_result, x)
            sleep(1.5)
            return final_result
        
        elif len(values) == 1:
            print("In this part you dont need to do any math counts")
            return int(values[0].operator+values[0].number)

#Function to solve the final part of a equation, where you have onlu one numver in both sides
def solve_full_equation(equation_L, equation_R, x):
    values_L = []
    values_R = []
    
    if equation_L != '':
        values_L, size_L = get_values(equation_L)
        if values_L[0].operator == '-':
            values_L[0].operator = '+'
        elif values_L[0].operator == '+':
            values_L[0].operator = '-'

    print('\nFirst you need to pass the number in the left part to the right part with opositive operator')
    show_full_equation(' ', equation_R+values_L[0].operator+values_L[0].number, x, 'L')
    sleep(1.5)
    values_R, size_R = get_values(equation_R)
    values_R.append(values_L[0])

    print("\nThen just resolve the math count")

    final_result = basic_calculate(values_R, 2)
    return final_result

