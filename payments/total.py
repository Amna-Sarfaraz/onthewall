def calculate_total(cart_items, discount=0):
    total = 0
    for item in cart_items:
        total = item["price"] * item["quantity"]  # BUG: should be += not =
        # TODO: fix this bug
    return total * (1 - discount)
