# Importing modules 
#import variable_types 
#obj2=variable_types.person2('maruthi','prasad',1991)
#print(obj2._name)
#print(obj2._person2__surname)
#print(obj2.yob)


# Parent class 
class person:
    _name='sudhanshu' 
    __surname='kumar'
    yob=1990


    def _age(self,current_year):
        return current_year-self.yob 
    
    def __age2(self,current_year):
        return current_year-self.yob
    

# Creating parent class object and calling methods in it     
obj=person() 
print(obj._age(2023))
print(obj._person__age2(2023))


# Inheriting Parent class variables in child class
class employee(person):
    _name='maruthi'
    __surname='prasad'
    yob=1991

# Creating child class object and calling child parent class variables and methods  
obj1=employee()
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)
print(obj1.yob)
print(obj1._age(2023))
print(obj1._person__age2(2023))


