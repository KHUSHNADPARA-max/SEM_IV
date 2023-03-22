class claculator:
    def __init__(self, num):
        self.num = num
        
    def getSquare(self):
        print(f"The Square of {self.num} is {self.num ** 2}")
    def getSquareRoot(self):
        print(f"The Square of {self.num} is {self.num ** 0.5}")
    def getCube(self):
        print(f"The Square of {self.num} is {self.num ** 3}")
    
obj = claculator(9)

obj.getSquare()
obj.getSquareRoot()
obj.getCube()
