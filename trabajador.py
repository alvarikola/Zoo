class Trabajador:
    
    def __init__(self, id:int, nombre:str, puesto:str) -> None:
        self.id = id
        self.nombre = nombre
        self.puesto = puesto


    def leer(self):
        return self.id + ", " + self.nombre + ", " + self.puesto
    

    def actualizar(self, idNuevo:int, nombreNuevo:str, puestoNuevo:str):
        self.id = idNuevo
        self.nombre = nombreNuevo
        self.puesto = puestoNuevo


    def delete(self):
        self.id = None
        self.nombre = None
        self.puesto = None