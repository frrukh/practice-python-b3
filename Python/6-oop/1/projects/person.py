class Person:
    def __init__(self,name,age,color,height,blood_group,gender):
        self.name=name
        self.age=age
        self.color=color
        self.height=height
        self.blood_group=blood_group
        self.gender=gender
    
    def display_all(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Color: {self.color}')
        print(f'Height: {self.height}')
        print(f'Blood group: {self.blood_group}')
        print(f'Gender: {self.gender}')


person1=Person('Zain',26,'brown','5ft-5in','A+','Male')
person1.display_all()

print('***************')

person2=Person('Ali',23,'white','6ft-1in','c-','Male')
person2.display_all()