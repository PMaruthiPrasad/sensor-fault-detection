from Inheritence import employee
#print(Inheritence)
obj1=employee()
obj1

# with one underscore that is protected variable and accessing those variables mentioned below
# with two underscores that is private variable and accessing those variables mentioned below
class person2:
    def __init__(self, name,surname,yob):
        self._name = name
        self.__surname =surname
        self.yob = yob
    
sudh=person2('sudhanshu','kumar',1990)
print(sudh._name)
print(sudh._person2__surname)
print(sudh.yob)