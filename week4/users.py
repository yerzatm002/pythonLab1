import hashlib


class User:
    __password: str
    def __init__(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.__password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()

    @property
    def get_password(self) -> str:
        return self.__password


def create_user(username: str, password: str) -> User:
    user = User(username=username)
    user.set_password(password=password)
    return user


user = create_user(username='yerzatm', password='123456')
print(user.get_password)