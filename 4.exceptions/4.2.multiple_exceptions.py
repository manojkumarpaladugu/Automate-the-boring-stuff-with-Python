# except zero division error
def divide():
    print('Enter dividend')
    dividend = input()
    print('Enter divisor')
    divisor = input()
    
    try:
        dividend = int(dividend)
        divisor = int(divisor)
        return dividend / divisor
    except ValueError:
        print('You didn\'t provide number')
    except ZeroDivisionError:
        print('You tried to divide by zero')
    except: # handles all other errors
        print('Unknown error')

print(divide())
