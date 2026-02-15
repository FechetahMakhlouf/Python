# Import only the specified functions from the sal module
from sal import fun_1, fun_2

# Import the entire sal module (allows access using sal.function_name)
import sal

# Import the sys module to inspect Python's module search path
import sys

# Import specific functions from a package submodule
from ecommerce.sale import fun_3, fun_4

# Import the entire 'sale' module inside the ecommerce package
from ecommerce import sale

# -------------------------
# PACKAGES
# -------------------------
# A package is simply a folder that contains one or more Python modules.
# It must include an __init__.py file so Python recognizes it as a package.
#
# Example structure:
#
# ecommerce/
# ├── __init__.py
# ├── sale.py
# ├── shopping/
# │   ├── __init__.py
# │   └── sales.py
# └── another_module.py
#
# You can then import modules or functions using:
#   import ecommerce.sale
#   from ecommerce.sale import fun_3
# -------------------------

# -------------------------
# SUB-PACKAGES
# -------------------------
# A sub-package is a folder inside a package containing its own modules.
# Example: ecommerce.shopping is a sub-package of ecommerce.
#
# Here we import the 'sales' module located inside ecommerce.shopping.
from ecommerce.shopping import sales


# -------------------------
# Calling functions from ecommerce.shopping.sales
# -------------------------

sales.calc_tax()        # Calls calc_tax() from ecommerce.shopping.sales
sales.calc_shipping()   # Calls calc_shipping() from ecommerce.shopping.sales

# calc_tax()        # ERROR → Not defined in the current scope
# calc_shipping()   # ERROR → Not defined in the current scope
# These functions were NOT imported directly, only their module was imported.


# -------------------------
# Calling functions from ecommerce.sale
# -------------------------

sale.fun_3()      # Call fun_3 using the module reference
sale.fun_4()      # Call fun_4 using the module reference

# Calling functions imported directly from ecommerce.sale
fun_3()           # Direct call (imported above)
fun_4()           # Direct call (imported above)


# -------------------------
# sal module usage
# -------------------------

sal.fun_1()       # Call fun_1 from the sal module
sal.fun_2()       # Call fun_2 from the sal module

fun_1()           # Direct call (imported at the top)
fun_2()           # Direct call (imported at the top)


# -------------------------
# COMPILED PYTHON FILES
# -------------------------
# When Python runs your program, it creates .pyc files in the __pycache__ folder.
# These contain compiled bytecode so Python can run faster next time.
# -------------------------


# -------------------------
# MODULE SEARCH PATH
# -------------------------
# sys.path is a list of directories where Python looks when you use "import".
# If a module cannot be found, its folder must be added to sys.path.
# -------------------------
print(sys.path)


# Using the dir() function to list all attributes inside the 'sales' module
print(dir(sales))   # Shows functions, variables, classes, etc. defined in 'sales'

# __name__ attribute
# Shows the module's name as Python recognizes it
print(sales.__name__)

# __package__ attribute
# Shows the package that the module belongs to (empty if it's a standalone module)
print(sales.__package__)

# __file__ attribute
# Shows the file path of the module on your system
print(sales.__file__)
