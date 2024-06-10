   def roman_to_int():
    roman = input("Insira seu número em algarismos romanos: ")

    nums = {'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1}

    roman = roman.upper()
    total = 0
    for i in range(len(roman)):
        try:
            value = nums[roman[i]]
            if i + 1 < len(roman) and nums[roman[i + 1]] > value:
                total -= value
            else:
                total += value
        except KeyError:
            raise ValueError('Input is not a valid Roman numeral: %s' % roman)

    return total

print(roman_to_int())

def roman_to_int(s):
