def calculator(number1, number2, operator):
    '''Checks if operator token given is valid, and operates on the numbers based on given argument'''
    opers = ['+', '-', '*', '/', '//', '**']
    if operator in opers: 
        if operator==opers[0]:
            return float(number1+number2)
        if operator==opers[1]:
            return float(number1-number2)
        if operator==opers[2]:
            return float(number1*number2)
        if operator==opers[3]:
            if number2==0:
                return False
            return float(number1/number2)
        if operator==opers[4]:
            if number2==0: 
                return False
            return float(number1//number2)
        if operator==opers[5]:
            return float(number1**number2)
    else: 
        print('Invalid Operation')

def parse_input():
    '''Asks for an input equation, and splits the equation into the 3 tokens for the calculator function'''
    inp = input("Enter equation: ")
    args = inp.split(" ")
    a=int(args[0])
    b=int(args[2])
    op = args[1]
    print(str(calculator(a, b, op)))

