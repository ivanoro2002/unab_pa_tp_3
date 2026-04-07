class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.eje_x
    
    def eje_y(self):
        return self.eje_y
    
    def mostrar_ejes(self):
        print("Eje X:", self.eje_x, "Eje Y:", self.eje_y)
    
    def opuesto(self):
        opx = self.eje_x * -1
        opy = self.eje_y * -1
        print("Eje -X=", opx, "Eje -Y=", opy)
    
    class Linea: 
        def __init__(self, ):
            self.punto1 = Punto ("x",1, "y",2)
print (Punto(1,2).mostrar_ejes())

