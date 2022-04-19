def print_hi():
    cards = {
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 0,
        10: -1,
        'J': -1,
        'Q': -1,
        'k': -1,
        'A': -1
    }
    current_hand = [2, 3, 4, 10, 'Q', 5]
    # current_hand = ['A', 3, 4, 10, 'J', 4]
    # current_hand = [2, 7, 4, 9, 3, 5]
    # sum_ch = 0
    # for ch in current_hand:
    #     sum_ch += cards[ch]
    sum_ch = sum([cards[x] for x in current_hand])
    print(sum_ch)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
