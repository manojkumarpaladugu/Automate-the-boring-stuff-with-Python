def divide(dividend, divisor):
    try:
        if divisor == 0:
            raise Exception('Divide by zero error')
        return dividend / divisor
    except Exception as err:
        print(err)


print(divide(42,12))
print(divide(42,0))
        
