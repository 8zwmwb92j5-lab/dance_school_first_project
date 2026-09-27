# потом переделаю под тг бота

print("==========Танцевальная школа==========")



# показ напрпавлений

schedule = {
    "Hip-Hop": [
        "Пн/Ср 18:00",
        "Вт/Чт 19:30"
    ],
    "Contemporary": [
        "Пн/Ср 17:00",
        "Вт/Чт 15:00"
    ],
    "Breaking": [
        "Вт/Чт 18:30",
        "Пн/Пт 19:30"
    ]
}

# список учеников
students = []

# функция для просмотра записей
def show_students():
    if not students:
        print("Записей пока нет")
    else:
        for number, student in enumerate(students):
            number += 1
            print("--- Запись №" + str(number) + "---")
            print("Имя:" + student["name"])
            print("Телефон:" + student["phone"])
            print("Возраст:" + str(student["age"]))
            print("Направление:" + student["dance_style"])
            print("Группа:" + student["group"])

# функция для записи ученика
def register_student():

    # есть ли направление в расписании
    dance_styles = list(schedule.keys())

    for number, style in enumerate(dance_styles):
        print(f"{number + 1}. {style}")

    while True:
        dance_style_group = int(input("Введите номер направления: "))

        if dance_style_group < 1 or dance_style_group > len(dance_styles):
            print("Некорректно введен номер направления.")
        else:
            selected_dance_style = dance_styles[dance_style_group - 1]
            break

    print(selected_dance_style)

    # показ расписания

    for hours in range(len(schedule[selected_dance_style])):
        print(f"{hours + 1}. {schedule[selected_dance_style][hours]}")

    # выбор группы

    while True:
        group_number = int(input("Выберете номер группы:"))
        # проверка
        if group_number < 1 or group_number > len(schedule[selected_dance_style]):
            print("чо долбаеб нормально введи")
        else:
            selected_group = (schedule[selected_dance_style][group_number - 1])
            print(selected_group)
            break

    # ввод и запоминание имени, телефона и возраста

    student_name = input("Введите ваше имя: ")
    student_phone_number = input("Введите ваш номер телефона:")
    while True:
        student_age = int(input("Введите ваш возраст:"))
        if student_age < 5 or student_age > 100:
            print("ты долбаеб введи нормально возраст он от 5 до 100")
        else:
            break

    # вывод переменных и подтверждение записи

    print("Ваши данные:")
    print(student_name)
    print(student_phone_number)
    print(student_age)

    while True:
        confirmation = input("Вы подтверждаете запись? ")
        if confirmation == "Да" or confirmation == "да":
            print("Запись подтверждена!")
            student = {
                "name": student_name,
                "phone": student_phone_number,
                "age": student_age,
                "dance_style": selected_dance_style,
                "group": selected_group
            }
            students.append(student)
            break
        elif confirmation == "Нет" or confirmation == "нет":
            print("Запись отменена.")
            break
        else:
            print("долбаеб введи просто да или нет")
    print()

def delete_student():
    if not students:
        print("Записей для удаления пока нет")
    else:
        for number, student in enumerate(students):
            print(f"{number + 1}. {student['name']}")
        student_number = int(input("Введите номер записи для удаления"))
        del students[student_number - 1]

def edit_student():
    if not students:
        print("Записей для редактирования нет")
    else:
        print("Доступные для редактирования записи:")
        for number, person in enumerate(students):
            print(f"{number + 1}. {person['name']}")
        student_edit_number = int(input("Введите номер записи для изменения"))
        student = students[student_edit_number - 1]
        print("Выберите, какие данные вы хотите заменить:")
        print("1. Изменить имя")
        print("2. Изменить номер телефона")
        print("3. Изменить возраст")
        print("4. Изменить направление")
        print("5. Изменить группу")

        while True:
            selected_action = input("Выберите, что вы хотите изменить:")
            if selected_action == "1":
                student["name"] = input("Введите новое имя: ")
                break
            elif selected_action == "2":
                student["phone"] = input("Введите новый номер: ")
                break
            elif selected_action == "3":
                student["age"] = int(input("Введите новый возраст: "))
                break
            elif selected_action == "4":
                print("Доступные направления:")
                print("1. Hip-Hop")
                print("2. Contemporary")
                print("3. Breaking")

                dance_style_number = int(input("Введите номер нового направления: "))

                if dance_style_number == 1:
                    student["dance_style"] = "Hip-Hop"
                elif dance_style_number == 2:
                    student["dance_style"] = "Contemporary"
                elif dance_style_number == 3:
                    student["dance_style"] = "Breaking"
                    break

            elif selected_action == "5":
                for number, group in enumerate(schedule[student["dance_style"]]):
                    print(f"{number + 1}. {group}")

                while True:
                    group_number = int(input("Выберите новый номер группы: "))

                    if group_number < 1 or group_number > len(schedule[student["dance_style"]]):
                        print("Некорректный номер группы")
                    else:
                        selected_group = schedule[student["dance_style"]][group_number - 1]
                        student["group"] = selected_group
                        print("Группа изменена!")
                        break
                break

            else:
                print("Некорректный ввод. Выберите число по списку")


while True:
    print("1. Записаться в школу")
    print("2. Посмотреть записи")
    print("3. Удалить запись")
    print("4. Изменить запись")
    print("5. Выйти")
    choice = int(input("Выберите номер действия:"))
    if choice ==  1:
        register_student()
    elif choice == 2:
        show_students()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        edit_student()
    elif choice == 5:
        break
    else:
        print("Введите номер из существующих")











