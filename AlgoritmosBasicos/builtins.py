print(type(1))

built = __builtins__.type("Olá!")

print(built)
print(dir())

a = 2
b = 5
b **= a
print(b)
print(dir())
print(dir(__builtins__))
# O builtins está no escopo global do python
