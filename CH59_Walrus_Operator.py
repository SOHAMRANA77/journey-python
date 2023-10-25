import time

# Example of the walrus operator :=
A = True
print(A := False)

number = [1, 2, 3, 4, 5, 6, 7]
while n := len(number) > 0:
    print(number.pop())
    time.sleep(1)
if not number:
    print("Launch")

# Collect food names until "Quit" is entered
foods = []
while (food := input("Enter the Food Name: ").strip().capitalize()) != "Quit":
    foods.append(food)

print("Food list:", foods)
