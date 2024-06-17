from coleccionAnimal import ColeccionAnimal
from animal import Animal
from coleccionTrabajador import ColeccionTrabajador
from trabajador import Trabajador
from coleccionHabitat import ColeccionHabitat
from habitat import Habitat

ct = ColeccionTrabajador()
cc = ColeccionAnimal()
# print(cc.buscar(Animal('Gato')))
# print(ct.insertar(Trabajador('Jose Luis')))
# ct.borrar(Trabajador('<trabajador.Trabajador object at 0x0000027B6F21ADE0>'))
# cc.actualizar("Quedan 2 semanas de clase", "Hola qué tal!")
# ca = [("uno","dos")] + ca
print(ct.leer())