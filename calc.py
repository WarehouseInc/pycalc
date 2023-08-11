import numpy
from numpy import emath
def welcome():
    print("Calculator 2.0")

def calculate():
    operation = input('''
Enter math operation:
'+' for addition
'-' for subtraction
'*' for multiplication
'/' for division
'**' for power
'%'  for modulo
'sqrt' for square root (CASE SENSITIVE!)
'cbrt' for cube root (again, case sensitive.)
''')
    while True:
            try: 
                if operation == 'sqrt':
                   try:
                       num0 = input('Operand: ')
                       num = float(num0)
                   except ValueError:
                       print('Invalid operand. Abort.')
                   else:
                       break
                if operation == 'cbrt':
                   try:
                       num0 = input('Operand:')
                       num = float(num0)
                   except ValueError:
                        print('Invalid operand. Abort.')
                   else:
                        break
                else:
                    try:
                        num1 = input('Operand 1:')
                        num2 = input('Operand 2:')
                        number_1 = float(num1)
                        number_2 = float(num2)
                    except ValueError:
                        print("Invalid operand(s). Abort.")
                    else:
                        break
            except ValueError:
                print("Invalid operation. Abort.")
                exit()
            else:
                break
    if operation == '+':
            try:
                print('{} + {} = '.format(number_1, number_2))
                print(number_1 + number_2)
            except UnboundLocalError:
                exit()

    elif operation == '-':
            try:
                print('{} - {} = '.format(number_1, number_2))
                print(number_1 - number_2)
            except UnboundLocalError:
                exit()

    elif operation == '*':
            try:
                print('{} * {} = '.format(number_1, number_2))
                print(number_1 * number_2)
            except UnboundLocalError:
                exit()

    elif operation == '/':
            try:
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            except UnboundLocalError:
                exit()
            except ZeroDivisionError:
                print("Indeterminate")
            
    elif operation == '**':
            try:
                print('{} ** {} = '.format(number_1, number_2))
                print(number_1 ** number_2)
            except UnboundLocalError:
                exit()

    elif operation == '%':
            try:
                print('{} % {} ='.format(number_1, number_2))
                print(number_1 % number_2)
            except UnboundLocalError:
                exit()
            except ZeroDivisionError:
                print("Indeterminate")
        
    elif operation == 'sqrt':
                num_sqrt = numpy.emath.sqrt(num)
                print(f'The square root of {num} is {num_sqrt}')
        
    elif operation == 'cbrt':    
                num_cbrt = numpy.cbrt(num)
                print(f'The cube root of {num} is {num_cbrt}')
            
    else:
            print('Invalid operator. Abort.')
    again()

def again():
    n = input('''
    Calculate again? Y/N
    ''')
    if n.upper() == 'Y':
        calculate()
    elif n.upper() == 'N':
        print('Quitting...')
    else:
       return again()

def main():
    welcome()
    calculate()
    
main()