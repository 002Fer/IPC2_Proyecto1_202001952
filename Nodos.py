class Nodo:
    def __init__(self, datos):
        self.datos=datos
        self.siguiente=None

class listaSimple:
    def __init__(self):
        self.cabeza=None
        self.tamaño=0
         

    def insertar(self,datos):
        nuevoNodo=Nodo(datos)
        if self.tamaño == 0:
            self.cabeza = nuevoNodo

        else:
            auxiliar=self.cabeza
            while auxiliar.siguiente !=None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nuevoNodo 
        self.tamaño += 1

    def listar_ac(self):
        auxiliar_dato=self.cabeza
        while auxiliar_dato !=None:
            print(auxiliar_dato.datos)







     
            


            

        
        




