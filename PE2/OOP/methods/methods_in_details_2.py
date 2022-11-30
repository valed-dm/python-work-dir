# The self parameter is used to obtain access to the object's instance and class variables.

# The example shows both ways of utilizing self:

class Classy:
    varia = 2

    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()
