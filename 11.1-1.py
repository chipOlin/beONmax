# vowels = ["a", "e", "i", "o", "u", "y"]
#
#
# def count_vowels(string) -> int:
#     string.lower()
#     c = 0
#     for s in string:
#         if s in vowels:
#             c += 1
#     return c
#
#
# print(count_vowels(input("Input string: ")))
#
#
def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeiou'])


print(count_vowels('blablabla'))