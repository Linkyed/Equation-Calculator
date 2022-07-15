equation = 'sq2*3+2'

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
    #Clear a space if the equation starts with '-'
    if numbers_list[0] == '':
        numbers_list = numbers_list[1: len(numbers_list)]
    #Get the operador of each number
    for char in equation:
        if char.isnumeric() == False:
            operators_list.append(char)
    
    number_list_size = len(numbers_list)

    #Star to save the numbers and them operators in a list of objects
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
        


#Function that use the list of objectos with operators and numbers to calculate the result
def calculate(number_operators, size):
    sum = 0
    for i in range(0, size):
        sum += int(number_operators[i].operator + number_operators[i].number)
    return sum


#Test
#for i in range(0, n):
 #   print(list[i].operator, list[i].number)
