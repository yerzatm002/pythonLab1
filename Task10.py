from typing import Iterable, Iterator

names = ('Yerzat', 'Azamat', "Dias")

for index, name in enumerate(names):
    if index%2==0:
        print(f'{index}: {name=}')

# numbers = (range(0, 10))
# print(numbers)

names = [n for n in names if n.startswith('Y')]
print(names)

user = {
    'first_name': 'Yerzat',
    'last_name': 'Meirambekuly',
    'username': 'yerzatm',
}

for key, value in user.items():
    print(key, ':', value)
custom_user = {
    k: user[k] for k in user
}
print(custom_user)

if first_name := user.get('first_name'):
    print(first_name)

print(user.get('is_admin', False))