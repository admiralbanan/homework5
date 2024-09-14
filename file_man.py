import os
import shutil
import platform
import random
import json

BALANCE_FILE = 'balance.txt'
HISTORY_FILE = 'purchases.json'
LISTDIR_FILE = 'listdir.txt'

# Декоратор для обработки исключений ввода/вывода файлов
def file_exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Файл не найден.")
        except IOError:
            print("Ошибка ввода-вывода.")
    return wrapper

@file_exception_handler
def read_balance():
    return float(open(BALANCE_FILE, 'r').read()) if os.path.exists(BALANCE_FILE) else 0.0

@file_exception_handler
def save_balance(balance):
    with open(BALANCE_FILE, 'w') as f:
        f.write(str(balance))

@file_exception_handler
def read_history():
    return json.load(open(HISTORY_FILE, 'r')) if os.path.exists(HISTORY_FILE) else []

@file_exception_handler
def save_history(purchases):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(purchases, f)

@file_exception_handler
def save_directory_contents():
    with open(LISTDIR_FILE, 'w') as f:
        files = (item for item in os.listdir() if os.path.isfile(item))
        dirs = (item for item in os.listdir() if os.path.isdir(item))
        f.write(f"files: {', '.join(files)}\n")
        f.write(f"dirs: {', '.join(dirs)}\n")
    print(f"Содержимое рабочей директории сохранено в файл '{LISTDIR_FILE}'.")

def manage_bank_account():
    balance = read_balance()
    purchases = read_history()

    while True:
        print('\n1. Пополнение счета\n2. Покупка\n3. История покупок\n4. Выход')

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
    try:
        amount = float(input('Введите сумму для пополнения: '))
        return balance + amount
    except ValueError:
        print("Ошибка: введите корректное число.")
        return balance

def make_purchase(balance, purchases):
    try:
        amount = float(input('Введите сумму покупки: '))
        if amount > balance:
            print('Недостаточно средств.')
        else:
            item = input('Введите название покупки: ')
            balance -= amount
            purchases.append((item, amount))
            print(f'Покупка "{item}" на сумму {amount} завершена. Баланс: {balance}')
    except ValueError:
        print("Ошибка: введите корректное число.")
    return balance, purchases

def show_history(purchases):
    if purchases:
        print('История покупок:')
        print('\n'.join(f'{item}: {amount}' for item, amount in purchases))
    else:
        print('История покупок пуста.')

# Главное меню
def main_menu():
    while True:
        print("\nМеню:\n1. Создать папку\n2. Удалить файл/папку\n3. Копировать файл/папку\n4. Просмотр содержимого директории\n5. Посмотреть только папки\n6. Посмотреть только файлы\n7. Сохранить содержимое директории в файл\n8. Информация об ОС\n9. Создатель программы\n10. Играть в викторину\n11. Мой банковский счет\n12. Сменить рабочую директорию\n13. Выход")
        
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
