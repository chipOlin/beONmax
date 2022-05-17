romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def parse_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[c] < romans[roman[i + 1]]:
            result -= romans[c]
        else:
            result += romans[c]
    return result


print(parse_roman("I") == 1)
print(parse_roman("IV") == 4)
print(parse_roman("VI") == 6)
print(parse_roman("XIX") == 19)
print(parse_roman("LI") == 51)
print(parse_roman("MLXI") == 1061)
