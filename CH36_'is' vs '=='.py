a = 7
b = "7"
print("STR VS INT", a, "\""+b+"\"")
print("is ", a is b)  # False (different types)
print("== ", a == b)  # True (values are equal)

a = 7
b = 7
print("INT VS INT", a, b)
print("is ", a is b)  # True (same object because integers are immutable and Python caches small integers)
print("== ", a == b)  # True (values are equal)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print("LIST VS LIST", a, b)
print("is ", a is b)  # False (different objects)
print("== ", a == b)  # True (values are equal)

a = "soham"
b = "Soham"
print("STR VS STR", "\""+a+"\"", "\""+b+"\"")
print("is ", a is b)  # False (different objects)
print("== ", a == b)  # False (values are not equal, case-sensitive comparison)

b = "soham"
print("STR VS STR", "\""+a+"\"", "\""+b+"\"")
print("is ", a is b)  # True (same object because Python interns small strings)
print("== ", a == b)  # True (values are equal)
