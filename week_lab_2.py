#Выведите (через пробел) все четные числа от a до b (включительно).
a, b = map(int, input().split())
for i in range(a, b + 1):
   if i % 2 == 0:
       print(i, end=' ')
print('\n', '-------------------------------', '\n', sep='')

#Найдите самый маленький натуральный делитель числа x, отличный от 1 (2 <= x <= 30000).
x = int(input())
i = 2
while x % i > 0:
    i+=1
print(i)
print('\n', '-------------------------------', '\n', sep='')

#Выведите все натуральные делители числа x в порядке возрастания (включая 1 и само число).
x = int(input('x = '))
for i in range(1,x+1):
    if x % i == 0:
      print(i,end = ' ')
print('\n', '-------------------------------', '\n', sep='')

#Вычислите сумму данных N натуральных чисел.
n = int(input())
s = 0
for i in range(n):
    num = int(input())
    s+=num
print(s)
print('\n', '-------------------------------', '\n', sep='')

#Переведите натуральное число из двоичной системы в десятичную (в двоичном числе не более 10 цифр).
n = input()
print(int(n, base=2))

#Напишите функцию double power (double a, int n), function power (a:real; n:longint): real (Pascal), вычисляющую значение an.
a = float(input())
n = int(input())
res = a
for i in range(1,n):
    res *= a
print(res)

#Напишите "функцию голосования" bool Election(bool x, bool y, bool z) (C/C++),
#function Election (x, y, z:boolean): boolean (Pascal), возвращающую то значение (true или false),
#которое среди значений ее аргументов x, y, z встречается чаще.
def ellection(x: bool, y: bool, z: bool):
    print(int((x + y + z) >= 2))


x, y, z = map(int, input().split())
ellection(x,y,z)

#Добавление денег на счет
#Передается float sum -> и далее он должен добавиться на счет. Например:
#addToBankAccount(500) -> если на счете 0 то должно поменяться на 500.
bank_cash = 0.0
def add_to_bank_account(summa: float) -> float:
    return bank_cash + summa


bank_cash = add_to_bank_account(500)
print(bank_cash)

# Высчитывание денег со счета
# Передается float sum -> и далее он должен убрать деньги со счета. Например:
# substractFromBankAccount(200) -> если на счете 500 то должно поменяться на 300.
def substract_from_bank_account(summa: float) -> float:
    return bank_cash - summa


bank_cash = substract_from_bank_account(300)
print(bank_cash)

# Изменение валюты и перерасчет денег на счете (USD -> KZT). Если у вас счет в долларах, то следует вывести их в тенге
# Передается float sum и с какой валюты на какой -> и далее конвертация. Например: moneyConversion(300, USD, KZT) -> вы меняете 300$ -> на KZT то есть происходит умножение 300 * 470 = 14100
def money_conversion(summa: float, from_currency: str, to_currency: str) -> float:
    if from_currency is 'KZT':
        summa = summa / 470
    elif to_currency is 'USD':
        summa = summa * 470
    return summa


print(money_conversion(300, 'USD', 'KZT'))