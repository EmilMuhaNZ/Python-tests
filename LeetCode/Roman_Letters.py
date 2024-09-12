#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

def romanToInt(s):
    sum = 0
    letters = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    first_number = 0
    next_number = 0
    for i in range(len(s) -1, -1, -1):
        current_number = s[i]
        first_number = next_number
        next_number = values[letters.index(current_number)]
        if next_number >= first_number:
            sum += next_number
        else:
            sum -= next_number
    return sum