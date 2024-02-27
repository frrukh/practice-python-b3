# Modules is a method to divide the code in different files and then we can import files 
# Modules allows us to use the same code again and again instead to write it multi times

# Importing a complete module file
import convertors
# accessing function from imported file
convertors.kg_to_lbs(5)

# Importing a specific function from a specific module
from convertors import lbs_to_kg
# convertors.lbs_to_kg(66)
lbs_to_kg(20)
