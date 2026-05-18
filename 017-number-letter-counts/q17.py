
words= {1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten"}

tens = {1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"}

tens_only = {11: "eleven",
             12: "twelve",
             13: "thirteen",
             14: "fourteen",
             15: "fifteen",
             16: "sixteen",
             17: "seventeen",
             18: "eighteen",
             19: "nineteen"}

def get_letter_form(num):
    string = ""
    if num >= 1000:
        string += words[num // 1000] + " thousand "
        num -= (num // 1000) * 1000
    if num >= 100:
        string += words[num // 100] + " hundred"
        num -= (num // 100) * 100
    if 11 <= num <= 19:
        string += " and " + tens_only[num] if string != "" else tens_only[num]
        num -= num
    if num >= 10:
        string += " and " + tens[num//10] if string != "" else tens[num//10]
        num -= (num // 10) * 10
    if num >= 1:
        if string == "":
            string += words[num]
        elif string[-1] == "d":
            string += " and " + words[num]
        else:
            string += " " + words[num]
    return string

total = ""
for n in range(1, 1001):
    
    print(s := get_letter_form(n).replace(" ", ""))
    total += s
    
print(len(total))
    
