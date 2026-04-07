class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def mostrar_ejes(self):
        print("Eje X:", self.x, "Eje Y:", self.y)
    
    def opuesto(self):
        opx = self.x * -1
        opy = self.y * -1
        print("Eje -X=", opx, "Eje -Y=", opy)
    
class Linea: 
    def __init__(self, )
