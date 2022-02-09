'''Пользователь водит свое имя. Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.'''

name = input('Enter your name')
upper = name.upper()
lower = name.lower()
output = '{} {}'.format(upper, lower)
print(output)