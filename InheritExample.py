class Item:
    def __init__(self):
        self.__name = ''
        self.__quantity = 0

    def __set_name__(self, owner, name):
        self.__name = name

    def __set_quantity__(self, quantity):
        self.__quantity = quantity

    def display(self):
        """Displys the name and quantity"""
        print(self.__name, self.__quantity)

class Produce(Item):
    def __init__(self):
        Item.__init__(self)
        self.__expiration = ''

    def __set_expiration__(self, expire):
        self.__expiration = expire

    def __get_expiration__(self):
        return self.__expiration

    def display(self):
        super().display()
        print(self.__expiration)

item1 = Item()
item1.__set_name__(item1, 'cereal')
item1.__set_quantity__(2)
item1.display()

item2 = Produce()
item2.__set_name__(item2, 'apple')
item2.__set_quantity__(4)
item2.__set_expiration__('sept 25, 24')
item2.display()
