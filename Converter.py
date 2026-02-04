numeral_input = input("Enter the roman numerals you want to convert: ") #Input module to get roman numeral input from User


def roman_to_int(numeral):#function responsible for converting Roman Numeral to Integer
    final_answer = 0
    if "CM" in numeral:#These if statments handle cases for numbers such as IV for four, otherwise, it will read as six for example
        final_answer += 900
        numeral = numeral.replace("CM","")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD","")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC","")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL","")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX","")
    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV","")
    
    for i in numeral:
        if i == "M":
            final_answer += 1000#Adds 1000 to value if M is in input
        elif i == "D":
            final_answer += 500#Adds 500 to value if D is in input
        elif i == "C":
            final_answer += 100#Adds 100 to value if C is in input
        elif i == "L":
            final_answer += 50#Adds 50 to value if L is in input 
        elif i == "X":
            final_answer += 10#Adds 10 to value if X is in input
        elif i == "V":
            final_answer += 5#Adds 5 to value if V is in input
        elif i == "I":
            final_answer += 1#Adds 1 to value if I is in input 
        print("The roman numerals you entered translates to: " + str(final_answer) + "!") #Prints output


roman_to_int(numeral_input)   



