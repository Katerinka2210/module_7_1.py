from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name #  название продукта
        self.weight = weight # общий вес товара
        self.category = category # категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')  # открыли файл в режиме чтения
        products = file.read()  #  создали перепеменную, в которую вписали содержимое файла
        file.close()  # закрыли файл после выполенных действий
        return products # вернули содержимое файла

    def add(self, *products):
        current_products = self.get_products() # в текущие продукты вписали содержимое файла
        file = open(self.__file_name, 'a') # открыли файл в режиме добавления
        for i in products:  # перебрали заданные продукты
            if str(i.name) not in current_products: # если продукта(его строкового значения)  нет в содержимом файла
                file.write(str(i) + '\n') # то добавим  этот продукт и сделаем отступ на след. строку
                current_products += str(i) + '\n' # запишем его в содержимое файла
            else:
                print(f'Продукт {i.name} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
