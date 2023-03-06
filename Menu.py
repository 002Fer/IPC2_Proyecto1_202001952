from Nodos import listaSimple
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from Muestra import Muestra
from CeldaViva import CeldaViva
from Organismo import Organismo
from os import system


class menu:

    def __init__(self) -> None:

        self.mostrarMenu()
    def mostrarMenu(self):
        opcion =''
        while opcion != '6':
            print("-------------Menu-------------")
            print("1. Abrir archivo")
            print("2. Mostrar grafica")
            print("3. Ingresar Celula")
            print("4. Celdas para sobrevivir")
            print("5. Crear XML")
            print("6. Salir")
            opcion=input("Ingrese una de las opciones: ")
            
            if opcion== '1':
                archivo=askopenfilename(title="Abrir un archivo")
                archivoxml=minidom.parse(archivo)
                self.procesoInformacion(archivoxml)


                print("Se cargo el archivo")
                    
            elif opcion=='2':
                self.crearGrafica()

            elif opcion=='3':
                self.insertarNueva()
                self.crearGrafica()
                


            elif opcion=='4':
                
                listar=self.muestraAnalizada.listaCeldasVivas
                nodo=listar.cabeza
                while nodo!=None:
                    celda:CeldaViva=nodo.datos
                    print("Listado de celdas vivas")
                    print(celda.x +" "+celda.y+" "+celda.organismo)
                    nodo=nodo.siguiente
                    print("")

                print("Elija una de ceula a analizar")
                
                
                



    def procesoInformacion(self,archivoXml):

        columnasX = archivoXml.getElementsByTagName('columnas')
        filasY = archivoXml.getElementsByTagName('filas')
        muestra = archivoXml.getElementsByTagName('muestra')

        codigoMuestra = muestra[0].childNodes[1].firstChild.data
        nombreMuestra= muestra[0].childNodes[3].firstChild.data

        dimensionX= columnasX[0].childNodes[0].data
        dimensionY= filasY[0].childNodes[0].data

        nuevaMuestra = Muestra(codigoMuestra,nombreMuestra,dimensionX,dimensionY)

        organismoXml= archivoXml.getElementsByTagName('organismo')

        for organismo in organismoXml:
            
            codigo=organismo.childNodes[1].firstChild.data
            nombre=organismo.childNodes[3].firstChild.data
            nuevoOrganismo=Organismo(codigo,nombre)
            nuevaMuestra.listaOrganismos.insertar(nuevoOrganismo)
        
        celdasVivasXML=archivoXml.getElementsByTagName('celdaViva')

        for celdaviva in celdasVivasXML:

            fila =celdaviva.childNodes[1].firstChild.data
            columna= celdaviva.childNodes[3].firstChild.data
            codigoOrganismo=celdaviva.childNodes[5].firstChild.data

            nuevaCeldaViva=CeldaViva(codigoOrganismo, columna, fila)

            nuevaMuestra.listaCeldasVivas.insertar(nuevaCeldaViva)

        self.muestraAnalizada=nuevaMuestra

    def insertarNueva(self):
        
        posx=input("Ingrese la posicion x de la nueva celula: ")
        posy=input("ingrese la posicion y de la nueva celula ")
        nombreCel=input("Ingrese el codigo del organismo ")
        celva_viva=CeldaViva(nombreCel,posx,posy)
        self.muestraAnalizada.listaCeldasVivas.insertar(celva_viva)
        
        
        

        print('ser cargo la nueva muestra')



    def crearGrafica(self):
        x= self.muestraAnalizada.dimensionX
        y= self.muestraAnalizada.dimensionY

        codigoGrapviz=""" 
            digraph structs{
                node[shape=record];
                MATRIZ [
                    label="
        
        
        """

        cuentax=-1
        cuentay=-1
        while(cuentax<int(x)):
            if cuentay==-1:
                codigoGrapviz=codigoGrapviz+'{x,y'
            else:
                codigoGrapviz=codigoGrapviz+'{'+str(cuentax)

            cuentay=0
            while(cuentay< int(y)):
                if cuentax==-1:
                    codigoGrapviz=codigoGrapviz+'|'+str(cuentay)

                else:
                    lisCeldasVivas=self.muestraAnalizada.listaCeldasVivas
                    nodoActual=lisCeldasVivas.cabeza
                    codigoOrganismo=""

                    while nodoActual!=None:
                        celdaViva:CeldaViva= nodoActual.datos
                        coordenadaX=celdaViva.x
                        coordenadaY=celdaViva.y

                        if(int(cuentax)==int(coordenadaX) and int(cuentay)==int(coordenadaY)):
                            print("CeldaViva")
                            print(celdaViva.organismo)
                            codigoOrganismo="|"+celdaViva.organismo
                            break
                        else:
                            codigoOrganismo='|'
                        nodoActual=nodoActual.siguiente

                    codigoGrapviz=codigoGrapviz+codigoOrganismo
                cuentax==0

                cuentay=cuentay+1
            cuentax=cuentax+1

            if(cuentax==int(x)):
                codigoGrapviz=codigoGrapviz+'}'

            else:
                codigoGrapviz=codigoGrapviz+'}|'
        codigoGrapviz=codigoGrapviz+"""
                        "];
            }
        """

        mi_archivo=open('grafica.dot','w')
        mi_archivo.write(codigoGrapviz)
        mi_archivo.close()
'''
        system('dot -Tpng grafica.dot -o grafica.png')
        system('cd ./grafica.png')
        startfile('grafica.png')'''


cargarmenu=menu()
cargarmenu.mostrarMenu()

