def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    maxnum = num1

    if num2 > maxnum:
        maxnum = num2
    if num3 > maxnum:
        maxnum = num3
    
    print(f'The greates number is {maxnum}')
    ########################################
    # Do not delete the return statement
    ########################################
    return maxnum


if __name__ == '__main__':
    main()
