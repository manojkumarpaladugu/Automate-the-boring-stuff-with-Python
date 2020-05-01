# except zero division error
def divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print('You tried to divide by zero')

print(divide(42,2))
print(divide(42,12))
print(divide(42,0))
print(divide(42,1))
