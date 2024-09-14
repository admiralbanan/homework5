import os
import shutil
import platform
import random
import json

BALANCE_FILE = 'balance.txt'
HISTORY_FILE = 'purchases.json'
LISTDIR_FILE = 'listdir.txt'

# Функция для чтения баланса с файла
def read_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            return float(f.read())
    return 0.0

# Функция для сохранения баланса в файл
def save_balance(balance):
    with open(BALANCE_FILE, 'w') as f:
        f.write(str(balance))

# Функция для чтения истории покупок с файла
def read_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

# Функция для сохранения истории покупок в файл
def save_history(purchases):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(purchases, f)

# Функция для сохранения содержимого рабочей директории в файл
def save_directory_contents():
    files = []
    directories = []

    for item in os.listdir():
        if os.path.isfile(item):
            files.append(item)
        elif os.path.isdir(item):
            directories.append(item)

    with open(LISTDIR_FILE, 'w') as f:
        f.write(f"files: {', '.join(files)}\n")
        f.write(f"dirs: {', '.join(directories)}\n")

    print(f"Содержимое рабочей директории сохранено в файл '{LISTDIR_FILE}'.")

# Функция для работы с банковским счетом
def manage_bank_account():
    balance = read_balance()
    purchases = read_history()

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        
        if choice == '1':
            balance = top_up(balance)
            save_balance(balance)
        elif choice == '2':
            balance, purchases = make_purchase(balance, purchases)
            save_balance(balance)
            save_history(purchases)
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
        print("7. Сохранить содержимое директории в файл")
        print("8. Информация об ОС")
        print("9. Создатель программы")
        print("10. Играть в викторину")
        print("11. Мой банковский счет")
        print("12. Сменить рабочую директорию")
        print("13. Выход")
        
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
            save_directory_contents()
        elif choice == '8':
            system_info()
        elif choice == '9':
            creator_info()
        elif choice == '10':
            play_quiz()
        elif choice == '11':
            manage_bank_account()
        elif choice == '12':
            change_directory()
        elif choice == '13':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
