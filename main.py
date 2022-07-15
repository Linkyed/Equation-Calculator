from Basic_Equation_Calculator import calculate, get_values

#Começar a colocar o delay nas coisas
from time import sleep

#equation = "23-22=-33+x"
equation = '33-x+11=1+2'
# Plus = +
# Minus = -
# Multipla' = *
# Division = /
# Exponetation = ^   
# Square Root = %

#Function to separate the X of the equation
def get_X(equation):
    position = equation.find('x')
    equation_size = len(equation)
    equal_position = equation.find('=')
    before_equal = False
    if equal_position > position:
        before_equal = True

    #If the equation has a X then the fuction will do their work
    if position != -1:
        next_operator_position = 0
        previous_operator_position = 0
        #Start to check the next chars in the equation to find a '+' or '-' or '=' or the end
        if position+1 < equation_size-1:
            for i in range(position+1, equation_size):
                if equation[i] == '-' or equation[i] == '+' or equation[i] == '=':
                    next_operator_position = i
                    break
            if next_operator_position <= position:
                next_operator_position = equation_size
        else:
            next_operator_position = equation_size
        #Start to check the previvous chars in the equation to find a '+' or '-' or '=' or the end
        if position-1 > 0:
            for i in range(position-1, 0, -1):
                if equation[i] == '-' or equation[i] == '+' or equation[i] == '=':
                    if equation[i] == '=':
                        previous_operator_position = i+1
                    else:
                        previous_operator_position = i
                    break
        return  before_equal, equation[previous_operator_position: next_operator_position]
    else:
        return 0

#Function to split the equation in two parts
def equation_split(equation, x):
    new_equation = equation.replace(x, '')
    new_equation = new_equation.split('=')
   
    equation_Left = new_equation[0]
    equation_Right = new_equation[1]
    return equation_Left, equation_Right

#Function to check the order to solve the equation
def case_level(equation):
    has_parenthesis = False
    has_Squareroot = False
    has_exponentiation = False
    has_Multiply = False
    has_Division = False
    case_lv = 0

    if equation.find('(') != -1:
        has_parenthesis = True
        if case_lv == 0:
            case_lv = 3
    elif equation.find('sq') != -1:
        has_Squareroot = True
        if case_lv == 0:
            case_lv = 2
    elif equation.find('^') != -1:
        has_exponentiation = True
        if case_lv == 0:
            case_lv = 2
    elif equation.find('*') != -1:
        has_Multiply = True
        if case_lv == 0:
            case_lv = 1
    elif equation.find('/') != -1:
        has_Division = True
        if case_lv == 0:
            case_lv = 1
    return has_parenthesis, has_exponentiation, has_Squareroot, has_Multiply, has_Division

#Function to solve the equation math based in the operations
def solve_equation(has_parenthesis, has_exponentiation, has_Squareroot, has_Multiply, has_Division, equation, x=''):
    did_nothing = False
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
        values, size = get_values(equation)
        if len(values) > 1:
            print("Start solving the math counts:")
            if x != '':
                if x.find('+') != -1:
                    x = x.replace('+', '')
                if equation[0] != '-' and equation[0] != '+':
                    equation = '+'+equation
                print(x+equation)
                final_result = calculate(values, size)
                if final_result>=0:
                    print(x+"+"+str(final_result))
                else:
                    print(x+str(final_result))

            else:
                print(equation)
                final_result = calculate(values, size)
                print(final_result)
            print("\nThen now the equation looks like this: ")
            return did_nothing, final_result
        elif len(values) == 1:
            did_nothing = True
            return did_nothing, str(values[0].operator+values[0].number)

#Geting the position of X (If it is before or after the '=') and the X variable
x_position, x = get_X(equation)
#Spliting the equation in left part and right part
equation_Left, equation_Right = equation_split(equation, x)

#Geting the order to solve the equation left and right
has_parenthesis_Right, has_exponentiation_Right, has_Squareroot_Right, has_Multiply_Right, has_Division_Right = case_level(equation_Right)
has_parenthesis_Left, has_exponentiation_Left, has_Squareroot_Left, has_Multiply_Left, has_Division_Left = case_level(equation_Left)

print("Solving this equation: \n{}\n".format(equation))

