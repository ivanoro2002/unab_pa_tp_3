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
    def __init__(self, p_a, p_b):
        self.p_a = p_a
        self.p_b = p_b

    def move_der(self, distance):
        self.p_a.x += distance
        self.p_b.x += distance
    
    def move_izq(self, distance):
        self.p_a.x -= distance
    
    def move_arriba(self, distance):
        self.punto_a.y += distance
        self.punto_b.y += distance
    
    def move_abajo(self, distance):
        self.punto_a.y -= distance
        self.punto_b.y -= distance
