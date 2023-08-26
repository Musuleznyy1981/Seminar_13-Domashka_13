# Мусулезный Максим 26.08.2023
# Банкомат по выдачи и зачислению cash  с учетом комиссии на снятие денег и начисленнию процентов


from datetime import date
import My_exception


class Bankomat:
    __bank: float = 0
    count: int = 0

    def __init__(self, account_num: int, name_bank: str, percent_take: float = 0.015, percent_add: float = 0.03, percent_tax: float = 0.01):
        self.account_num = account_num
        self.name_bank = name_bank
        self.percent_add = percent_add
        self.percent_tax = percent_tax
        self.percent_take = percent_take

    def add_bank(self, cash: float) -> None:
        self.__bank += cash
        self.count += 1
        if self.count % 3 == 0:
            self.__bank = self.__bank + self.percent_add * self.__bank
            print("начислены проценты в размере: ", self.percent_add * self.__bank)

    def take_bank(self, cash: float) -> None:
        self.__bank -= cash
        self.count += 1

        if cash * self.percent_take < 30:
            self.__bank -= 30
            print("списаны проценты за cash: ", 30)
        elif cash * self.percent_take > 600:
            self.__bank -= 600
            print("списаны проценты за cash: ", 600)
        else:
            self.__bank -= cash * self.percent_take
            print("списаны проценты за cash: ", cash * self.percent_take)
        if self.count % 3 == 0:
            self.__bank = self.__bank + self.percent_take * self.__bank
            print("начислены проценты в размере: ", self.percent_add * self.__bank)

    def exit_bank(self):
        print("Рады вас видетеь снова!\n")
        exit()

    def check_bank(self) -> int:
        while True:
            cash = int(input("Введите сумму опреации кратно 50\n"))
            if cash % 50 == 0:
                return cash

    def get_bank(self):
        return self.__bank

    def set_bank(self, bank: float):
        self.__bank = bank


if __name__ == '__main__':
    accounts = []
    list_operation = []

    while(True):
        try:
            account_num = int(input("введите номер счета(целое число): "))
            break
        except ValueError as e:
            print(f"\nНеправильный формат ввода данных: {e}.\n")

    name_bank = input("введите название банка: ")
    accounts.append(Bankomat(account_num, name_bank))
    i = 0
    j = 0


    while True:
        action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю всех операций\n5 "
                       "- создать новый аккаунт(счет)\n6 - перейти на аккаунт(счет)\n7 - список акаунтов\n8 - выход\n")

        if action == '1':
            if accounts[i].get_bank() > 5_000_000:
                accounts[i].set_bank(accounts[i].get_bank() - accounts[i].get_bank() * accounts[i].percent_tax)
                print("списан налог на богатство: ", accounts[i].get_bank() * accounts[i].percent_tax)
            cash = accounts[i].check_bank()
            if cash < accounts[i].get_bank():
                accounts[i].take_bank(cash)
                list_operation.append([i, str(date.today()), -1 * cash,accounts[i].get_bank()])
            else:
                print("no money\n")
            if accounts[i].get_bank() > 5_000_000:
                accounts[i].set_bank(accounts[i].get_bank() - accounts[i].get_bank() * accounts[i].percent_tax)
                print("списан налог на богатство: ", accounts[i].get_bank() * accounts[i].percent_tax)
            print("Баланс = ", accounts[i].get_bank())
        elif action == '2':
            cash = accounts[i].check_bank()

            if cash < 0:
               raise ValueBankError(cash)

            accounts[i].add_bank(cash)
            if accounts[i].get_bank() > 5_000_000:
                accounts[i].set_bank(accounts[i].get_bank() - accounts[i].get_bank() * accounts[i].percent_tax)
                print("списан налог на богатство: ", accounts[i].get_bank() * accounts[i].percent_tax)
            print("Баланс = ", accounts[i].get_bank())

            list_operation.append([i, str(date.today()), cash, accounts[i].get_bank()])

        elif action == '3':
            print("Баланс = ", accounts[i].get_bank())
        elif action == '4':
            print("id  Date  Cash  Balance")
            print(list_operation)
        elif action == '5':
            account_num = int(input("введите номер счета(целое число): "))
            name_bank = input("введите название банка: ")
            accounts.append(Bankomat(account_num, name_bank))
            j = j + 1
            i = j
        elif action == '6':
            i = int(input(f'Введите целое число от 0 до {j}\n'))
            while i > j:
                i = int(input(f'аккаунт не существует\nВведите целое число от 0 до {j}'))
        elif action == '7':
            print(f'id      №сч       банк    баланс')
            for i in range(len(accounts)):
                print(f'{i:<8}{accounts[i].account_num:<10}{accounts[i].name_bank:<8}{accounts[i].get_bank():<8}')
            print('\n')
        else:
            accounts[i].exit_bank()


# Сравнение, умножение, сложение двух матриц

from My_exception import ValFormatError

class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError("+")
            # return f'Error: матрицы разных размеров'
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            raise ValFormatError("*")
            # return f'Error: невозможно перемножить матрицы'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError("eq")
            # return f'Error: матрицы разных размеров'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s


if __name__ == '__main__':

    m_1 = [[1, 2, 4],
              [5, 6,  8],
              [2, 5, -2],
              [10, 5, 0]]

    m_2 = [[1, 2, 4],
              [5, 6,  8],
              [5, 6,  8],
              [-2, 2, 0]]

    m_3 = [[1, 2, 4, 5],
              [5, 6, 8, 0],
              [5, 0, -7, 1]]

    m_4 = [[1, 2, 4, 5, 0],
              [5, 6, 8, 0, 0],
              [5, 0, -7, 1, 0]]

    matr_1 = Matrix(m_1)
    matr_2 = Matrix(m_2)
    matr_3 = Matrix(m_3)
    matr_4 = Matrix(m_4)

    print ("Cложение матриц:")
    matr_sum = matr_1 + matr_2
    print(matr_sum)

    print ("Умножение матриц:")
    matr_mul = matr_1 * matr_3
    print(matr_mul)
    print(matr_1 * matr_4)

    print ("Cравнение матриц:")
    print(matr_1 == matr_3)
    print(matr_1 == matr_2)

class ValError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет невалидное  значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет невалидное  значение  = {self.b}"


class ValFormatError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Error: Невозможно сложить матрицы, матрицы разных размеров"
        elif self.operation == '*':
            return f"Error: Невозможно перемножить матрицы: не подходят размерности"
        else:
            return f"Error: Невозможно сравнить. Матрицы разных размеров"


class ValueBankError(Exception):
    def __init__(self, cash):
        self.cash = cash

    def __str__(self):
        return f"Ошибка ввода. Число {self.cash} < 0 "

# расчет площади, периметра прямоугольника,селадывание и вычитание двух прямоугольников


from My_exception import ValError

class Rectangle:

    def __init__(self, side_a: float, side_b: float | None =None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __str__(self):
        return f"В результате - прямоугольник со сторонами: {self._side_a}   {self._side_b}, периметром: {self.get_perimeter()}, площадью: {self.get_area()}"





if __name__ == '__main__':
    flag = False
    while True:
        if flag:
            choise = input("1 - выход\n2 - продолжить\n")
            if choise == '1':
                break
        flag = True

        try:
            a_1 = float(input('введите первую сторону первого прямоугольника '))
            b_1 = float(input('введите стороны второго прямоугольника '))
            a_2 = float(input('введите первую сторону первого прямоугольника '))
            b_2 = float(input('введите стороны второго прямоугольника'))
        except ValueError as e:
            print(f"\nНеправильный формат ввода данных: {e}.\nПо умолчанию приняты все стороны прямоугольников = 1\n")
            a_1 = a_2 = b_1 = b_2 = 1

        if a_1 <= 0 or b_1 <= 0:
            raise ValError(a_1, b_1)
        if a_2 <= 0 or b_2 <= 0:
            raise ValError(a_2, b_2)

        rectangle_1 = Rectangle(a_1, b_1)
        print(f'{rectangle_1.get_perimeter() = },  {rectangle_1.get_area() = }')
        rectangle_2 = Rectangle(a_2, b_2)
        print(f'{rectangle_2.get_perimeter() = },  {rectangle_2.get_area() = }')
        choise = input("Выберите опреации над прямоугольниками\n1 - сложение\n2 - вычитание\n3 - выход\n")
        match choise:
            case '1':
                rectangle_3 = rectangle_1 + rectangle_2
                print(rectangle_3)

            case '2':
                rectangle_3 = rectangle_1 - rectangle_2
                print(rectangle_3)
            case _:
                break

