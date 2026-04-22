## Inline Method:
# - When a method's body is as clear as its name, we can inline it and remove the method. 
#       This can simplify the code and reduce the number of methods, making it easier to read and
# - maintain. However, it's important to ensure that the inlined code is still clear and does not 
#       violate the Single Responsibility Principle. If the method being inlined has multiple responsibilities, 
#       it may be better to keep it as a separate method.

class PizzaDelivery:
    # ...
    def getRating(self):
        return 2 if self.moreThanFiveLateDeliveries() else 1
  
    def moreThanFiveLateDeliveries(self):
        return self.numberOfLateDeliveries > 5
    
# After inlining the `moreThanFiveLateDeliveries` method, we can simplify the `getRating` method as follows:
class PizzaDelivery:
  # ...
  def getRating(self):
    return 2 if self.numberOfLateDeliveries > 5 else 1