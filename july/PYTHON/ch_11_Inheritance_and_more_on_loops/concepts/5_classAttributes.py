class Employee:
    a=1
    # def show(self):
    #     print(f"The class attribute is {self.a}")

    @classmethod #used when we not wants to change our class attribute isng object
    def show(cls):
        print(f"The class attribute is {cls.a}")
    
e=Employee()
e.a=32
e.show()