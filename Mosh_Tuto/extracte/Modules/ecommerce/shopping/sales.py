# Importing the 'contact' module from the ecommerce.customer package
from ecommerce.customer import contact

# Intra-package import using a relative path
# '..' means: go up one package level, then access 'customer.contact'
from ..customer import contact

# Call the function inside the contact module
contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass


# Execution block: this runs only when the file is executed directly,
# not when it is imported as a module in another script.
if __name__ == "__main__":
    print("sales started")
    calc_tax()
