class person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    def Age(self):  
        print("Age: ", self.age)
obj = person("srihari", 19); 
print("Name: ", obj.name)   
obj.Age()
