# Extract Variable:
# - When you have a complicated expression, you can extract part of it into a variable with a meaningful name.
# - This can make the code easier to read and understand, as the variable name can provide context and clarify the purpose of the expression.
def renderBanner(self):
    if (self.platform.toUpperCase().indexOf("MAC") > -1) and \
       (self.browser.toUpperCase().indexOf("IE") > -1) and \
       self.wasInitialized() and (self.resize > 0):
        True

# 
def renderBanner(self):
    isMac = self.platform.toUpperCase().indexOf("MAC") > -1
    isIE = self.browser.toUpperCase().indexOf("IE") > -1
    wasResized = self.resize > 0

    if isMac and isIE and self.wasInitialized() and wasResized:
        True