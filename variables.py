"""
table
object reference count
"""
a = "nyc"
b = "nyc"
c = "nyc"


a = 123
print(a)
print(b)

c = 'what'
d = c
print(d==c)
print(d is c)

