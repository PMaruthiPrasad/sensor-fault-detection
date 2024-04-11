class car:
    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def milage(self):
        print("milage of this car"  )

class tata(car):
    pass


c=car('solid','v6','radial')
print(c)

t=tata('grey','v8','radial2')
print(t)
print(t.milage())

