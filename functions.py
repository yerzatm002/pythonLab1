from typing import Callable


def say_hello():
    print('hellooo')


def say_hello_name(name='Aza'):
    print(f'Hello {name}')


# always show return type in functions
def print_numbers(numbers, is_reversed=False) -> None:
    numbers.sort(reverse=is_reversed)
    print(numbers)


numbers = [2, 3, 5, 1]
print_numbers(numbers, True)

#типизация ИМПОРТАНТ!!!
def get_full_name(first_name: str, last_name: str) -> str:
    return f'{first_name} {last_name}'.title()

#чтобы сторого не следить за порядком можно указать аргументы с именами
full_name = get_full_name(
    first_name='Yerzat',
    last_name='Meirambekuly',)

print(f'{full_name=}')

def get_string_number_sum(numbers: str) -> int:
    nums = [int(n) for n in numbers if n.isdigit()]
    return sum(nums)

numbers_sum = get_string_number_sum('1234567')
print(f'{numbers_sum=}')

#'*' 'asacad'
# kwargs выводится как дикшонари
def some_thing(name: str, **kwargs):
    print(name)
    print(kwargs)

some_thing('Yerzat', some_arg1='adad', some_arg2='aadadad')

#nice thing!
def user_information(
        first_name: str,
        last_name: str,
        age: int,
        **kwargs,
):
    print(f'first_name: {first_name}')
    print(f'last_name: {last_name}')
    print(f'age: {age}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

user_information(
    'Yerzat',
    'Meirambekuly',
    20,
    is_admin=True,
    salary='150 000$'
)


#Lamda Functions

users = [
    {'first_name': 'Yerzat', 'age': 25},
    {'first_name': 'Yerzat', 'age': 15},
]

print(sorted(users, key=lambda u: u.get('age', 0)))

def call_other_func(some_func: Callable):
    return some_func()

call_other_func(say_hello())