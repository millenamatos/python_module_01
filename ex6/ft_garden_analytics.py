class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.Statistics()

    def show(self):
        self._stats._show += 1
        print(f'{self._name}: {self._height}cm, {self._age} days old')
    
    def grow(self):
        self._stats._grow += 1
        self._height = round(self._height + 8.0, 1)

    def age(self):
        self._stats._age += 1
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
        return self._height

    def get_age(self):
        return self._age

    @staticmethod
    def check_age(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return (cls("Unknown plant", 0.0, 0))

    class Statistics:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0


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


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self):
        super().bloom()
        self._seeds = 42


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        self._stats._shade += 1
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

def show_stats(plant):
   print(f'[statistics for {plant._name}]')
   print(f'Stats: {plant._stats._grow} grow, {plant._stats._age} age, {plant._stats._show} show')
   if isinstance(plant, Tree):
    print(f'{plant._stats._shade} shade')


# auxiliary functions
def show_flower(rose):
    print("=== Flower")
    rose.show()
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_stats(rose)

def show_tree(oak):
    print("\n=== Tree")
    oak.show()
    show_stats(oak)
    oak.produce_shade()
    show_stats(oak)

def show_seed(sunflower):
    print("\n=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)


# main function
def ft_garden_analytics():
    anonymous = Plant.create_anonymous()
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}\n")
    
    show_flower(rose)
    show_tree(oak)
    show_seed(sunflower)

    print("\n=== Anonymous")
    anonymous.show()
    show_stats(anonymous)

if __name__ == "__main__":
    ft_garden_analytics()