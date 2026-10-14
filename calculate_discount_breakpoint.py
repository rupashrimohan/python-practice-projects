def calculate_discount(price, discount):
    """Calculate the final price of the product."""
    final_price = price - (price * discount)
    breakpoint()
    return final_price


calculate_discount(100, 0.2)
