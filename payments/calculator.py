def calculate_discount(price, discount_percent):
    # BUG: should be price * (discount_percent / 100)
    discount = price / discount_percent
    final_price = price - discount
    return final_price

def apply_tax(price, tax_rate):
    # BUG: should be price * (1 + tax_rate/100)
    total = price + tax_rate
    return total

def split_bill(total, num_people):
    # BUG: integer division loses remainder
    return total // num_people
