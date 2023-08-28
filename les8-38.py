"Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных"

def delete_contact(phonebook, search_key):
    search_key = search_key.capitalize()
    for i in range(len(phonebook)):
        if phonebook[i]['last_name'] == search_key or phonebook[i]['first_name'] == search_key:
            del phonebook[i]


def change_contact(phonebook, search_key, choice_key, val_new):
    search_key = search_key.capitalize()
    contact = ['last_name', 'first_name', 'middle_name', 'phone_number']
    for i in range(len(phonebook)):
        if phonebook[i]['last_name'] == search_key or phonebook[i]['first_name'] == search_key:
            phonebook[i][contact[choice_key-1]] = val_new





def load_file(filename):
    phonebook = []
    try:
        with open(filename, 'r') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number
                })
            print('Данные успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    return phonebook


def search_contacts(phonebook, search_key):
    results = []
    for contact in phonebook:
        if (search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower()):
            results.append(contact)
    return results


def views_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(
            f"{index}. {contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}")


def save_to_file(filename, phonebook):
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(
                f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}")
    print('Данные сохранены в файле')


def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен')


def main():
    phonebook = []
    filename = 'contacts.txt'

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Изменить данные")
        print("7. Удалить данные")
        print("8. Выйти")


        choice = input('Выберите действие: ')
        if choice == '1':
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
            print()
        elif choice == '2':
            save_to_file(filename, phonebook)
            print()
        elif choice == '3':
            views_contacts(phonebook)
            print()
        elif choice == '4':
            search_key = input("Введите имя или фамилию для поиска: ")
            results = search_contacts(phonebook, search_key)
            if (results):
                print('Найдены контакты: ')
                print(results)
            else:
                print('Контактов по вашему запросу нет!')
            print()
        elif choice == '5':
            phonebook = load_file(filename)
            print()
        elif choice == '6':
            search_key = input("Введите имя или фамилию для поиска: ")
            print("1. Изменить Фамилию")
            print("2. Изменить Имя")
            print("3. Изменить Отчество")
            print("4. Изменить Номер телефона")
            choice_key = int(input("Выберите действие: "))
            val_new = input("Введите новое значение: ")
            change_contact(phonebook, search_key, choice_key, val_new)
            print()
        elif choice == '7':
            search_key = input("Введите имя или фамилию для поиска: ")
            delete_contact(phonebook, search_key)
            print()
        elif choice == '8':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')



if __name__ == "__main__":
    main()
    print()
    print()