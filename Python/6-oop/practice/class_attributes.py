class Animals:

    def __init__(self, name, legs, eat):
        self.name=name
        self.legs=legs
        self.eat=eat

    def name_animal(self):
        print(self.name)

    def legs_animal(self):
        print(self.legs)

    def eat_animal(self):
        print(self.eat)
    
    def all_animal(self):
        print(f'Name: {self.name}')
        print(f'Legs: {self.legs}')
        print(f'Eat: {self.eat}')