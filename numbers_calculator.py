import os

#Class that i used to save the operators of one equation and the location of each one
class teste:
    def __init__(self, operator, location):
        self.operator = operator
        self.location = location
        
#Just some examples to test, each side of the equation will give me the numbers and the operations, and it will be
#saved in this lists bellow for my program calculate the result.
#OBS:[The way that i will get this numbers and operators is unknown, but i will try to develope one GUI to get them]

operators_left = [7, 7, 5, 5, 7, 4, 2] # 7 = Plus, 6 = Minus, 5 = Multiply, 4 = Division, 3 = Exponetation, 2 = Square Root
numbers_left = [2, 3, 4, 2, 4, 2, 2, 4]
#The equation above is :2+3+4*2*4+2/(4**1/2): the final is a square root

operators_right = [6] # 7 = Plus, 6 = Minus, 5 = Multiply, 4 = Division, 3 = Exponetation, 2 = Square Root
numbers_right = [7, 2] 
#The equation above is :7-2:

path = r'C:\Users\gustavo\Desktop\Equation Calculator'
txt = 'equation_solution.txt'

#Function to write/create a txt with a text that i want
def write_txt(txt_name, text):
    if os.path.isfile(path+"\ ".replace(' ', '')+txt_name):
        with open(txt_name, 'a', encoding="utf-8") as file:
            file.write(text)
    else:
        with open(txt_name, 'w', encoding="utf-8") as file:
            file.write(text)

#Function to create a visual(string) equation with the numbers and operators
def visualizer_equation(numbers, operators):
    equation = ''
    for i in range(0, len(numbers)):
        equation = equation+str(numbers[i])
        if i < len(operators):
            if operators[i] == 7:
                equation = equation+'+'
            elif operators[i] == 6:
                equation = equation+'-'
            elif operators[i] == 5:
                equation = equation+'*'
            elif operators[i] == 4:
                equation = equation+'/'
            elif operators[i] == 3:
                equation = equation+'^'
            elif operators[i] == 2:
                equation = equation+'√'
    if equation[len(equation)-1].isnumeric() == False:
        equation = equation[0:len(equation)-1]
    return equation


#Function that will creat one object to one operator in the equation
def creat_operator_object(operators):
    operator_list = []
    for i in range(0, len(operators)):
        obj = teste(operators[i], i)
        operator_list.append(obj)
    return operator_list


#The main function, that can calculate the numbers and operations, based on how important they are (Math orderd calculation)
def calculate(object_list, numbers, operators):
    #When the list of object has one os more operators, it will calculate base on your orders and the numbers that it is involved
    if len(object_list) > 0:
        lowest = object_list[0].operator
        for iten in object_list:
            if iten.operator < lowest:
                lowest = iten.operator
        #Loop to start calculating
        for i in range(0, len(object_list)):
            #Conditional that only allow the calcution of the priority operator
            if object_list[i].operator == lowest:
                #If it is a addition
                if object_list[i].operator == 7:
                    write_txt(txt, 'Equation: '+visualizer_equation(numbers, operators))
                    n = numbers[object_list[i].location] + numbers[object_list[i].location+1]
                    
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                    
                    write_txt(txt, "\nNow you solve the addition of {}+{}\n\n".format(numbers[object_list[i].location], numbers[object_list[i].location+1]))
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                #If it is a subtraction
                elif object_list[i].operator == 6:
                    write_txt(txt, 'Equation: '+visualizer_equation(numbers, operators))
                    n = numbers[object_list[i].location] - numbers[object_list[i].location+1]
                    write_txt(txt, "\nNow you solve the subtraction of {}-{}\n\n".format(numbers[object_list[i].location], numbers[object_list[i].location+1]))
                    
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                    
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                #If it is a multiplication
                elif object_list[i].operator == 5:
                    write_txt(txt, 'Equation: '+visualizer_equation(numbers, operators))
                    n = numbers[object_list[i].location] * numbers[object_list[i].location+1]
                   
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                    
                    write_txt(txt, "\nNow you solve the Multiplication of {}*{}\n\n".format(numbers[object_list[i].location], numbers[object_list[i].location+1]))
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                #if it is a Division
                elif object_list[i].operator == 4:
                    write_txt(txt, 'Equation: '+visualizer_equation(numbers, operators))
                    n = numbers[object_list[i].location] / numbers[object_list[i].location+1]
                    
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                    
                    write_txt(txt, "\nNow you solve the Division of {}/{}\n\n".format(numbers[object_list[i].location], numbers[object_list[i].location+1]))
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                  
                #If it is a exponentiation
                elif object_list[i].operator == 3:
                    write_txt(txt, 'Equation: '+visualizer_equation(numbers, operators))
                    n = numbers[object_list[i].location] ** numbers[object_list[i].location+1]
                    
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                    
                    write_txt(txt, "\nNow you solve the Exponentiation of {}**{}\n\n".format(numbers[object_list[i].location], numbers[object_list[i].location+1]))
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    
                #If it is a Square Root
                elif object_list[i].operator == 2:
                    write_txt(txt, 'Equation: '+visualizer_equation(numbers, operators))
                    n = numbers[object_list[i].location+1] ** (1/numbers[object_list[i].location])
                    
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                    
                    write_txt(txt, "\nNow you solve the Square Root of {}√{}\n\n".format(numbers[object_list[i].location], numbers[object_list[i].location+1]))
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    
                object_list.pop(i)
                break
        
        #print(numbers, object_list)
        #Recursion to calculate all the operator and numbers until that dont left one operation in the list
        return calculate(object_list, numbers, operators)
    else:
        #When the recursion end the program will return one number that is the result after all the operations
        write_txt(txt, "Then after all operation you have the number : {} : as a result\n\n".format(numbers[0]))
        return numbers[0]

#Just one test about the equation that i created above in the code, this is not capable to calculate one equation
#With X but it will be resolved when i decided how i will get the equation and the numbers and operations in theis own list
operators_L = creat_operator_object(operators_left)
operators_R = creat_operator_object(operators_right)
write_txt(txt, "Solving the Left Side:\n\n")
left_result= calculate(operators_L, numbers_left, operators_left)
write_txt(txt, "\nSolving the Right Side:\n\n")
right_result = calculate(operators_R, numbers_right, operators_right)

#Geting the result numbers together in one list and finishing the last math count
final_numbers = [right_result, left_result]
if left_result >= 0:
    final_operations = [6]
else:
    final_operations = [7]
final_object = creat_operator_object(final_operations)
write_txt(txt, "\n\nNow, to finish the work: \n\n")
result = calculate(final_object,final_numbers,final_operations)


