class Employee:
    a=1
    @classmethod #used when we not wants to change our class attribute uisng object
    def show(cls):
        print(f"The class attribute is {cls.a}")


# problem!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @property
    def namne(self):
        return f"{self.fname} self.{self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


    
e=Employee()
e.a=32
e.show()
e.name="Sheh khan"