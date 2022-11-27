import os
import re
from tokenize import String


class Item():
    # ініціалізація товарів
    def __init__(self, item_name, item_type, item_quantity):
        self.__item_name = str(item_name)
        self.__item_type: str = item_type
        self.__item_quantity = item_quantity

    def get(self, key):
        if (key == "item_name"):
            value = self.__item_name
        elif (key == "item_type"):
            value = self.__item_type
        elif (key == "item_quantity"):
            value = self.__item_quantity
        else:
            print("Задано неіснуюче поле")
        return value

    # редагує окреме поле рядка
    def edit(self, key, value):
        if (key == "item_name"):
            self.__item_name = value
        elif (key == "item_type"):
            self.__item_type = value
        elif (key == "item_quantity"):
            self.__item_quantity = value

    # друк одного рядка
    def print(self):
        print("{0:25} | {1:20} | {2:25}".format(
            self.__item_name,
            self.__item_type,
            self.__item_quantity
        )
        )

    def join(self):
        # обє'днати всі характеристики товару через знак ","
        return (','.join(
            (self.__item_name,
             str(self.__item_type),
             str(self.__item_quantity)
             )
        )
        )

    def set(self, text_row: String):
        # конвертувати всі характеристики з файлу
        try:
            list = text_row.split(',')
            self.__item_name = list[0]
            self.__item_type = list[1]
            self.__item_quantity = list[2]
            print("Convert is successful")
            return self
        except:
            print("Convert is failed")


class Items():
    # в цьому класі зберігається масив об'єктів класу Item і методи для роботи з цим масивом
    def __init__(self):
        self.__items = []

    # + новий товар
    def create(self, item_name, item_type, item_quantity):
        try:
            item = Item(item_name, item_type,
                              item_quantity)
            self.__items.append(item)
            print("Creating is succesfull")
            return
        except:
            print("Creating is failed")

    # шукає по назві товару і видаляє його
    def delete(self, name):
        success = False  # змінна успішне завершення
        for i in range(len(self.__items)):
            if re.match("^.?"+name+".*", self.__items[i].get("item_name")):
                self.__items.remove(self.__items[i])
                success = True
                break
        return success

    # друкує всі товари
    def print(self):
        print("-"*120)
        print("{0:25} | {1:20} | {2:25}".format(
            "Назва товару",
            "Одиниці виміру",
            "Кількість"
        )
        )
        print("-"*120)
        for item in self.__items:
            item.print()
        print("-"*120)

    def change_qua(self, name, qua):
        success = False  # змінна успішне завершення
        for item in self.__items:
            if re.match("^"+name+".*", item.get("item_name")):
                #self.__items.delete
                item.print() 
                quantity = item.get("item_quantity")

                new = quantity - qua
                print(new)
                item.edit("item_quantity", new)
                success = True
                break
                
        return success

    def find_items(self):
        # пошук
        while True:
            choice = int(
                input("Шукати товар за:\n1 - Назвою\t2 - Кількістю\n"))

            if choice == 1:
                pattern = input("Введіть назву товару: ")
                print("-"*120)
                print("{0:25} | {1:20} | {2:25}".format(
                    "Назва товару",
                    "Одиниці виміру",
                    "Кількість"                    
                )
                )
                print("-"*120)
                for item in self.__items:
                    if re.match("^"+pattern+".*", item.get("item_name")):
                        item.print()
                print("-"*120)
                break

            elif choice == 2:
                pattern = input("Введіть кількість: ")
                print("-"*120)
                print("{0:25} | {1:20} | {2:25}".format(
                    "Назва товару",
                    "Одиниці виміру",
                    "Кількість"                    
                )
                )
                print("-"*120)
                for item in self.__items:
                    if re.match("^"+pattern+".*", item.get("item_quantity")):
                        item.print()
                print("-"*120)
                break

            else:
                print("Введено неправильний символ")
        return

    def read_from_file(self, fileName):
        # читає з файлу
        print("items start read")
        if (len(self.__items) > 0):
            print("set is full")
            return
        file_reader = open(fileName, mode='r', encoding="utf-8")
        data_list = file_reader.read().strip().split("\n")
        for row in data_list:
            item = Item('', '', '')
            self.__items.append(item.set(row))
        file_reader.close()

    def save_to_file(self, fileName):
        # зберігає у файл
        file_writer = open(fileName, mode='w', encoding="utf-8")
        for item in self.__items:
            file_writer.write(item.join()+"\n")
        file_writer.close()


class Storage():
    # ініціалізація складів
    def __init__(self, name, address, phone_number, capacity):
        self.__name: str = name
        self.__address = address
        self.__phone_number = phone_number
        self.__capacity = capacity

    def get(self, key):
        if (key == "name"):
            value = self.__name
        elif (key == "address"):
            value = self.__address
        elif (key == "phone_number"):
            value = self.__phone_number
        elif (key == "capacity"):
            value = self.__capacity
        else:
            print("Задано неіснуюче поле")
        return value

    # редагує окреме поле рядка
    def edit(self, key, value):
        if (key == "name"):
            self.__name = value
        elif (key == "address"):
            self.__address = value
        elif (key == "phone_number"):
            self.__phone_number = value
        elif (key == "capacity"):
            self.__capacity = value

    # друк одного рядка
    def print(self):
        print("{0:15} | {1:15} | {2:15} | {3:13}".format(
            self.__name,
            self.__address,
            self.__phone_number,
            self.__capacity
        )
        )

    def join(self):
        # обє'днати всі характеристики  через знак ","
        return (','.join(
            (
                self.__name,
                self.__address,
                self.__phone_number,
                self.__capacity
            )
        )
        )

    def set(self, text_row: String):
        # конвертувати всі характеристики  з файлу
        try:
            list = text_row.split(',')
            self.__name = list[0]
            self.__address = list[1]
            self.__phone_number = list[2]
            self.__capacity = list[3]
            return self
        except:
            print("String is not converted")


