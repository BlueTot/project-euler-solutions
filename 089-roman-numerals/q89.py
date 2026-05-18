import roman

with open("roman.txt", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]

romanchars = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

def inefficient_roman_to_num(r):
    total = 0
    while r:
        double = r[0:2]
        if double in romanchars:
            total += romanchars[double]
            r = r[2:]
        else:
            single = r[0]
            total += romanchars[single]
            r = r[1:]
    return total
            

chars_saved = 0
for string in data:
    num = inefficient_roman_to_num(string)
    newstring = roman.toRoman(num)
    chars_saved += len(string) - len(newstring)
print(chars_saved)