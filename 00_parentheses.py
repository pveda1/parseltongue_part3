import sys 
g = sys.argv
x = g[1]

count = 1 
punctuation = '''!()-{}[]; :'"\,<>.?@#$%^&*_~'''
new_string = ""

for c in x:
    if c in punctuation:
        new_string+=c
    elif count%2 == 0:
        c = c.lower()
        new_string+=c
        count+=1
    else:
        c = c.upper()
        new_string +=c
        count+=1
print(new_string)


second_str = ""
second_str+=new_string
vowels = "AEIOU"

for h in second_str:
    if h in vowels:
        second_str = second_str.replace(h, "*")
    else:
        h == h 
print(second_str)

par_count = 0
parentheses = 0

for d in new_string:
    if d == "(":
        par_count+=1
    elif d == ")":
        parentheses+=1
    else:
        d == d
if par_count == parentheses:
    print("Balanced? True")
else:
    print("Balanced? False")




        





