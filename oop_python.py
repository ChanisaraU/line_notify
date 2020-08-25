class submarine :
    def __init__ (self,price):
        self.name = 'mint'
        self.sub_name = 'ship luffy'
        self.price = price #million
        self.kilo = 1000
    def missile(self):
        print('we are department of missile') 

    def calcommission(self) :
        pc = 10
        percent = self.price* (pc/100)
        print('ราคาคงเหลือ : {} บาท'.format(percent))

    def goto(self,gen,dis) :
        print(f"text goto {gen} .... {dis}")   
        self.kilo = self.kilo + dis

    def fuel(self) :
        deisel =20
        cal_feul = self.kilo + deisel   
        print("wewewewewe{}".format(cal_feul))

class electric(submarine) :
     def __init__ (self,price) :
        super().__init__(price)


price = int(input())
box = submarine(price)        
print(box.name)
box.calcommission()
print(box)
box.missile()
print(box)
box.goto('chaina',7000)
print(box.kilo)
print(box.fuel())

tesla = electric(1000)
print(tesla.goto('japan',20))