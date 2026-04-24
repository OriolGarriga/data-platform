# Replace Temp with Query:
# - When a temporary variable is assigned the result of an expression, and that variable is used only once, 
#   we can replace the temporary variable with a query that directly computes the value. 
def hasDiscount(order):
    basePrice = order.basePrice()
    return basePrice > 1000

def hasDiscount(order):
    return order.basePrice() > 1000