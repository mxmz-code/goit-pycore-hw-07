def print_menu():
    print("╔═════════════════════════════╗")
    print("║      Адресна Книга          ║")
    print("╠═════════════════════════════╣")
    print("║ 1. Додати контакт           ║")
    print("║ 2. Знайти контакт           ║")
    print("║ 3. Редагувати телефон       ║")
    print("║ 4. Видалити контакт         ║")
    print("║ 5. Переглянути всі контакти ║")
    print("║ 6. Додати день народження   ║")
    print("║ 7. Вивести дні народження   ║")
    print("║ 8. Вихід                    ║")
    print("╚═════════════════════════════╝")

def get_input(prompt):
    return input(prompt)

def validate_name(name):
    return name.isalpha()

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_birthday(birthday):
    try:
        datetime.strptime(birthday, '%d.%m.%Y')
        return True
    except ValueError:
        return False
