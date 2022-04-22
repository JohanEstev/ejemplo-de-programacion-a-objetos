class Animal:
    
    def __init__ (self ,especie ,edad ):
        
        self.especie=especie 
        self.edad=edad


    def hablar (self):
        
        pass
    
    
    def moverse(self):
        
        pass
    
    
    def describeme(self):
        
        
        print("soy un Animal del tipo ", self.especie , " y tengo" , self.edad,"años")
        
class perro(Animal):
    
    def hablar(self):
        
        print("Guau")
        
    def moverse(self):
        
        print("caminando con 4 patas")
        
class Vaca(Animal):
    
    def hablar(self):
        
        print("Muu")
        
    def moverse(self):
        
        print("Caminando con 4 patas") 



animal=Animal("manifero",10)
animal.describeme()
print("-"*40)
mi_perro=perro("manifero",20)
mi_perro.describeme()
mi_perro.hablar()
mi_perro.moverse()
print("-"*40)
mi_vaca=Vaca("manifero",23)
mi_vaca.describeme()
mi_vaca.hablar()
mi_vaca.moverse()
print("-"*40)
        
        