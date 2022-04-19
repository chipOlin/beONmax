def print_hi():
    table_cards = ['A_S', 'J_H', '7_D', '8_D', '10_D']
    hands_cards = ['J_D', '3_D']

    table_suites = [i[-1] for i in table_cards]
    hand_suites = [i[-1] for i in hands_cards]

    suites_in_game = table_suites + hand_suites

    # flush = False
    # for suit in "CHSD":
    #     if suites_in_game.count(suit) >= 5:
    #         flush = True
    #         break

    # flush = any([suites_in_game.count(suit) >= 5 for suit in "CHSD"])

    flush = any([sum([card[-1] == suit for card in table_cards + hands_cards]) >= 5 for suit in "CHSD"])

    if flush:
        print("WIN")
    else:
        print("LOSS")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
