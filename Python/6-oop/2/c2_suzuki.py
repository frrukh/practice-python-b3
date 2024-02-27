from p_vehicle import Vehicle

# vehicle is parent of this class:
class Suzuki(Vehicle):
    def __init__(self, model, color, transmission, madeIn):
        super().__init__('Suzuki',model,color,transmission)
        self.madeIn=madeIn

    def about_car(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Color: {self.color}')
        print(f'Transmission: {self.transmission}')

    def about_Suzuki(self):
        print('Suzuki is a Japanese multinational recognized for its automobiles and motorcycles.')

    def __del__(self):
        print('Suzuki object is deleted.')


# eMehran is the child of Suzuki and grand child of Vehicles and we can access all the functions and variables of Suzuki and Vehicle from eMehran.
class eMehran(Suzuki):
    
    
    def __init__(self,color):
        super().__init__('E-Mehran', color, 'Auto', 'Pakistan')
    
    
    def about_eMehran(self):
        print("This car is designed by students and teachers of Azad Cahiwala Institute Lahore, python batch 3.")
    

    def __del__(self):
        print('eMehran object is deleted.')

'''
eMehran1=eMehran('Pink')
# from grand parent
print('From Grand Parent.')
eMehran1.display_all()
# from parent
print('From Parent')
eMehran1.about()
# its own
print('Its own')
eMehran1.about_eMehran()
 '''       

'''
s1=Suzuki('Mehran', 'Red', 'Auto', 'Pakistan')

# accessing parent's variable
print(s1.brand)

# accessing parent's function
s1.display_all()

# accessing own variable
print(s1.madeIn)

print('********************')
# accessing own function
s1.about_car()
s1.about()
'''