password = int(input('Type your six numbers password: '))

def pass_verific():
    if password == 123456:
        print('Correct password.')
    else:
        print('Wrong password, try again!')
pass_verific()