
cart = {}

def add_item(cart, 
             item_name, 
             item_type, 
             item_amount, 
             item_price):
    
    cart[item_name] = {
        "item_name": item_name,
        "item_type": item_type,
        "item_amount": item_amount,
        "item_price": item_price
}
    
def total_price(cart):
    total = 0
    for item in cart:
        total += cart[item]["item_amount"] * cart[item]["item_price"]
    return total

def total_tax(cart):
    total_fruit = 0
    total_wine = 0

    for item in cart:
        if cart[item]["item_type"] == "fruit":
            total_fruit += cart[item]["item_amount"] * cart[item]["item_price"]
        elif cart[item]["item_type"] == "wine":
            total_wine += cart[item]["item_amount"] * cart[item]["item_price"]
            
    tax_fruit = total_fruit * 0.06
    tax_wine = total_wine * 0.21
    return tax_fruit + tax_wine
    
add_item(cart, "banana", "fruit", 6, 1)
add_item(cart, "apple", "fruit", 3, 1.5)
add_item(cart, "bottle of wine", "wine", 2, 10)

print(cart)
print(cart["banana"]["item_name"])

print("total price: ", total_price(cart))
print("total tax: ", total_tax(cart))