#Star to solve the equations based where the X stay, starting with X before the '='
if x_position == True:
    
    #Start to solve the left part of the equation, who has the X variable
    print("Left Part:")
    
    #If X is not alone in the equation
    if equation_Left != '':
        did_nothing, solution_Left = solve_equation(has_parenthesis_Left, has_exponentiation_Left, has_Squareroot_Left, has_Multiply_Left, has_Division_Left, equation_Left, x)
        #If the program had to solve math counts
        if did_nothing == False:
            
            if solution_Left >= 0:

                print('\n'+x.replace('+', '')+'+'+str(solution_Left)+'='+equation_Right)
            else:
                print('\n'+x.replace('+', '')+str(solution_Left)+'='+equation_Right)

        else:
            
            print("There is no math to do in this part")
    
    else:
        
        print("There is no math to do in this part")
        solution_Left = x
    
    #Start to solve the right part of the equation
    print("\nRight Part:")
    did_nothing, solution_Right = solve_equation(has_parenthesis_Right, has_exponentiation_Right, has_Squareroot_Right, has_Multiply_Right, has_Division_Right, equation_Right)
    
    #Cheking if the program had to do any count in the left part
    if type(solution_Left) == int:
        
        #If the program had to solve math counts
        if did_nothing == False:
            #Printing and saving the equation based in the value of the left equation
            if solution_Left >= 0:  
                print('\n'+x.replace('+', '')+'+'+str(solution_Left)+'='+str(solution_Right))
                final_equation_str = x.replace('+', '')+'+'+str(solution_Left)+'='+str(solution_Right)
            
            else:
                print('\n'+x.replace('+', '')+str(solution_Left)+'='+str(solution_Right))
                final_equation_str = x.replace('+', '')+str(solution_Left)+'='+str(solution_Right)
        
        else:
            if solution_Left >= 0:
                final_equation_str = x.replace('+', '')+'+'+str(solution_Left)+'='+str(solution_Right)
            
            else:
                final_equation_str = x.replace('+', '')+str(solution_Left)+'='+str(solution_Right)
            print("There is no math to do in this part")
    
    else:
        
        #Printing and saving the equation based if the X in left equation had a number with it or not
        if solution_Left == x:
            print('\n'+solution_Left.replace('+', '') +'='+str(solution_Right))
            final_equation_str = solution_Left.replace('+', '') +'='+str(solution_Right)
        
        else:
            print('\n'+x.replace('+', '')+solution_Left +'='+str(solution_Right))
            final_equation_str = x.replace('+', '')+solution_Left +'='+str(solution_Right)

#Solving the equation if the X is after the '='
else:
    #Start solving the Left part
    print("Left Part:")
    did_nothing, solution_Left = solve_equation(has_parenthesis_Left, has_exponentiation_Left, has_Squareroot_Left, has_Multiply_Left, has_Division_Left, equation_Left)
    
    #If the program had to solve math counts
    if did_nothing == False:
        
        if equation_Right.isnumeric() == False:
            print('\n'+str(solution_Left)+'='+x.replace('+', '')+equation_Right)
        else:
            print('\n'+str(solution_Left)+'='+x.replace('+', '')+'+'+equation_Right)
    
    else:
        
        print("There is no math to do in this part")
        solution_Left = solution_Left.replace('+', '')
    
    #Start solving the Right part where the X stay
    print("\nRight Part:")
    
    #If X is not alone in the equation
    if equation_Right != '':
        
        did_nothing, solution_Right = solve_equation(has_parenthesis_Right, has_exponentiation_Right, has_Squareroot_Right, has_Multiply_Right, has_Division_Right, equation_Right, x)
        
        #If the program had to solve math counts
        if did_nothing == False:

            #Printing and saving the equation based in the value of the left equation
            if solution_Right >= 0:
                
                print('\n'+str(solution_Left)+'='+x.replace('+', '')+'+'+str(solution_Right))
                final_equation_str = str(solution_Left)+'='+x.replace('+', '')+'+'+str(solution_Right)
            
            else:

                print('\n'+str(solution_Left)+'='+x.replace('+', '')+str(solution_Right))
                final_equation_str = str(solution_Left)+'='+x.replace('+', '')+str(solution_Right)
        
        else:
            
            final_equation_str = str(solution_Left)+'='+x.replace('+', '')+str(solution_Right)
            print("There is no math to do in this part")
    
    else:
        
        print("There is no math to do in this part")
        final_equation_str = str(solution_Left)+'='+x.replace('+', '')

print("\nNow solving this equation: \n{}".format(final_equation_str))

#print(solution_Right -(solution_Left))

#Teste
#for i in range(0, left_size):
#    print(values_Left[i].operator, values_Left[i].number)
#for i in range(0, right_size):
#    print(values_Right[i].operator, values_Right[i].number)
