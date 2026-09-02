class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        print(f'Plant created: {self._name}: {self._height}cm, {self._age} days old\n')
    
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

def ft_garden_security():
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-10)
    rose.set_age(-20)
    print(f'Current state: Rose: {rose.get_height()}cm, {rose.get_age()} days old')

if __name__ == "__main__":
    ft_garden_security()