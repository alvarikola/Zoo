from habitat import Habitat
from db import Db


SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS habitat (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	descripcion TEXT NOT NULL
)
'''


SQLDDLSELECT = '''
    SELECT * FROM habitat
'''


SQLDDLINSERT = '''INSERT INTO habitat (descripcion) VALUES '''


SQLDDLUPDATEPART1 = '''UPDATE habitat SET habitat = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''


SQLDDLDELETE = '''DELETE FROM habitat WHERE id = '''


SQLDDLSELECT1 = '''SELECT id FROM habitat WHERE descripcion LIKE '''


class ColeccionTrabajador:
    DBNOMBRE = "animal.db"

    def __init__(self):
        self.con = Db.conectar(self.DBNOMBRE)

        self.con.execute(SQLMDLCREATE)


    def leer(self) -> str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    

    def insertar(self, habitat):
        if self.buscar(habitat) == 0:
            elstr = "('" + str(habitat) + "')"
            self.con.execute(SQLDDLINSERT + elstr)


    def actualizar(self, habitatViejo:str, habitatNuevo:str):
        id = self.buscar(habitatViejo)
        if id != 0 and self.buscar(habitatNuevo) == 0:
            elstr = SQLDDLUPDATEPART1 + habitatNuevo 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, habitat):
        id = self.buscar(habitat) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, habitat:Habitat) -> int:
        resultado = 0
        elstr = '"' + str(habitat) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado