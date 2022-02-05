
user_name = (input('Please, enter your name:\n'))
user_age = int(input('Please, enter your age:\n'))
if 16 < user_age < 70:
    print('Welcome, ',user_name, ', on our website.' )
elif user_age == 16:
    print('Dear,', user_name, ', need to wait one year.')
elif 70 <= user_age <= 90:
    print('You are lucky', user_name, 'and welcome.')
elif user_age >= 121:
    print('You are not real,', user_name, '.')
else:
    print("I'm sorry,", user_name,', you are too young.')



