from trabajador import Trabajador
from db import Db


SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS trabajador (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	nombre TEXT NOT NULL
)
'''


SQLDDLSELECT = '''
    SELECT * FROM trabajador
'''


SQLDDLINSERT = '''INSERT INTO trabajador (nombre) VALUES '''


SQLDDLUPDATEPART1 = '''UPDATE trabajador SET nombre = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''


SQLDDLDELETE = '''DELETE FROM trabajador WHERE id = '''


SQLDDLSELECT1 = '''SELECT id FROM trabajador WHERE nombre LIKE '''


class ColeccionTrabajador:
    DBNOMBRE = "animal.db"

    def __init__(self):
        self.con = Db.conectar(self.DBNOMBRE)

        self.con.execute(SQLMDLCREATE)


    def leer(self) -> None:
        return self.con.execute(SQLDDLSELECT).fetchall()
    

    def insertar(self, trabajador):
        if self.buscar(trabajador) == 0:
            elstr = "('" + str(trabajador) + "')"
            self.con.execute(SQLDDLINSERT + elstr)


    def actualizar(self, trabajadorViejo:str, trabajadorNuevo:str):
        id = self.buscar(trabajadorViejo)
        if id != 0 and self.buscar(trabajadorNuevo) == 0:
            elstr = SQLDDLUPDATEPART1 + trabajadorNuevo 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, trabajador):
        id = self.buscar(trabajador) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, trabajador:Trabajador) -> int:
        resultado = 0
        elstr = '"' + str(trabajador) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado