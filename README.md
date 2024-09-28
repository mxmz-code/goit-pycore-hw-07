# Тема 10. Домашня робота. Розширене Об'єктно-Орієнтоване Програмування в Python

Настав час об'єднати наші попередні домашні завдання в одне в один функціональний проєкт.

#### Сьогодні ви навчитеся:

Створенню класу `Birthday` з можливістю додавання поля для дня народження до контакту
Підтримці нового списку команд, включаючи обробку додавання та показу дня народження для контактів.
Коректному закриттю програми після виконання команди `close` або `exit`

#### Формат здачі:

Розмістіть файли з розв'язанням у репозиторії `goit-pycore-hw-07`, та прикріпіть лінки до них у відповідь на домашнє завдання.
Прикріпіть файл репозиторію у форматi `zip` у відповідь на домашнє завдання.

## Технiчний опис завдання

### Завдання 1

По перше додамо додатковий функціонал до класів з попередньої домашньої роботи:

- Додайте поле birthday для дня народження в клас `Record`. Це поле має бути класу `Birthday`. Це поле не обов'язкове, але може бути тільки одне.

```bash
class Birthday(Field):
def **init**(self, value):
try: # Додайте перевірку коректності даних # та перетворіть рядок на об'єкт datetime
except ValueError:
raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
def **init**(self, name):
self.name = Name(name)
self.phones = []
self.birthday = None
```

- Додайте функціонал роботи з `Birthday` у клас `Record`, а саме функцію `add_birthday`, яка додає день народження до контакту.
- Додайте функціонал перевірки на правильність наведених значень для полів `Phone`, `Birthday`.
- Додайте та адаптуйте до класу `AddressBook` нашу функцію з четвертого домашнього завдання, тиждень 3, `get_upcoming_birthdays`, яка для контактів адресної книги повертає список користувачів, яких потрібно привітати по днях на наступному тижні.

Тепер ваш бот повинен працювати саме з функціоналом класу `AddressBook`. Це значить, що замість словника contacts ми використовуємо `book = AddressBook()`

### Завдання 2

Для реалізації нового функціоналу також додайте функції обробники з наступними командами:

- `add-birthday` - додаємо до контакту день народження в форматі `DD.MM.YYYY`
- `show-birthday` - показуємо день народження контакту
- `birthdays` - повертає список користувачів, яких потрібно привітати по днях на наступному тижні

```bash
@input_error
def add_birthday(args, book): # реалізація

@input_error
def show_birthday(args, book): # реалізація

@input_error
def birthdays(args, book): # реалізація
```

Тож в фіналі наш бот повинен підтримувати наступний список команд:

1. `add [ім'я] [телефон]`: Додати або новий контакт з іменем та телефонним номером, або телефонний номер к контакту який вже існує.
2. `change [ім'я] [старий телефон] [новий телефон]`: Змінити телефонний номер для вказаного контакту.
3. `phone [ім'я]`: Показати телефонні номери для вказаного контакту.
4. `all`: Показати всі контакти в адресній книзі.
5. `add-birthday [ім'я] [дата народження]`: Додати дату народження для вказаного контакту.
6. `show-birthday [ім'я]`: Показати дату народження для вказаного контакту.
7. `birthdays`: Показати дні народження, які відбудуться протягом наступного тижня.
8. `hello`: Отримати вітання від бота.
9. `close або exit`: Закрити програму.

```bash

def main():
book = AddressBook()
print("Welcome to the assistant bot!")
while True:
user_input = input("Enter a command: ")
command, \*args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            # реалізація

        elif command == "show-birthday":
            # реалізація

        elif command == "birthdays":
            # реалізація

        else:
            print("Invalid command.")
```

Для прикладу розглянемо реалізацію команди `add [ім'я] [телефон]`. В функції `main` ми повинні додати обробку цієї команди, в відповідне місце:

```bash
         elif command == "add":
            print(add_contact(args, book))
```

Сама реалізація функції `add_contact` може виглядати наступним чином:

```bash
@input\*error
def add_contact(args, book: AddressBook):
name, phone, \*\* = args
record = book.find(name)
message = "Contact updated."
if record is None:
record = Record(name)
book.add_record(record)
message = "Contact added."
if phone:
record.add_phone(phone)
return message
```

Наша функція `add_contact` має два призначення - додавання нового контакту або оновлення телефону для контакту, що вже існує в адресній книзі.

Параметри функції це список аргументів `args` та сама адресна книга `book`.

- Спочатку функція розпаковує список `args`, отримуючи ім'я `name` і телефон phone з перших двох елементів списку. Решта аргументів ігнорується завдяки використанню \*\_. Далі метод `find` об'єкта `book` виконує пошук запису з іменем `name`. Якщо запис з таким іменем існує, метод повертає цей запис, інакше повертається `None`.
- Якщо запис не знайдено, то це новий контакт і функція створює новий об'єкт Record з іменем `name` і додає його до `book` викликом методу `add_record`. Після додавання нового запису змінній message присвоюється повідомлення `"Contact added."` успішності операції.
- Далі незалежно від того, чи був запис знайдений або створений новий, до цього запису додається телефонний номер за допомогою методу `add_phone`, якщо він був наданий. На завершення функція повертає повідомлення про результат своєї роботи: `"Contact updated."`, якщо контакт був оновлений, або `"Contact added."`, якщо контакт був доданий. Для перехоплення помилок вводу та виведення відповідного повідомлення про помилку використовуємо декоратор `@input_error`.

### Критерії оцінювання:

1. Реалізувати всі вказані команди до бота

2. Всі дані повинні виводитися у зрозумілому та зручному для користувача форматі

3. Всі помилки, такі як неправильний ввід чи відсутність контакту, повинні оброблятися інформативно з відповідним повідомленням для користувача

4. Валідація даних:

- Дата народження має бути у форматі `DD.MM.YYYY`.
- Телефонний номер має складатися з `10` цифр.

5. Програма повинна закриватися коректно після виконання команд `close` або `exit`

### Результат виконаного ДЗ

![Results](/assets/image-1.png)
