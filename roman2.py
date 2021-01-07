def convert_to_roman(num):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanvalue = ""
    for i,d in enumerate(sayi):
        while (num >= d):
            num -= d
            romanvalue += roman[i]
    return romanvalue
print(convert_to_roman(3100))