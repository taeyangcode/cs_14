# Question 1

# retail_item.py


class RetailItem:
    def __init__(self, description, unit_amount, price):
        # description
        self.__description = description
        # unit amount
        self.__unit_amount = unit_amount
        # price
        self.__price = price

    # accessor methods

    def get_description(self):
        return self.__description

    def get_unit_amount(self):
        return self.__unit_amount

    def get_price(self):
        return self.__price

    # mutator methods

    def set_description(self, description):
        self.__description = description

    def set_unit_amount(self, unit_amount):
        self.__unit_amount = unit_amount

    def set_price(self, price):
        self.__price = price
