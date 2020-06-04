from parse import compile

p = compile("It's {}, I love it!")
print(p)

result = p.parse("It's spam, I Love It!")
print (result)
print (result[0])