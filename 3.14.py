def print_hi():
    number = int(input("Enter number: "))

    reversed_number = 0
    tmp_original = number

    while tmp_original > 0:
        reversed_number = (reversed_number * 10) + tmp_original % 10
        tmp_original = tmp_original // 10

    if reversed_number == number:
        print("Palindrome")
    else:
        print("No palindrome")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
