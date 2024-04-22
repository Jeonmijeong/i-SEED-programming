# 7.
class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

class RVCars(Car):
    def __init__(self):
        super().__init__()
        self.seatNum = 0 
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum
