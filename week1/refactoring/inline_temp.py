
def hasDiscount(order):
    basePrice = order.basePrice()
    return basePrice > 1000

def hasDiscount(order):
    return order.basePrice() > 1000