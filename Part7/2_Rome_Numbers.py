def arabic_to_roman(num):
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400:
                 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman_num = ''
    for r in sorted(roman_map.keys(), reverse=True):
        while num >= r:
            roman_num += roman_map[r]
            num -= r
    return roman_num


arabic_num = int(input("Введите арабское число: "))
print(f"Римское число: {arabic_to_roman(arabic_num)}")
