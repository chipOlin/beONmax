# hand = ["7", "J", "3", "4", "2"]
#
#
# def is_full_house(cards):
#     unique_card = set(cards)
#     dict_card = {}
#     for uq in unique_card:
#         if cards.count(uq) < 4:
#             dict_card[uq] = cards.count(uq)
#     return len(dict_card) == 2 and sum(dict_card.values()) == 5
#
#
# print(is_full_house(hand))
#

def is_full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])


print(is_full_house(["A", "A", "A", "K", "K"]))
print(is_full_house(["J", "10", "J", "J", "J"]))
print(is_full_house(["J", "10", "4", "Q", "9"]))
