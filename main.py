from addressbook import AddressBook
from record import Record
from utils import print_menu, get_input, validate_name, validate_phone, validate_birthday

def main():
    book = AddressBook()

    while True:
        print_menu()
        choice = get_input("Оберіть опцію (наприклад, 1): ")

        if choice == '1':
            name = get_input("Введіть ім'я (наприклад, Олег): ")
            if not validate_name(name):
                print("Невірне ім'я. Ім'я повинно містити лише букви.")
                continue

            phone = get_input("Введіть телефон (наприклад, 0987654321): ")
            if not validate_phone(phone):
                print("Невірний телефон. Номер повинен містити 10 цифр.")
                continue

            record = book.find(name)
            if not record:
                record = Record(name)
                book.add_record(record)

            record.add_phone(phone)
            print("Контакт успішно доданий.")

        elif choice == '6':
            name = get_input("Введіть ім'я для додавання дня народження: ")
            record = book.find(name)
            if not record:
                print("Контакт не знайдено.")
                continue

            birthday = get_input("Введіть день народження (DD.MM.YYYY): ")
            if not validate_birthday(birthday):
                print("Невірний формат дня народження.")
                continue

            record.add_birthday(birthday)
            print("День народження успішно доданий.")

        elif choice == '7':
            upcoming = book.get_upcoming_birthdays()
            if not upcoming:
                print("Немає контактів з днями народження на наступному тижні.")
            else:
                print("Контакти, що мають день народження на наступному тижні:")
                for record in upcoming:
                    print(record)

        elif choice == '8':
            print("Програма завершена.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
