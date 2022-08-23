


class Item:
    def __init__(self, type: str, amount: int, price: float) -> None:
        self.type = type
        self.amount = amount
        self.price = price
        
    def __str__(self) -> str:
        return f"type: {self.type}, amount: {self.amount}, price: {self.price}"
    
    def total_price(self, type: str, amount: int, price: float, items: dict) -> float:
        total = 0
        for item in items:
            total += self.amount * self.price
        return total
        
        
        
basket = [Item("banana", 6, 1),
          Item("apple", 3, 1.5),
          Item("bottle of wine", 2, 10)]
        

print(basket.total_price())