class Habitat:
    
    def __init__(self, id:int, descripcion:str) -> None:
        self.id = id
        self.descripcion = descripcion


    def leer(self):
        return self.id + ", " + self.descripcion
    

    def actualizar(self, idNuevo:int, descripcionNuevo:str):
        self.id = idNuevo
        self.descripcion = descripcionNuevo


    def delete(self):
        self.id = None
        self.descripcion = None