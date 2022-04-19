def print_hi():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = [11, 12, 13, 14, 15]
    f_list = [fl for fl in first_list if fl % 2 != 0]
    s_list = [sl for sl in second_list if sl % 2 == 0]
    sum_list = f_list + s_list
    print(sum_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
