class CarInfo:
    def __init__(self,brand,modal,color,transmission):
        self.brand=brand
        self.modal=modal
        self.color=color
        self.transmission=transmission
    

    def display_brand(self):
        print(f'Brand: {self.brand}')


    def display_modal(self):
        print(f'Modal: {self.modal}')


    def display_color(self):
        print(f'Color: {self.color}')


    def display_transmission(self):
        print(f'Transmission: {self.transmission}')

    
    def display_all(self):
        print(f'Brand: {self.brand}')
        print(f'Modal: {self.modal}')
        print(f'Color: {self.color}')
        print(f'Transmission: {self.transmission}')
        


c1=CarInfo('Honda','Civic','Transparent','Auto')
c1.display_brand()
c1.display_modal()
c1.display_color()
c1.display_transmission()
c1.display_all()

c2=CarInfo('Toyota','Corolla','White','Manual')
c2.display_all()