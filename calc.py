def welcome():
    print('''
Calculator 1.5.1
''')


...
welcome()


def calculate():
    operation = input('''
Enter math operation:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
%  for modulo
''')
    try:
        number_1 = int(input('Enter the first number: '))
        number_2 = int(input('Enter the second number: '))
        invalid = False
    except ValueError:
        print("Invalid operand")
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

        else:
            print('Invalid operator')

    again()


def again():
    calc_again = input('''
Calculate again? Y/N
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Exiting...')
    else:
        again()


calculate()