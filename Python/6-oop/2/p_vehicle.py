# This class will the parent of all other classes
class Vehicle:

    def __init__(self, brand, model, color, transmission):
        self.brand = brand
        self.model = model
        self.color = color
        self.transmission = transmission

    def display_all(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Color: {self.color}')
        print(f'Transmission: {self.transmission}')

    # del function is used to add some action when the object will deleted 
    # the object is deleted in two ways 
        # 1-- del objName 
        # 2-- when the file execution is completed the object is deleted automatically
    def __del__(self):
        print('Vehicle object is deleted.')
    

v1=Vehicle('Honda', 'City', 'black', 'Auto')
# del v1    #deleting object using del keyword.
# print(v1.brand)
# print(v1.model)
# print(v1.color)
# print(v1.transmission)

# v1.display_all()