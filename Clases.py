import csv
class Helado:
    __gramos = float
    __precio = float
    __sabores = list
    def __init__ (self, gramos, precio):
        self.__gramos = float (gramos)
        self.__precio = float (precio)
        self.__sabores = []
    def getGramos (self):
        return self.__gramos
    def getSabores (self):
        sabores = []
        for i in self.__sabores:
            sabores.append (i.getNombre())
        return sabores
    def getPrecio (self):
        return self.__precio
    def saborVendido (self, sabor):
        self.__sabores.append (sabor)
    def contarSabor (self, sabor):
        cont = 0
        for i in self.__sabores:
            if sabor == i.getNombre():
                cont += 1
        return cont
    def buscarCodigo (self, code):
        gramosVendidos = 0
        i = 0
        while i<len (self.__sabores) and self.__sabores[i].getCodigo()!=code:
            i += 1
        if i<len (self.__sabores):
            gramosVendidos = self.__gramos/len (self.__sabores)
        return gramosVendidos

class Sabor:
    __idSabor = int
    __ingredientes = str
    __nombreSabor = str
    def __init__ (self, idSabor, ingredientes, nombreSabor):
        self.__idSabor = int (idSabor)
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
    def getNombre (self):
        return self.__nombreSabor
    def getCodigo (self):
        return self.__idSabor

class ManejaSabores:
    def __init__ (self):
        self.__sabores = []
    def agregarSabor (self, sabor):
        self.__sabores.append (sabor)
    def testSabores (self):
        archivo = open ('sabores.csv')
        reader = csv.reader (archivo, delimiter=';')
        for fila in reader:
            sabor = Sabor (fila[0], fila[1], fila[2])
            self.agregarSabor (sabor)
        archivo.close()
    def buscarSabor (self, sabor):
        i = 0
        while i<len (self.__sabores) and self.__sabores[i].getNombre()!=sabor:
            i += 1
        if i<len (self.__sabores):
            sabor = self.__sabores[i]
        else:
            print ('No se encontro el sabor buscado.')
            sabor = None
        return sabor
    def contarSabores (self, mH):
        listaSabores = []
        for i in self.__sabores:
            sabor = []
            nombreSabor = i.getNombre()
            cont = mH.contarSabor (nombreSabor)
            sabor.append (cont)
            sabor.append(nombreSabor)
            listaSabores.append (sabor)
        listaSabores.sort (reverse=True)
        for i in range(5):
            print ('Top {} de sabores mas pedidos: {}'.format (i+1, listaSabores[i][1]))

class ManejaHelados:
    def __init__ (self):
        self.__helVend = []
    def agregarVenta (self, venta):
        self.__helVend.append (venta)
    def cargarVenta (self, mS, gramos, precio):
        helado = Helado (gramos, precio)
        cantSabores = input ('Ingrese cantidad de sabores a comprar: ')
        for i in range (int (cantSabores)):
            sabor = input ('Ingrese sabor: ')
            sVendido = mS.buscarSabor (sabor)
            if sVendido != None:
                helado.saborVendido (sVendido)
        self.agregarVenta (helado)
    def contarSabor (self, sabor):
        cont = 0
        for i in self.__helVend:
            cont += i.contarSabor (sabor)
        return cont
    def buscarGramos (self, code):
        total = 0
        for helado in self.__helVend:
            total += helado.buscarCodigo (int (code))
        print ('La cantidad de gramos vendidos para el helado de codigo {} es: {:.2f}'.format (code, total))
    def inciso4 (self, gramos):
        sabores = []
        for i in self.__helVend:
            if gramos == i.getGramos():
                aux = i.getSabores()
                for sab in aux:
                    if sab not in sabores:
                        sabores.append (sab)
        print ('Los sabores vendidos para los helados de {}g son:'.format (gramos))
        for i in sabores:
            print (i)
    def precioRecaudado (self):
        total = 0
        for i in self.__helVend:
            total += i.getPrecio()
        print ('El total recaudado es: ${:.2f}'.format (total))
    
class Menu:
    __switcher = None
    def __init__ (self):
        self.__switcher = {'1': self.opcion1,
                           '2': self.opcion2,
                           '3': self.opcion3,
                           '4': self.opcion4,
                           '5': self.opcion5}
    def opcion (self, op, mH, mS):
        bul = False
        funcion = self.__switcher.get (op)
        if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
            funcion (mH, mS)
        else:
            print ('Fin del programa...')
            bul = True
        return bul
    def opcion1 (self, mH, mS):
        gramos = input ('Ingrese el peso del helado a vender: ')
        precio = input ('Precio: ')
        mH.cargarVenta (mS, gramos, precio)
    def opcion2 (self, mH, mS):
        mS.contarSabores (mH)
    def opcion3 (self, mH, mS):
        code = input ('Ingrese un numero de sabor: ')
        mH.buscarGramos (code)
    def opcion4 (self, mH, mS):
        gramos = input ('Ingrese tamaño de un tipo de helado: ')
        mH.inciso4 (int (gramos))
    def opcion5 (self, mH, mS):
        mH.precioRecaudado()