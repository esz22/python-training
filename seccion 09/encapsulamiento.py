class persona:
    def __init__(self):
        self.__nombre=" "
        self.__edad=0
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def get_edad(self):
            return self.__edad
    def set_edad(self,edad):
        self.__edad=edad
    
p1=persona()
p1.set_nombre("kike")
p1.set_edad(22)
print(p1.get_nombre())
print(p1.get_edad())
#print(p1.__nombre)


#p1.set_nombre("karla")
#print(p1.get_nombre())
#p1.__nombre="karla"
#print(p1.__nombre)

