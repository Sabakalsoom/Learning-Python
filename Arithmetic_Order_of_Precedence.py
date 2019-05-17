"""
multiplication and division have the same order of precedence so it does not matter which one we do before
and has a higher precedence over + and -
"""

print(2+4*3/2)

"""
we use parenthesis when we want our own order of precedences. 
"""

print((2+4)*3/2)


print((2+4*2)*3/2)  #Multiplication has a higher precedence over addition

a = 10
print(a)

a = a+10
print(a)  #after adding 10 to a

a+=10    #shortcut for above
print(a)

a-=10
print(a)

a*=10
print(a)

a/=10
print(a)
