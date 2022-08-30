

class Cart:
    def __init__(self) -> None:
        self.list: list = []
        self.on_sale = False
        
    def __str__(self) -> list:
        return self.list
        
    def show(self) -> None:
        print (self.list)
        
    def add_item(self, item) -> None:
        self.list.append(item)
        
    def total_price(self) -> float:
        total = 0
        if self.on_sale == False:
            for item in self.list:
                total += item.price * item.amount
        else:
            for item in self.list:
                if item.type == "fruit":
                    total += item.price * item.amount * 0.5
                else:
                    total += item.price * item.amount
        return total
    
    def total_tax(self) -> float:
        total_fruit = total_wine = 0
        if self.on_sale == False:
            for item in self.list:
                if item.type == "fruit":
                    total_fruit += item.price * item.amount
                elif item.type == "wine":
                    total_wine += item.price * item.amount
        else:
            for item in self.list:
                if item.type == "fruit":
                    total_fruit += item.price * item.amount * 0.5
                elif item.type == "wine":
                    total_wine += item.price * item.amount

        return total_fruit * 0.06 + total_wine * 0.21
    
    def activate_sale(self, bool: bool) -> None:
        self.on_sale = bool
        
class Item:
    def __init__(self, 
                 name: str, 
                 type: str, 
                 amount: int, 
                 price: float) -> None:
        self.name = name
        self.type = type
        self.amount = amount
        self.price = price
    
    def __str__(self) -> str:
        return f"name: {self.name}, type: {self.type}, amount: {self.amount}, price: {self.price}"
    
    def total_price(self) -> float:
        return self.amount * self.price

cart = Cart()


b = Item("banana", "fruit", 6, 1)
a = Item("apple", "fruit", 3, 1.5)
w = Item("bottle of wine", "wine", 2, 10)
print(b)

cart.add_item(b)
cart.add_item(a)
cart.add_item(w)


print(cart.__str__())
cart.show()

print(cart.total_price())
print(cart.total_tax())

print(b.total_price())

cart.activate_sale(True)
print(cart.on_sale)

print(cart.total_price())
print(cart.total_tax())