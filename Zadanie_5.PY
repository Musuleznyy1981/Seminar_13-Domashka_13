
# Задание №5  Мусулезный Максим 26.08.2023
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня меньше, чем ваш уровень, вызывайте исключение уровня доступа.

import json
from Seminar_13.Zadanie4 import  User

from Seminar_13.Zadanie3 import AccesErorr, LevelError
class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass


    @staticmethod
    def load_users(path: str = 'users2.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(User(name, str(id), str(level)))


    def login(self, name: str, id: str) -> str:
        login_user = User(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:
                return user.level
        else:
            raise AccesErorr(name)

    def create_user(self, name: str, id: str, level: str):
        cur_name, cur_id = input("Введите имя авторизированного пользователя и его id через пробел").split()
        if current_level := self.login(cur_name, cur_id):
            if int(current_level) > int(level):
                return User(name, id, level)
            else:
                raise LevelError(current_level, level)


b = UserWorkshop()
print(b.login('Musuleznyy', '1')) #(имя, id)  уровень = 5
print(b.create_user('New_user', '1', '3'))  #создаст нового пользователя (имя, id, уровень) в случае если его уровень меньше, чем уровень указанного авторизированного пользователя