class Laptop:
    def __init__(self, brand, memory=8):
        self.brand = brand
        self.memory = memory

my_laptop = Laptop("HP", 16)
print(my_laptop.memory)