# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('Задание 1')
from collections import Counter
students_1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
student_list = {}
for student in students_1:
    student_list[student.get("first_name")] = students_1.count(student)

for student, key in student_list.items():
    print(f'{student}: {key}')
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

print('Задание 2')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

student_list2 = {}
for student in students:
    student_list2[student.get("first_name")] = students.count(student)

name =max((value, key) for key, value in student_list2.items())[1]
print(f'Самое частое имя среди учеников: {name}')
print()


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('Задание 3')
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for cnt, students in enumerate(school_students, 1):
    student_dict = {} # определяем словарь для строки с одним студентом для анализа в цикле ниже
    for student in students:
        name = [] # максимально повторяющееся имя студента\ов
        student_dict[student.get("first_name")] = students.count(student)

        # определяем сколько раз повторяется самое частое имя
        max_num = max((value, key) for key, value in student_dict.items())[0]

        # делаем инверсию ключей и значений чтобы достать имя, соотвтетсвющие max_num
        student_dict_revers = {key: value for key, value in student_dict.items() if value == max_num}
        name.append(student_dict_revers.keys())
    # Обрабатываем имена как строки - убираем все лишнее
    name = str(name).strip("[dict_keys(['").strip("])]").replace("'", "")
    print(f'Самое частое имя в классе {cnt}: {name}')
print()


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

print('Задание 4')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

students_dict ={}
for class_school in school:
    cnt_male = 0
    cnt_female = 0
    num_class = class_school['class']
    for students in class_school['students']:
        name = students['first_name']
        if is_male[name]:
            cnt_male += 1
        else:
            cnt_female += 1
    # проверяем на повторяемость классов
    if not students_dict.get(num_class):
        students_dict[num_class] = {'девочки': cnt_female, 'мальчики': cnt_male}
    else:
        students_dict[num_class]['девочки'] += cnt_female
        students_dict[num_class]['мальчики'] += cnt_male
# Выводим результат
for key, value in students_dict.items():
    slash = "\'"
    print(f"Класс {key}: {str(value).strip('{').strip('}').replace(':', '').replace(slash, '')}")
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print('Задание 5')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
students_dict ={}
for class_school in school:
    cnt_male = 0
    cnt_female = 0
    num_class = class_school['class']
    for students in class_school['students']:
        name = students['first_name']
        if is_male[name]:
            cnt_male += 1
        else:
            cnt_female += 1
    # проверяем на повторяемость классов
    if not students_dict.get(num_class):
        students_dict[num_class] = {'девочки': cnt_female, 'мальчики': cnt_male}
    else:
        students_dict[num_class]['девочки'] += cnt_female
        students_dict[num_class]['мальчики'] += cnt_male

# Выводим результат
cnt_male = 0
cnt_female = 0
super_class = {}
for key, value in students_dict.items():
    if value['девочки'] > cnt_female:
        cnt_female += value['девочки']
        super_class['девочек'] = key
    elif value['мальчики'] > cnt_male:
        cnt_male += value['девочки']
        super_class['мальчиков'] = key
for key, value in super_class.items():
    print(f'Больше всего {key} в классе {value}')
