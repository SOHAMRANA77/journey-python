class myclass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    @property
    def ten_value(self):
        # Explanation: This property returns 10 times the value.
        return 10 * self.value

    @ten_value.setter
    def ten_value(self, ten_v):
        # Explanation: This setter method allows setting the value based on a new value.
        # It divides the input by 10 to get the desired value.
        self.value = ten_v / 10


a = myclass(1)
a.show()  # Output: Value is 1

a.ten_value = 88  # Setter is invoked
print(a.ten_value)  # Output: 88.0

a.show()  # Output: Value is 8.8
