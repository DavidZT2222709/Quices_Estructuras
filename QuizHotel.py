class Nodo:
    def __init__(self, nombre, cedula, habitacion, orden_llegada):
        self.nombre = nombre
        self.cedula = cedula
        self.habitacion = habitacion
        self.orden_llegada = orden_llegada
        self.siguiente = None


class Hotel:
    def __init__(self):
        self.entradas_hotel = None
        self.salidas_hotel = None

    def ingreso(self, nombre, cedula, habitacion, orden_llegada):
        nuevo_nodo = Nodo(nombre, cedula, habitacion, orden_llegada)
        nuevo_nodo.siguiente = self.entradas_hotel
        self.entradas_hotel = nuevo_nodo

    def salida(self, habitacion):
        nodo_actual = self.entradas_hotel
        nodo_anterior = None

        while nodo_actual != None and nodo_actual.habitacion != habitacion:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_actual != None:
            if nodo_anterior != None:
                nodo_anterior.siguiente = nodo_actual.siguiente
            else:
                self.entradas_hotel = nodo_actual.siguiente

    def consulIndividual(self, cedula):
        nodo_actual = self.entradas_hotel

        while nodo_actual != None and nodo_actual.cedula != cedula:
            nodo_actual = nodo_actual.siguiente

        if nodo_actual != None:
            return f"Cedula: {nodo_actual.cedula}, Nombre: {nodo_actual.nombre}, Habitacion: {nodo_actual.habitacion}, Orden de llegada: {nodo_actual.orden_llegada}"
        else:
            return "El huesped no se encuentra registrado en el hotel"

    def consulTotal_cedula(self,cedula):
        huesped = []
        nodo_actual = self.entradas_hotel

        while nodo_actual != None:
            if nodo_actual.cedula == cedula:
                huesped.append(f"Cedula: {nodo_actual.cedula}, Nombre: {nodo_actual.nombre}, Habitacion: {nodo_actual.habitacion}, Orden de llegada: {nodo_actual.orden_llegada}")
                nodo_actual = nodo_actual.siguiente
            if not huesped:
                return "No tenemos huespedes registrados con ese numero de cedula"
            else:
                return huesped

    def consulTotal_ordenllegada(self, Orden_llegada):
        huesped = []
        nodo_actual = self.entradas_hotel

        while nodo_actual != None:
            huesped.append(f"Cedula: {nodo_actual.cedula}, Nombre: {nodo_actual.nombre}, Habitacion: {nodo_actual.habitacion}, Orden de llegada: {nodo_actual.orden_llegada}")
            nodo_actual = nodo_actual.siguiente
        if not huesped:
            return "No tenemos huespedes registrados en esa posicion de llegada"
        else:
            return huesped

    def disponibles(self):
        habitaciones_ocupadas = {entradas.habitacion for entradas in self.entradas_hotel}
        habitaciones_desocupadas = [i for i in range(1,101) if i not in habitaciones_ocupadas]
        return habitaciones_desocupadas

    def desocupadas(self):
        habitaciones_ocupadas = {entrada.habitacion for entrada in self.entradas_hotel}
        return habitaciones_ocupadas

GojoSensei = Hotel()

GojoSensei.ingreso("Nichol", 37758942, 23, 2)
GojoSensei.ingreso("David", 1006746283,43, 8)
GojoSensei.ingreso("Dannys", 42496557, 100, 1)

GojoSensei.consulIndividual(42496557)
GojoSensei.consulTotal_cedula(37758942)
GojoSensei.consulTotal_ordenllegada(8)

GojoSensei.salida(43)