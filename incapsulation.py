class ineuron1:
    def __init__(self):
        self.__students1='datascience'

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
        self.__students1=new_value

i1=ineuron1()
i1.students()
i1.__students1='data analytics'
i1.students()
i1.student_change('maruthi prasad')
i1.students()