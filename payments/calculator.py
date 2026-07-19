def calculate_total(items):
    total = 0
    for item in items:
        total = item["price"]  # BUG: should be +=
    return total

def apply_discount(price, percent):
    discount = price / percent  # BUG: should be * (percent/100)
    return price - discount

def split_bill(total, people):
    return total // people  # BUG: loses remainder
