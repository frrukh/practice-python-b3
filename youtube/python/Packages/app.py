# Package is a folder in which we can place our code to manage our code 
# to create a Package simply create a folder and make a file with name "__init__.py"
# to import the module in a package we use this syntax: import packageName.moduleName
import ecommerce.shipping

# accessing whole package with module
ecommerce.shipping.shipping_cost()

# accessing a module directly
from ecommerce import shipping
shipping.shipping_cost()

# accessing a function directly
from ecommerce.shipping import shipping_cost
shipping_cost()

# to access multi functions we can use this syntax
from ecommerce.shipping import shipping_cost,cost
shipping_cost()
cost()