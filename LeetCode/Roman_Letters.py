#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

def romanToInt(self, s):
    sum = 0
    letters = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    first_number = 0
    last_number = 0
    for i in range(len(s) -1, -1, -1):
        