class Storages():
    # в цьому класі зберігається масив об'єктів класу storage і методи для роботи з цим масивом
    def __init__(self):
        self.__storages = []

    # + нова група
    def create(self, name, address, phone_number, capacity):
        try:
            storage = Storage(name, address, phone_number, capacity)
            self.__storages.append(storage)
            print("Creating is succesfull")
            return
        except:
            print("Creating is failed")

    # шукає групу за назвою та видаляє
    def delete(self, name):
        success = False  # змінна успішне завершення
        for i in range(len(self.__storages)):
            if re.match("^"+name+".*", self.__storages[i].get("name")):
                self.__storages.remove(self.__storages[i])
                success = True
                break
        return success

    # друкує всі групи
    def print(self):
        print("-"*100)
        print("{0:15} | {1:15} | {2:15} | {3:15}".format(
            "Назва складу",
            "Адрес",
            "Номер телефону",
            "Місткість"
        )
        )
        print("-"*100)
        for storage in self.__storages:
            storage.print()
        print("-"*100)

    def find_storages(self):
        # пошук
        while True:
            choice = int(
                input("Шукати склад за:\n1 - Назвою\t2 - Місткістю\n"))

            if choice == 1:
                pattern = input("Введіть назву: ")
                print("-"*100)
                print("{0:15} | {1:15} | {2:9} | {3:13}".format(
                    "Назва складу",
                    "Адрес",
                    "Номер телефону",
                    "Місткість"
                )
                )
                print("-"*100)
                for storage in self.__storages:
                    if re.match("^"+pattern+".*", storage.get("name")):
                        storage.print()
                print("-"*100)
                break

            if choice == 2:
                pattern = str(input("Введіть місткість: "))
                print("-"*100)
                print("{0:15} | {1:15} | {2:9} | {3:13}".format(
                    "Назва складу",
                    "Адрес",
                    "Номер телефону",
                    "Місткість"
                )
                )
                print("-"*100)
                for storage in self.__storages:
                    if re.match("^"+pattern+".*", storage.get("capacity")):
                        storage.print()
                print("-"*100)
                break

            else:
                print("Введено неправильний символ")
        return

    def read_from_file(self, fileName):
        # читання з файлу
        print("Storages start read")
        if (len(self.__storages) > 0):
            print("full")
            return
        file_reader = open(fileName, mode='r', encoding="utf-8")
        data_list = file_reader.read().strip().split("\n")
        for row in data_list:
            storage = Storage('', '', '', '')
            self.__storages.append(storage.set(row))
        file_reader.close()

    def save_to_file(self, fileName):
        # зберігання у файл
        file_writer = open(fileName, mode='w', encoding="utf-8")
        for storage in self.__storages:
            file_writer.write(storage.join()+"\n")
        file_writer.close()


file_name_items = "items.txt"
file_name_storages = "storages.txt"

items = Items()
storages = Storages()

items.read_from_file(file_name_items)
storages.read_from_file(file_name_storages)

def options():

    print("1:  Вивести список товарів")
    print("2:  Прийом/Відпуск товарів")
    print("3:  Вивести список складів")
    print("4:  Пошук товарів")
    print("5:  Пошук складів")
    print("6:  Додати товар")
    print("7:  Додати склад")
    print("8:  Видалити товар")
    print("9:  Видалити склад")
    print("10: Зберегти зміни y файл")
    print("11: clear")
    print("12: exit")


os.system("cls")

while True:
    options()
    try:
        option = int(input())

        if option == 1:
            items.print()
        elif option == 2:
            name = input("Введіть назву товару: ")
            qua = input("Введіть кількість: ")
            print()
            items.change_qua(name, qua)
        elif option == 3:
            storages.print()
        elif option == 4:
            items.find_items()
        elif option == 5:
            storages.find_storages()
        elif option == 6:
            name = input("Назва товару: ")
            type = input("Одиниці виміру: ")
            qua = input("Кількість: ")
            items.create(name, type, qua)
        elif option == 7:
            name = input("Назва: ")
            count = input("Адреса: ")
            date_start = input("Номер телефону: ")
            spicialty = input("Місткість: ")
            storages.create(name, count, date_start, spicialty)
        elif option == 8:
            name = str(input("Введіть назву товару: "))
            items.delete(name)
        elif option == 9:
            name = input("Введіть назву складу: ")
            storages.delete(name)
        elif option == 10:
            items.save_to_file(file_name_items)
            storages.save_to_file(file_name_storages)
        elif option == 11:
            os.system("cls")
        elif option == 12:
            break
        else:
            print("Опція не із списку\n")
    except:
        print("Неправильне значення\n")

    print("\nBикoнaнo")
    input("ENTER")
    print()

print("До зустрічі!")
