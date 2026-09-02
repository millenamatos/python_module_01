class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
    
    def show(self):
        print(f'{self.name}: {self.height}cm, {self.days} days old')
    
    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age(self):
        self.days = self.days + 1

def ft_plant_growth():
    rose = Plant("Rose", 25.0, 30)
    initial_size = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for start in range(7):
        print(f'=== Day {start + 1} ===')
        rose.grow()
        rose.age()
        rose.show()
    print(f'Growth this week: {round(rose.height - initial_size, 1)}cm')

if __name__ == "__main__":
    ft_plant_growth()