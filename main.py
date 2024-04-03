import math
# IMPORTANT: Dont use Sums() along side with other class methods
# This is because it will cause value errors


""" INSTRUCTIONS: 
    1. assuming general notation for general Riemann sum:
            RiemannSum(function, lowerBound, upperBound, optional:subIntervals)

    2. change the values of summation(function, lowerBound, upperBound, subIntervals)) to the values you want to calculate for
    3. comment out functions you dont want to use (optional)
    4. run the program

    When using the Sums method to calculate regular summation dont input any subIntervals value
        example: Riemann("2*x", 0, 10)
            Riemann(math expression, lower bound, upper bound)
"""
def main():

    function1 = Riemann("pow(x,2)-4*x", -1, 59)                     # function, lowerBound, upperBound, subIntervals

    #function1.Sums()                                              # Regular summation            
    function1.Table()                                              # individual f(x) values
    print(f"Left Riemann: {function1.Left_Riemann()}")             # Left Riemann sum 
    print(f"Right Riemann: {function1.Right_Riemann()}")           # Right Riemann sum 
    print(f"Trapezoid: {function1.Trapezoid()}")                   # Trapezoid Riemann sum



class Riemann:
    def __init__(self, function, a, b, subIntervals=1):
    
        self.lowerBound = a
        self.upperBound = b
        self.function = function

        self.nums = []
        self.subIntervals = subIntervals
        self.h = (self.upperBound - self.lowerBound) / self.subIntervals
        self.sum = 0


    def f(self, x):
        function = eval(self.function)
        return function
    
    def Sums(self):
        self.sum = 0
        while(self.lowerBound <= self.upperBound):
            function = self.f(self.lowerBound)
            self.sum += function
            print(f'F({self.lowerBound}) = {self.sum}')
            self.lowerBound += 1

        total_sum = f"total sum = {self.sum}"
        print(total_sum)
        return self.sum

    def Function_Values(self):
        self.sum = 0
        while(self.lowerBound <= self.upperBound):
            function = self.f(self.lowerBound)
            self.nums.append(function)
            self.lowerBound += self.h
        return self.nums
        
    def Table(self):
        self.sum = 0
        while(self.lowerBound <= self.upperBound):
            function = self.f(self.lowerBound)
            print(f'F({self.lowerBound}) = {function}')
            self.nums.append(function)
            self.lowerBound += self.h
        return 0
        
    def Left_Riemann(self):
        self.sum = 0
        for i in range(0, len(self.Function_Values())-1):
            self.sum += self.Function_Values()[i]

        return self.sum*self.h
     
        
    def Right_Riemann(self):
        self.sum = 0
        for i in range(1, len(self.Function_Values())):
            self.sum += self.Function_Values()[i]

        return self.sum*self.h

    
    def Trapezoid(self):
        return 0.5*(self.Left_Riemann()+self.Right_Riemann())






if __name__ == "__main__":
    main()


