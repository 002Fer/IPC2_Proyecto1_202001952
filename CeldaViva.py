class CeldaViva:

    x:int
    y:int

    def __init__(self,organismo,x,y) -> None:
        self.x=x
        self.y=y
        self.organismo=organismo

    def obtenerPosicion(self, dimensionMatriz)->int:
        return self.x + self.y * dimensionMatriz