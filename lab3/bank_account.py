from enum import Enum


class Account(Enum):
    USD = 1
    RUB = 2
    KZT = 3
    EUR = 4


class BankAccount:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._account = Account.KZT
        self._cash = 0.0

    def getname(self):
        return self._name

    def setname(self, name):
        self._name = name

    def getsurname(self):
        return self._surname

    def setsurname(self, surname):
        self._surname = surname

    def getaccount(self):
        return self._account

    def setaccount(self, account: Account):
        self._account = account

    def getcash(self):
        return self._cash

    def setcash(self, cash):
        self._cash = cash

    def add_to_bank_account(self, summa: float):
        self._cash += summa

    def substract_from_bank_account(self, summa: float):
        self._cash -= summa

    def money_conversion(self, from_currency: str, to_currency: str) -> float:
        if from_currency == 'KZT' & to_currency == 'USD':
            self._cash /= 470
        elif from_currency == 'USD' & to_currency == 'KZT':
            self._cash *= 470
        elif from_currency == 'KZT' & to_currency == 'RUB':
            self._cash *= 8
        elif from_currency == 'RUB' & to_currency == 'KZT':
            self._cash /= 8
        elif from_currency == 'EUR' & to_currency == 'KZT':
            self._cash *= 520
        elif from_currency == 'KZT' & to_currency == 'EUR':
            self._cash /= 520

    def __repr__(self)-> str:
        return f'{self._name} {self._surname} {self._cash} {self._account}'

    def __del__(self):
        print('bank account is destroyed')


bankAccounts = []
while(True):
    print('Выберите ваше действия:')
    print('1. Создать пользователя')
    print('2. Выбрать пользователя')
    print('3. Выход')
    command = int(input())
    match command:
        case 1:
            name = str(input('name: '))
            surname = str(input('surname: '))
            bankAccount = BankAccount(name=name, surname=surname)
            bankAccounts.append(bankAccount)
        case 2:
            idBank = int(input('id of account '))
            print(bankAccounts[idBank])
        case 3:
            break
