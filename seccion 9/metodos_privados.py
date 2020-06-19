class persona:
    def __init__(self,nombre,ape_paterno,ape_materno):
        self.nombre=nombre
        self._paterno=ape_paterno
        self.__materno=ape_materno
    def __metodo_privado(self):
        print(self.nombre)
        print(self._paterno)
        print(self.__materno)
    def metodo_publico(self):
        self.__metodo_privado()
    def get_materno(self):
        return self.__materno
    def set_materno(self,apellido):
        self.__materno=apellido
    
        
p1=persona("juan","lopez","perez")
p1.metodo_publico()

print(p1.nombre)
print(p1._paterno)
print(p1.get_materno())
