print('Привет, дорогой друг!\nРады приветствовать тебя на нашем сайте!')
user_name = input('Как вас зовут?\n')
if 'admin' in user_name:
    print('Привет, повелитель!')

user_gender = input('Укажите свой пол. "М" или "Ж"\n')
user_age = int(input('Сколько вам полных лет?\n'))

if user_name == 'Женя':
    recommend = str('Советую Вам посмотреть "TENET"')
    print(recommend)
else:
    if (10 <= user_age <= 14 and user_gender == 'М') or (user_age >= 30 and user_gender =='М'):
        recommend = str('"Советую Вам посмотреть "StarWars" или "Мандалорец"')
        print(recommend)
    elif 22 <= user_age <= 32 and user_gender == 'Ж':
        recommend = str('Советую Вам посмотреть "Трансформеры"')
        print(recommend)
    elif user_age >= 16 and user_gender == 'Ж':
        recommend = str('Советую Вам посмотреть "Инсургент"')
        print(recommend)
    elif user_age < 11 and user_gender == 'М':
        recommend = str('Советую Вам посмотреть "TMNT"')
        print(recommend)
if user_name == 'Guido':
        print('Огромное спасибо')

