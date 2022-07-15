from time import sleep

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

    if equation.find('(') != -1:
        has_parenthesis = True

    if equation.find('sq') != -1:
        has_Squareroot = True
    
    if equation.find('^') != -1:
        has_exponentiation = True
     
    if equation.find('*') != -1:
        has_Multiply = True
     
    if equation.find('/') != -1:
        has_Division = True
      
    return has_parenthesis, has_exponentiation, has_Squareroot, has_Multiply, has_Division

#Function to return a treated str(equation) to show in the screen
def equation_treatment(value, x_neighbor=False):
    if value != '':
        try:
            if value >= 0 and x_neighbor == True:
                return '+'+str(value)
            
            else:
                return str(value)
        
        except:
            if value[0] != ' ' and value[0] != '-' and value[0] != '+' and x_neighbor == True:
                value = "+"+value
            if value == ' ':
                value = value.replace(' ', '')
            return value
    else:
        return ''

#Function to show one part of the equation, even if it has an X or not
def show_part_equation(equation_1, x=''):
    x = x.replace('+', '')
    equation_1 = equation_treatment(equation_1, True)
    
    if x != '':
        print(x+equation_1)
        
    else:
        print(equation_1)

#Function to show the full equation in the screen
def show_full_equation(equation_L, equation_R, x, option = ''):
    
    if option.upper() == "L":
        L = equation_treatment(equation_L, True)
        R = equation_treatment(equation_R)
        print(x.replace('+', '')+L+'='+R)
        return (x.replace('+', '')+L+'='+R)

    elif option.upper() == 'R':
        L = equation_treatment(equation_L)
        R = equation_treatment(equation_R, True)
        print(L+'='+x.replace('+', '')+R)
        return (L+'='+x.replace('+', '')+R)

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

#Function to show and pass the X to the left side of the equation if it is in the right side
def x_to_left(equation, x, xposition):
    equation_l, equation_r = equation_split(equation, x)
    if equation_r == '':
        equation_r = '0'
    if xposition == False:
        print("To start solving the equation {}, first, let's move the X to the left side".format(equation))
        if equation_r != '':
            if equation_r[0] == '+':
                equation_r = equation_r[1:]
            if xposition == False:
                if x.find('-') != -1:
                    x = x.replace('-', '')
                elif x[0] == '+' or x.find('+') == -1:
                    x = "-"+x.replace("+", '')
        sleep(1)
        print("To do that, just pass the X with oposite operator, and if in the right side nothing left, just add a 0 on that side")
        sleep(1)
        print("Then the equation will looks like that: ")
        show_full_equation(equation_l, equation_r, x, 'l')
        sleep(2)
        print()
        return x, x+'+'+equation_l+"="+equation_r
    else:
        return x, equation