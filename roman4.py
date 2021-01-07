def InttoRoman(number):
    romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
    if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
        return 0
    number = int(number)    
    result = ""
    for key, value in romandict.items():
        while number >= value:
            quotient = number // value 
            result += key * quotient
            number %= value
    return result