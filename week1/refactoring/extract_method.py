## Incorrect Design pattern - The code is not following the Single Responsibility Principle, 
#  - The `printOwing` method is responsible for both printing the banner and printing the details of the outstanding amount. 
#  - This can lead to code that is difficult to maintain and test, as changes to one aspect of the code may affect other aspects.
def printOwing(self):
    self.printBanner()

    # print details
    print("name:", self.name)
    print("amount:", self.getOutstanding())

# Correct Design pattern - The code is following the Single Responsibility Principle,
#  - The `printOwing` method is only responsible for printing the details of the
#    outstanding amount, while the `printBanner` method is responsible for printing the banner.
def printOwing(self):
    self.printBanner()
    self.printDetails()

def printDetails(self):
    print("name:", self.name)
    print("amount:", self.getOutstanding())
