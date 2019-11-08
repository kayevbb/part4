def decorator(func):
    def wrapper(self, name, password):
        if name == '':
            raise Exception("No username defined!")
        elif password == '':
            raise Exception("No password to change!")
        elif self.kwargs[name] == password:
            func(name, password)
    return wrapper

class User:
    def __init__(self):
        self.kwargs = {'Bektur': 1234, 'Jenish': 0000}

    @decorator
    def get_account_balance(name, password):
        print('Hello')

    @decorator
    def change_password(name, password):
        print('Ok')


user = User()
user.get_account_balance('Jenish', 0000)
user.change_password('Bektur', 1234)