class Animal:
    
    def __init__(self, id:int, nombre:str) -> None:
        self.id = id
        self.nombre = nombre


    def leer(self):
        return self.id + ", " + self.nombre
    

    def actualizar(self, idNuevo:int, nombreNuevo:str):
        self.id = idNuevo
        self.nombre = nombreNuevo


    def delete(self):
        self.id = None
        self.nombre = None