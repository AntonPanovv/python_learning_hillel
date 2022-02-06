import datetime
year_birth = input('Please, type your year of birth:\r\n')

if year_birth.isdigit() == False:
    year_birth = int(input('Please enter numeric value\r\n'))
else:
    year_birth = int(year_birth)
current_year = datetime.date.today().year
user_age = int(current_year - year_birth)

if user_age == 21:
   print('You should visit Holland.')
elif user_age > 21:
   print('You should visit Vietnam.')
else:
   print('Travell everywhere')