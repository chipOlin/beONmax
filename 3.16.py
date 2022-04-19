import random

def print_hi():
    rand_num = random.randint(1, 50)

    while True:
        player = input("Выкидываешь R/S/P: ").lower()

        if player not in ['r', 's', 'p']:
            print("Ты не то выкинул!")
            continue

        pc = random.choice(['r', 's', 'p'])

        print(f"pc - {pc}")

        win_comb = [('p', 'r'), ('r', 's'), ('s', 'p')]

        if player == pc:
            print("Ничья!")
        elif (player, pc) in win_comb:
            print("Игрок победил!")
        else:
            print("Комп победил!")

        if input("Еще раз? (y/n): ") == 'y':
            continue
        else:
            break


    print("Игра завершена!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
