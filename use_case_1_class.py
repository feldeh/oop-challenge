

class Cart:
    def __init__(self) -> None:
        self.list: list = []
        
    def __str__(self) -> list:
        return self.list
        
    def show(self) -> None:
        print (self.list)
        
    def add_item(self, item) -> None:
        self.list.append(item)
        
    def total_price(self) -> float:
        total = 0
        for item in self.list:
            total += item.price * item.amount
        return total
    
    def total_tax(self) -> float:
        total = total_fruit = total_wine = 0
        for item in self.list:
            if item.type == "fruit":
                total_fruit += item.price * item.amount
            elif item.type == "wine":
                total_wine += item.price * item.amount
        return total_fruit * 0.06 + total_wine * 0.21
        
class Item:
    def __init__(self, name: str, type: str, amount: int, price: float) -> None:
        self.name = name
        self.type = type
        self.amount = amount
        self.price = price
        
    def __str__(self) -> str:
        return f"name: {self.name}, type: {self.type}, amount: {self.amount}, price: {self.price}"
    
    def total_price(self, type: str, amount: int, price: float, items: dict) -> float:
        total = 0
        for item in items:
            total += self.amount * self.price
        return total

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






        
        
# cart = [Item("banana", 6, 1),
#         Item("apple", 3, 1.5),
#         Item("bottle of wine", 2, 10)]
        
