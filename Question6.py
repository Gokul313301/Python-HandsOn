def calculate_bill(price, quantity):
    total = price * quantity
    if total > 2000:
        discount = total * 0.10
        total -= discount
    return total

print(calculate_bill(100,24))
