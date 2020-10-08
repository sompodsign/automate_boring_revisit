def spam(divideBy):
    try:
        return 43/divideBy
    except ZeroDivisionError:
        print('Error: Invalid arguement')


print(spam(2))
print(spam(4))
spam(0)