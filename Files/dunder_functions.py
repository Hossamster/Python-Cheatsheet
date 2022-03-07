# Dunder functions 
class Order:
    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):
        return len(self.cart) # must return integer value onlyyyyyyyyy

    def __call__(self):
        print(self.customer)
    
    def __str__(self):
        return f"{self.customer} has bought {self.cart}" # must be string

    def __repr__(self):
        return f"Order(list of items, customer name)"

    def __bool__(self):
        return len(self.cart) > 0 

    def __add__(self,other):
        self.cart.append(other)
        return self
    
    def __radd__(self,other):
        c = self.cart.copy()
        c.insert(0,other)
        return Order(c,self.customer)
    def __getitem__(self,index):
        return self.cart[index]

    def __setitem__(self,key,value):
        self.cart[key] = value

order = Order(['laptop','monitor',"mouse"],'Hossam Kamel')

print(len(order)) # __len__

order() # __call__

# print(order) # <__main__.Order object at 0x0000024C925A7D60>

# after making __str__ method

print(order) # Hossam Kamel has bought ['laptop', 'monitor', 'mouse']

print(repr(order)) # Order(list of items, customer name)

# if order:
#     print(f"{order.customer}'s order is processing")
# else:
#     print("Shopping cart is empty")

# order = order + 'usb hub'
# print(order)

order = 'usb hub' + order
print(order.cart)

print(order[0])
order[0] = 'flash'
print(order[0])
