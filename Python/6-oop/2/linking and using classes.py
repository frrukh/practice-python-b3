from p_vehicle import Vehicle
from c1_honda import Honda
from c2_suzuki import Suzuki , eMehran


# Vehicle object
my_vehicle = Vehicle('Toyota', 'Corolla', 'White', 'Auto')

my_vehicle.display_all()
print('-------------------------')

# honda object
my_honda = Honda('Civic', 'Red', 'Manual')

# parent function
my_honda.display_all()
# own function
my_honda.about()
print('-------------------------')

# suzuki object
my_suzuki = Suzuki('Mehran', 'Blue', 'Auto', 'Pakistan')

# parent function
my_suzuki.display_all()
# own function
my_suzuki.about_Suzuki()
print('-------------------------')

# eMehran object
my_eMehran = eMehran('Purple')

# Grand parent function
my_eMehran.display_all()
# Parent function
my_eMehran.about_Suzuki()
# Own Function
my_eMehran.about_eMehran()
