def addition(a, b):
    return a + b

#main prog
def main():
    num1 = float(input('Enter your 1st Number:\n'))
    num2 = float(input('Enter your 2nd Number\n'))

    #call function
    result = addition(num1, num2)
    print('The result is', result)

main()