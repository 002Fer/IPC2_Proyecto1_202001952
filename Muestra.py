from Nodos import listaSimple

class Muestra:
    dimensionX:int
    dimensionY:int
    listaOrganismos:listaSimple
    listaCeldasVivas:listaSimple

    def __init__(self,codigo,descripcion,dimensionX,dimensionY) -> None:
        self.codigo=codigo
        self.descripcion=descripcion
        self.dimensionX=dimensionX
        self.dimensionY=dimensionY
        self.listaOrganismos = listaSimple()
        self.listaCeldasVivas = listaSimple()