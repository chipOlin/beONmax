import random

def print_hi():
    rand_num = random.randint(1, 50)
    tries = 0
    while True:
        inp_num = int(input("Угадай число: "))
        tries += 1
        if rand_num > inp_num:
            print("Бери больше!")

        if rand_num < inp_num:
            print("Бери меньше!")

        if inp_num == rand_num:
            print("Красавчик, угадал!")
            break

        if tries >= 6:
            print("Неудачник!")
            break

    print("Игра завершена!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
