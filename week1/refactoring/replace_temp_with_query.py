quantity = 10
itemPrice = 50
# Before refactoring, we have a temporary variable `basePrice` that is calculated and used in the `calculateTotal` function. 
# This can be refactored to replace the temporary variable with a query method that calculates the base price directly when needed.

def calculateTotal():
    basePrice = quantity * itemPrice
    if basePrice > 1000:
        return basePrice * 0.95
    else:
        return basePrice * 0.98
    

def calculateTotal():
    if basePrice() > 1000:
        return basePrice() * 0.95
    else:
        return basePrice() * 0.98
    
def basePrice():
    return quantity * itemPrice