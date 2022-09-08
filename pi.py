def welcome():
    print('''
Calculator 1.7.1 - Addon to calculate the digits of Pi
''')

...
welcome()

def calcPi(limit):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    point = limit
    count = 0

    while count != point + 1:
        if 4 * q + r - t < n * t:

            yield n

            if count == 0:
                yield '.'

            if point == count:
                print('')
                break
            count += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

def main():

    pi_digits = calcPi(int(input(
        "Number of decimals: ")))
    i = 0
    for d in pi_digits:
        print(d, end='')
        i += 1
        if i == 40:
            print("")
            i = 0
    main()

if __name__ == '__main__':
    main()
