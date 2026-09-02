class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def show(self):
        print(f'Created: {self.name}: {self.starting_height}cm, {self.starting_age} days old')

def ft_plant_factory():
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    list = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plants in list:
        plants.show()

if __name__ == "__main__":
    ft_plant_factory()