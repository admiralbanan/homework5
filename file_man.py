import os
import shutil
import platform
import random

# Функция для создания папки
def create_folder():
    folder_name = input("Введите имя папки для создания: ")
    os.makedirs(folder_name, exist_ok=True)
    print(f"Папка '{folder_name}' создана.")

# Функция для удаления файла или папки
def delete_file_folder():
    name = input("Введите имя файла/папки для удаления: ")
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' удалена.")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' удален.")
    else:
        print(f"Файл или папка '{name}' не найдены.")

# Функция для копирования файла или папки
def copy_file_folder():
    src = input("Введите имя копируемого файла/папки: ")
    dst = input("Введите новое имя файла/папки: ")
    if os.path.isdir(src):
        shutil.copytree(src, dst)
        print(f"Папка '{src}' скопирована как '{dst}'.")
    elif os.path.isfile(src):
        shutil.copy(src, dst)
        print(f"Файл '{src}' скопирован как '{dst}'.")
    else:
        print(f"Файл или папка '{src}' не найдены.")

# Функция для отображения содержимого директории
def list_directory():
    print("Содержимое рабочей директории:")
    for item in os.listdir():
        print(item)

# Функция для отображения только папок
def list_folders():
    print("Папки в рабочей директории:")
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

# Функция для отображения только файлов
def list_files():
    print("Файлы в рабочей директории:")
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)

# Функция для отображения информации об ОС
def system_info():
    print("Информация об операционной системе:")
    print(platform.system(), platform.release())

# Функция для отображения информации о создателе программы
def creator_info():
    print("Создатель программы: Иван Иванов")

# Функция для викторины
def play_quiz():
    famous_people = {
        "А.С. Пушкин": "06.06.1799",
        "Л.Н. Толстой": "09.09.1828",
        "М.В. Ломоносов": "19.11.1711",
        "Ф.М. Достоевский": "11.11.1821",
        "П.И. Чайковский": "07.05.1840",
        "А.П. Чехов": "29.01.1860",
        "С.А. Есенин": "03.10.1895",
        "И.С. Тургенев": "09.11.1818",
        "В.В. Маяковский": "19.07.1893",
        "Н.В. Гоголь": "01.04.1809"
    }

    selected_people = random.sample(list(famous_people.items()), 5)
    correct_answers = 0

    for person, birth_date in selected_people:
        user_answer = input(f"Введите дату рождения {person} в формате 'dd.mm.yyyy': ")
        if user_answer == birth_date:
            print("Верно!")
            correct_answers += 1
        else:
            print(f"Неверно! Правильная дата: {birth_date}")

    print(f"Количество правильных ответов: {correct_answers} из 5")

# Функция для работы с банковским счетом
def manage_bank_account():
    balance = 0
    purchases = []

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        
        if choice == '1':
            balance = top_up(balance)
        elif choice == '2':
            balance, purchases = make_purchase(balance, purchases)
        elif choice == '3':
            show_history(purchases)
        elif choice == '4':
            print("Возвращение в главное меню")
            break
        else:
            print('Неверный пункт меню')

def top_up(balance):
    amount = float(input('Введите сумму для пополнения: '))
    balance += amount
    print(f'Счет пополнен на {amount}. Баланс: {balance}')
    return balance

def make_purchase(balance, purchases):
    amount = float(input('Введите сумму покупки: '))
    if amount > balance:
        print('Недостаточно средств.')
    else:
        item = input('Введите название покупки: ')
        balance -= amount
        purchases.append((item, amount))
        print(f'Покупка "{item}" на сумму {amount} завершена. Баланс: {balance}')
    return balance, purchases

def show_history(purchases):
    if purchases:
        print('История покупок:')
        for item, amount in purchases:
            print(f'{item}: {amount}')
    else:
        print('История покупок пуста.')

# Функция для смены рабочей директории
def change_directory():
    new_dir = input("Введите путь к новой рабочей директории: ")
    try:
        os.chdir(new_dir)
        print(f"Рабочая директория изменена на: {new_dir}")
    except FileNotFoundError:
        print("Папка не найдена")

# Главное меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить файл/папку")
        print("3. Копировать файл/папку")
        print("4. Просмотр содержимого директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Информация об ОС")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Сменить рабочую директорию")
        print("12. Выход")
        
        choice = input("Выберите пункт: ")
        
        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_file_folder()
        elif choice == '3':
            copy_file_folder()
        elif choice == '4':
            list_directory()
        elif choice == '5':
            list_folders()
        elif choice == '6':
            list_files()
        elif choice == '7':
            system_info()
        elif choice == '8':
            creator_info()
        elif choice == '9':
            play_quiz()
        elif choice == '10':
            manage_bank_account()
        elif choice == '11':
            change_directory()
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
