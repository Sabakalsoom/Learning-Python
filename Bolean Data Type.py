"""
Bolean has only two possibilities:
1 or 0
white or black
True or False

The number 0 is false in any form (empty)
the number 1 is true in any form (non-empty)
"""

a = True
b = False
print(a)
print(b)

print("****")
print(bool())
print(bool(0))
print(bool(1))
print(bool(2))


c = ""
print(bool(c))  #it prints false becuase its an empty string

c = "2"
print(bool(c)) #It prints true because it is non-empty.

print("****")
c = 0
print(bool(c))

c = "0"
print(bool(c))



