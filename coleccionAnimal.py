from animal import Animal
from db import Db


SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS animal (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	nombre TEXT NOT NULL
)
'''


SQLDDLSELECT = '''
    SELECT * FROM animal
'''


SQLDDLINSERT = '''INSERT INTO animal (nombre) VALUES '''


SQLDDLUPDATEPART1 = '''UPDATE animal SET nombre = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''


SQLDDLDELETE = '''DELETE FROM animal WHERE id = '''


SQLDDLSELECT1 = '''SELECT id FROM animal WHERE nombre LIKE '''


class ColeccionAnimal:
    DBNOMBRE = "animal.db"

    def __init__(self):
        self.con = Db.conectar(self.DBNOMBRE)

        self.con.execute(SQLMDLCREATE)


    def leer(self) -> None:
        return self.con.execute(SQLDDLSELECT).fetchall()
    

    def insertar(self, animal):
        if self.buscar(animal) == 0:
            elstr = "('" + str(animal) + "')"
            self.con.execute(SQLDDLINSERT + elstr)


    def actualizar(self, animalViejo:str, animalNuevo:str):
        id = self.buscar(animalViejo)
        if id != 0 and self.buscar(animalNuevo) == 0:
            elstr = SQLDDLUPDATEPART1 + animalNuevo 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, animal):
        id = self.buscar(animal) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, animal:Animal) -> int:
        resultado = 0
        elstr = '"' + str(animal) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado