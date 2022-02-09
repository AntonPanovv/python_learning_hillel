'''Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.
Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white'''


list_of_cars = input('Enter car models from best to worst in your opinion separated with comma:\n').split()
unique_list_of_cars = list(set(list_of_cars))
sorted_cars = sorted(unique_list_of_cars)
string_with_cars = str(sorted_cars)
print(string_with_cars)
# meredes, volvo, volkswagen, audi, nissan, toyota, toyota, nissan, volvo, volkswagen, volvo, volkswagen, volvo, volkswagen,



