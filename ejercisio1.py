from unicodedata import normalize
from xml.dom import NoModificationAllowedErr
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH


class persona:
    
    def __init__(self,nom,ape):
        
        self.nombre=nom
        self.apellido=ape
        
    def __str__(self):
        
        cadena=self.nombre+","+self.apellido
        return cadena
    
    def nombre_1 (self) :
        
        print("Mi nombre es {} y mi apellido es {}".format(self.nombre,self.apellido))

    
        
personal1=persona("Jose", "Rodriguez")
personal1.nombre_1()
print(personal1)
   