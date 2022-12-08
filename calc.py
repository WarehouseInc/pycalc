def welcome():
    print("Calculator 1.8")

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
    try:
        if operation == 'sqrt':
            number_1 = float(input('Operand: '))
            invalid = False
        if operation == 'cbrt':
            number_1 = float(input('Operand: '))
            invalid = False
        else:
            number_1 = int(input('Operand 1: '))
            number_2 = int(input('Operand 2: '))
            invalid = False
    except ValueError:
        print("Invalid operand! Quitting...")
        number_1 = 1
        number_2 = 1
        invalid = True

    if not invalid:
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)

        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)

        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

        elif operation == '/':
            try:
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            except:
                print("Indeterminate")

        elif operation == '**':
            print('{} ** {} = '.format(number_1, number_2))
            print(number_1 ** number_2)

        elif operation == '%':
            try:
                print('{} % {} ='.format(number_1, number_2))
                print(number_1 % number_2)
            except:
                print("Indeterminate")
        
        elif operation == 'sqrt':
            try:
                number_1_sqrt = number_1 ** 0.5
                print('The square root of %0.9f is %0.9f'%(number_1 ,number_1_sqrt))
            except:
               print("Indeterminate-only non-negative numbers allowed")
        
        elif operation == 'cbrt':
            try:    
                number_1_cbrt = number_1 ** (1./3.)
                print('The cube root of %0.9f is %0.9f'%(number_1 ,number_1_cbrt))
            except:
                number_1 = abs(number_1)
                number_1_cbrt = number_1 ** (1./3.) * -1
                print('The cube root of -%0.9f is %0.9f'%(number_1 ,number_1_cbrt))      
        else:
            print('Invalid operator')
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