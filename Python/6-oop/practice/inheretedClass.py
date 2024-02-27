from class_attributes import Animals

class Goat(Animals):

    def __init__(self,color, weight):
        super().__init__('Goat', 4, 'Grass')
        self.color = color
        self.weight = weight
    
    def get_color(self):
        print(f'Color: {self.color}')

    def get_weight(self):
        print(f'Weight: {self.weight}')

    def goat_info(self):
        print(f'Color: {self.color}')
        print(f'Weight: {self.weight}')
    
goat1 = Goat('pink', '50kg')
# from parent
goat1.all_animal()
# own function
goat1.get_color()
# own function
goat1.get_weight()