#Class that i used to save the operators of one equation and the location of each one
class teste:
    def __init__(self, operator, location):
        self.operator = operator
        self.location = location
        
#Just some examples to test, each side of the equation will give me the numbers and the operations, and it will be
#saved in this lists bellow for my program calculate the result.
#OBS:[The way that i will get this numbers and operators is unknown, but i will try to develope one GUI to get them]

operators_left = [7, 7, 5, 5, 7, 4, 2] # 7 = Plus, 6 = Minus, 5 = Multiply, 4 = Division, 3 = Exponetation, 2 = Square Root
numbers_left = [2, 3, 4, 2, 4, 2, 4, 2]
#The equation above is :2+3+4*2*4+2/(4**1/2): the final is a square root

operators_right = [6] # 7 = Plus, 6 = Minus, 5 = Multiply, 4 = Division, 3 = Exponetation, 2 = Square Root
numbers_right = [7, 2] 
#The equation above is :7-2:




#Function that will creat one object to one operator in the equation
def creat_operator_object(operators):
    operator_list = []
    for i in range(0, len(operators)):
        obj = teste(operators[i], i)
        operator_list.append(obj)
    return operator_list


#The main function, that can calculate the numbers and operations, based on how important they are (Math orderd calculation)
def calculate(object_list, numbers):
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
                    n = numbers[object_list[i].location] + numbers[object_list[i].location+1]
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                #If it is a subtraction
                elif object_list[i].operator == 6:
                    n = numbers[object_list[i].location] - numbers[object_list[i].location+1]
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                #If it is a multiplication
                elif object_list[i].operator == 5:
                    n = numbers[object_list[i].location] * numbers[object_list[i].location+1]
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                #if it is a Division
                elif object_list[i].operator == 4:
                    n = numbers[object_list[i].location] / numbers[object_list[i].location+1]
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                #If it is a exponentiation
                elif object_list[i].operator == 3:
                    n = numbers[object_list[i].location] ** numbers[object_list[i].location+1]
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                #If it is a Square Root
                elif object_list[i].operator == 2:
                    n = numbers[object_list[i].location] ** (1/numbers[object_list[i].location+1])
                    numbers[object_list[i].location] = n
                    numbers.pop(object_list[i].location+1)
                    for part in object_list:
                        if part.location > object_list[i].location:
                            part.location -= 1
                object_list.pop(i)
                break
        
        #print(numbers, object_list)
        #Recursion to calculate all the operator and numbers until that dont left one operation in the list
        return calculate(object_list, numbers)
    else:
        #When the recursion end the program will return one list that contain the answer after all the operations
        return numbers, object_list

#Just one test about the equation that i created above in the code, this is not capable to calculate one equation
#With X but it will be resolved when i decided how i will get the equation and the numbers and operations in theis own list
operators_L = creat_operator_object(operators_left)
operators_R = creat_operator_object(operators_right)
c, d = calculate(operators_L, numbers_left)
e, f = calculate(operators_R, numbers_right)
print("test", c, d)
print("test", e, f)


