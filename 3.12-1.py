def print_hi():
    # sum = 0
    x = int(input("Введите число: "))
    # for i in range(x + 1):
    #     if i % 3 == 0 or i % 5 == 0:
    #         sum += i
    #         print(i)
    arg_list = [i for i in range(x + 1) if i % 3 == 0 or i % 5 == 0]
    sum_args = sum(arg_list)
    print(sum_args)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
