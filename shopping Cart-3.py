class Product: 
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.you_save=price=deal_price
    def display_product_detail(self):
        print("Product :{}".format(self.name))
        print("Price :{}".format(self.price))
        print("Deal_price :{}".format(self.deal_price))
        print("you save :{}".format(self.you_save))
        print("Rating :{}".format(self.rating))
class Electronicitem(Product):
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months=warranty_in_months
    
    def display_product_detail(self):
        super().display_product_detail()
        print("Warranty :{}".format(self.warranty_in_months))

class Groceryitem(Product):
    def __init__(self,name,price,deal_price,rating,packed_date,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.packed_date=packed_date
        self.expiry_date=expiry_date
    
    def display_product_detail(self):
        super().display_product_detail()
        print("Packed date :{}".format(self.packed_date))
        print("Expiry date :{}".format(self.expiry_date))

class order:
    delivery_charges={
        "prime_numbers":0,
        "non_prime_number":50
    }
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
    def add_items(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_detail(self):
        print('')
        for product,quantity in self.items_in_cart:
            product.display_product_detail()
            print("Quantity :{}".format(quantity))
            print('........................')
        print("delivery speed :{}".format(self.delivery_speed))
        print("delivery address :{}".format(self.delivery_address))



tv=Electronicitem("tv",4500,2000,4.5,24)
key=Electronicitem("keyboard",5000,2000,3.4,24)
milk=Groceryitem("Milk",40,20,4.5,"1/02/22","2/09/22")

order=order("prime_numbers","karimnagar")
order.add_items(tv,1)
order.add_items(key,1)
order.add_items(milk,1)
order.display_order_detail()