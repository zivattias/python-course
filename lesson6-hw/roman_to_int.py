# For example, 2 is written as II in Roman numeral, just two ones added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
#
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

def roman_to_int() -> int:
    int_value = int()
    rom_value: dict[str: int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s: str = input('Enter a roman numeral: ').upper()
    for i in range(len(s)):
        if i > 0 and rom_value.get(s[i]) > rom_value.get(s[i - 1]):
            int_value += rom_value[s[i]] - 2 * rom_value[s[i - 1]]
        else:
            int_value += rom_value.get(s[i])
    return int_value

print(roman_to_int())

