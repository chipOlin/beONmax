def whois_first(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return 'tie'


def solve_hanoi_tower(discs):
    return 2**discs - 1


def calc_dice_scores(lst):
    return sum([a + b for a, b in lst]) if not any([a == b for a, b in lst]) else 0


def any_duplicates(square):
    plain = [i for x in square for i in x]
    return sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    print(any_duplicates([[2, 4, 1], [1, 3, 5], [7, 8, 9]]))
    # print(calc_dice_scores([(3, 5), (6, 3), (2, 1)]))
    # print(solve_hanoi_tower(10))
    # print(whois_first(" Bang!", "  Bang!"))
    # print(whois_first("Bang!", "Bang!"))
    # print(whois_first("  Bang!", " Bang!"))
