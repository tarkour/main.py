import random


def is_vaild(number):
    return 1 <= number <= 100


random_number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

print('Попробуйте отгадать, какое целое число загадал компьютерjn 1 до 100?')
while True:
    num = int(input())
    if is_vaild(num) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if num > random_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    if num < random_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    if num == random_number:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')