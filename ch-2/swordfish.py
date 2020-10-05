while True:
    print('Enter name')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is your password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('access granted!')