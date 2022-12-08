import math
class Rest03:

    def __init__(self):
        pass
    def getSqrtResult(self, radius, height):
       
       powRad = math.pow(radius,2)
       powHeight = math.pow(height,2)

       result = math.sqrt(powRad+powHeight)
       return result