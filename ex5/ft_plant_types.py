class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        print(f'{self._name}: {self._height}cm, {self._age} days old')
    
    def grow(self):
        self._height = round(self._height + 2.1, 1)

    def age(self):
        self._age = self._age + 1

    def set_height(self, new_height):
        if (new_height < 0):
            print(f"{self._name}: Error, height can't be negative\nHeight update rejected")
        else:
            self._height = new_height
            print(f'Height updated: {self._height}cm')
    
    def set_age(self, new_age):
        if (new_age < 0):
             print(f"{self._name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = new_age
            print(f'Age updated: {self._age} days \n')
       
    def get_height(self):
        return round(self._height + 0.0, 1)

    def get_age(self):
        return self._age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, season):
        super().__init__(name, height, age)
        self._season = season
        self._nutrition = 0

    def grow(self):
        super().grow()
        self._nutrition = self._nutrition + 0.5

    def age(self):
        super().age()
        self._nutrition = self._nutrition + 0.5

    def show(self):
        super().show()
        print(f"Harvest season: {self._season}")
        print(f"Nutritional value: {int(self._nutrition)}")


def ft_plant_types():
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for start in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()

if __name__ == "__main__":
    ft_plant_types()