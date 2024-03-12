# @property

# 在下述的 Employee 中 , tax 的值來自於 income
# class Employee:
#     def __init__(self):
#         self.income = 0
#         self.__tax = 0

#     def earn_momey(self, money):
#         self.income += money
#         self.__tax += self.income * 0.05

#     def get_tax(self):
#         return self.__tax


# Kevin = Employee()
# Kevin.earn_momey(500)
# print(Kevin.get_tax())


# class Employee:
#     def __init__(self):
#         self.income = 0

#     def earn_momey(self, money):
#         self.income += money

#     @property
#     def tax_amount(self):
#         return self.income * 0.05


# Kevin = Employee()
# Kevin.earn_momey(500)
# print(Kevin.tax_amount)
# 25


class Employee:
    def __init__(self):
        self.income = 0

    def earn_momey(self, money):
        self.income += money

    @property
    def tax_amount(self):
        return self.income * 0.05

    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20


Kevin = Employee()
Kevin.tax_amount = 200
print(Kevin.income)
