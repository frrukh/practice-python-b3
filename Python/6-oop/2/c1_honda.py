# To import class first we gie the path and then class name
from p_vehicle import Vehicle

# the parent name will be written in the parentheses of child class like:
class Honda(Vehicle):
    def __init__(self,model, color, transmission):
        super().__init__('Honda', model, color, transmission) # Super function is used to target the function of parent

    def about(self):
        print('Honda is a renowned Japanese multinational corporation primarily known for manufacturing automobiles, motorcycles, and power equipment.')
    
    def __del__(self):
        print('Honda object is deleted.')


h1=Honda('Civic', 'red', 'Manual')
# calling the function of parent
h1.display_all()
# calling its own function
h1.about()