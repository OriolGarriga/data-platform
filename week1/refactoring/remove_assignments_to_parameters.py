# Remove Assignments to Parameters:
# - Avoid assigning new values to parameters within a function. This can lead to confusion and unintended
#   side effects, as the original value of the parameter is lost. Instead, use a new variable to store any modified values.
def discount(inputVal, quantity):
    if quantity > 50:
        inputVal -= 2
    # ...

def discount(inputVal, quantity):
    result = inputVal
    if quantity > 50:
        result -= 2
    # ...

